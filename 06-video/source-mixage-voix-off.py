"""Teaser Jàng — voix off (Piper, voix siwis CC-BY 4.0) + une seule musique (Pixabay « Lofi Study », FASSounds) + sons d'interface légers."""
import subprocess, sys, wave, numpy as np
sys.path.insert(0, '/tmp/claude-0/voix'); from lignes import L

SR = 44100; T = 73.0; N = int(SR * T)
V = '/tmp/claude-0/voix/'

def rdwav(p):
    w = wave.open(p); ch = w.getnchannels(); sr = w.getframerate()
    x = np.frombuffer(w.readframes(w.getnframes()), '<i2').astype(np.float64) / 32768
    x = x.reshape(-1, ch)
    if sr != SR:  # rééchantillonnage linéaire suffisant ici (voix 22,05 kHz → 44,1 kHz)
        n = int(len(x) * SR / sr); t = np.linspace(0, len(x) - 1, n)
        x = np.stack([np.interp(t, np.arange(len(x)), x[:, c]) for c in range(ch)], 1)
    return x

def hp(x, fc):
    X = np.fft.rfft(x, axis=0); f = np.fft.rfftfreq(len(x), 1 / SR)[:, None]
    return np.fft.irfft(X * (f / fc) ** 2 / np.sqrt(1 + (f / fc) ** 4), len(x), axis=0)

# ---------- voix off ----------
voice = np.zeros((N, 2))
starts = []
for i, (a, b, t) in enumerate(L):
    ls = 0.88 if i == 3 else 1.05
    a = 15.85 if i == 3 else a + 0.05
    sil = '0.1' if i == 3 else '0.25'
    out = f'{V}vo{i:02d}.wav'
    subprocess.run(['python3', '-m', 'piper', '-m', V + 'fr_FR-siwis-medium.onnx', '-f', out,
                    '--length-scale', str(ls), '--sentence-silence', sil], input=t.encode(), check=True, capture_output=True)
    v = rdwav(out)[:, :1]
    nz = np.where(np.abs(v[:, 0]) > 0.005)[0]; v = v[max(0, nz[0] - 200):nz[-1] + 2000]   # silences de début/fin retirés
    v = hp(v, 90)
    # compression douce (niveau régulier d'une phrase à l'autre)
    env = np.convolve(np.abs(v[:, 0]), np.ones(441) / 441, 'same')
    g = np.where(env > 0.08, (0.08 / np.maximum(env, 1e-9)) ** 0.5, 1.0)
    v = v[:, 0] * g
    v = v / (np.sqrt((v[np.abs(v) > 0.01] ** 2).mean()) + 1e-9) * 0.12
    dur = len(v) / SR
    assert a + dur <= (L[i + 1][0] if i + 1 < len(L) else T) + 0.05, (i, a, dur)
    k = int(a * SR); voice[k:k + len(v), 0] += v; voice[k:k + len(v), 1] += v
    starts.append((a, a + dur))
    print(f'{i:2d} {a:5.2f} → {a+dur:5.2f}  {t}')

# légère réverbération de pièce pour fondre la voix dans le mix
def room(x, secs=0.6, mix=0.08):
    n = int(secs * SR); t = np.arange(n) / SR; ir = np.random.default_rng(2).standard_normal(n) * np.exp(-t * 6.9 / secs)
    ir /= np.sqrt((ir ** 2).sum()); L2 = len(x) + n
    y = np.fft.irfft(np.fft.rfft(x[:, 0], L2) * np.fft.rfft(ir, L2), L2)[:len(x)]
    return x * (1 - mix) + y[:, None] * mix
voice = room(voice)

# ---------- musique : une seule piste, sans coupe ----------
m = rdwav('/tmp/claude-0/px/lofi.wav')
OFF = 86.4 - 15.8          # le beat revient à 86,4 s dans le morceau → 15,8 s dans la vidéo (« Voici Jàng »)
music = m[int(OFF * SR):int(OFF * SR) + N].copy()
music = np.pad(music, ((0, N - len(music)), (0, 0)))
music = music / np.sqrt((music ** 2).mean()) * 10 ** (-20 / 20)
t = np.arange(N) / SR
music *= np.clip(t / 1.2, 0, 1)[:, None]                 # entrée en fondu
music *= np.clip((T - t) / 2.5, 0, 1)[:, None]           # sortie

# ducking : la musique baisse de 9 dB quand la voix parle
mask = np.zeros(N)
for a, b in starts: mask[int(a * SR):int(b * SR)] = 1
k = int(0.35 * SR); kern = np.ones(k) / k
mask = np.clip(np.convolve(mask, kern, 'same') * 1.6, 0, 1)
duck = 10 ** (-9 * mask / 20)
music *= duck[:, None]

# ---------- sons d'interface (très légers) ----------
ui = rdwav('/tmp/claude-0/vid/sfx_ui.wav')[:N] * 0.45

mix = music + voice + ui
pk = np.abs(mix).max(); mix *= min(1, 0.89 / pk)

def save(name, x):
    x = np.clip(x, -1, 1); d = (x * 32767).astype('<i2')
    f = wave.open(name, 'wb'); f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes(d.tobytes()); f.close()
save('/tmp/claude-0/vid/vo_mix.wav', mix); save('/tmp/claude-0/vid/vo_voix.wav', voice); save('/tmp/claude-0/vid/vo_musique.wav', music / duck[:, None] * 0.89 / max(pk, 0.89))
print('ok')
