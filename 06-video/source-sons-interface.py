"""Bande-son originale du teaser Jàng (73 s) — synthèse numpy, aucun échantillon externe.
Sorties : musique.wav, sfx.wav (pistes séparées pour CapCut) et mix.wav (stéréo)."""
import numpy as np, wave

SR = 44100
T = 73.0
N = int(SR * T)
rng = np.random.default_rng(7)

def mtof(m): return 440.0 * 2 ** ((m - 69) / 12)
def buf(): return np.zeros((N, 2))

def place(dst, sig, t0, gain=1.0, pan=0.0):
    i = int(t0 * SR)
    if i >= N: return
    if sig.ndim == 1:
        l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
        sig = np.stack([sig * l, sig * r], 1)
    n = min(len(sig), N - i)
    dst[i:i + n] += sig[:n] * gain

def onepole_lp(x, fc):
    a = np.exp(-2 * np.pi * fc / SR); y = np.empty_like(x); s = 0.0
    for k in range(len(x)):
        s = (1 - a) * x[k] + a * s; y[k] = s
    return y

def lp_fast(x, fc):  # filtre passe-bas par FFT (doux)
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    return np.fft.irfft(X / np.sqrt(1 + (f / fc) ** 4), len(x))

def hp_fast(x, fc):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR)
    return np.fft.irfft(X * (f / fc) ** 2 / np.sqrt(1 + (f / fc) ** 4), len(x))

def bp_fast(x, lo, hi): return lp_fast(hp_fast(x, lo), hi)

def reverb(x, secs=2.2, mix=0.25, seed=1):
    n = int(secs * SR); t = np.arange(n) / SR
    g = np.random.default_rng(seed)
    out = np.empty_like(x)
    for c in range(2):
        ir = g.standard_normal(n) * np.exp(-t * 6.9 / secs)
        ir = lp_fast(ir, 6000); ir /= np.sqrt((ir ** 2).sum())
        L = len(x) + n
        y = np.fft.irfft(np.fft.rfft(x[:, c], L) * np.fft.rfft(ir, L), L)[:len(x)]
        out[:, c] = x[:, c] * (1 - mix) + y * mix * 1.6
    return out

# ---------- instruments ----------
def piano(m, dur=2.5, vel=0.5):
    f = mtof(m); n = int(dur * SR); t = np.arange(n) / SR
    s = np.zeros(n)
    for h in range(1, 9):
        fh = f * h * np.sqrt(1 + 0.0004 * h * h)
        if fh > 16000: break
        s += np.sin(2 * np.pi * fh * t) * (0.6 ** (h - 1)) * np.exp(-t * (1.2 + 0.9 * h))
    att = np.minimum(t / 0.004, 1)
    hammer = rng.standard_normal(n) * np.exp(-t * 90) * 0.04
    return (s * att + hammer) * vel * np.minimum(1, (dur - t) / 0.05)

def pad(ms, dur, vel=0.12, bright=1800):
    n = int(dur * SR); t = np.arange(n) / SR; s = np.zeros(n)
    for m in ms:
        for d in (-0.08, 0.0, 0.07):
            f = mtof(m) * 2 ** (d / 12)
            ph = 2 * np.pi * f * t + rng.uniform(0, 6.28)
            saw = 2 * ((ph / (2 * np.pi)) % 1) - 1
            s += saw
    s = lp_fast(s, bright)
    env = np.minimum(t / 0.9, 1) * np.minimum(1, (dur - t) / 0.9)
    return s * env * vel / len(ms)

def pluck(m, dur=0.6, vel=0.25):
    f = mtof(m); n = int(dur * SR); p = int(SR / f)
    b = rng.uniform(-1, 1, p); out = np.empty(n)
    for k in range(n):
        out[k] = b[k % p]; b[k % p] = 0.5 * (b[k % p] + b[(k + 1) % p]) * 0.996
    return out * vel

def kick(vel=0.9):
    n = int(0.45 * SR); t = np.arange(n) / SR
    f = 45 + 95 * np.exp(-t * 28)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 7) * vel

def hat(vel=0.08):
    n = int(0.08 * SR); t = np.arange(n) / SR
    return hp_fast(rng.standard_normal(n), 7000) * np.exp(-t * 60) * vel

def sub_boom(vel=0.9):
    n = int(2.5 * SR); t = np.arange(n) / SR
    f = 38 + 40 * np.exp(-t * 6)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 2.2) * vel

# ---------- sons d'interface / transitions ----------
def riser(dur=2.5, vel=0.25):
    n = int(dur * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
    out = np.zeros(n); seg = 2048
    for i in range(0, n, seg):
        fc = 300 * (40 ** (i / n))
        out[i:i + seg] = bp_fast(x[i:i + seg] if len(x[i:i+seg])==seg else np.pad(x[i:],(0,seg-len(x[i:]))), fc * 0.6, fc * 1.6)[:len(out[i:i+seg])]
    return out * (t / dur) ** 2 * vel

def whoosh(dur=0.9, vel=0.35):
    n = int(dur * SR); t = np.arange(n) / SR; x = rng.standard_normal(n)
    env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 2
    lo = bp_fast(x, 200, 1500); hi = bp_fast(x, 1500, 6000)
    mixw = np.clip(t / dur, 0, 1)
    return (lo * (1 - mixw) + hi * mixw) * env * vel

def click(vel=0.12):
    n = int(0.03 * SR); t = np.arange(n) / SR
    return (hp_fast(rng.standard_normal(n), 2500) * np.exp(-t * 300) + np.sin(2 * np.pi * 1800 * t) * np.exp(-t * 400) * 0.5) * vel

def pop(f=880, vel=0.25):
    n = int(0.18 * SR); t = np.arange(n) / SR
    fr = f * (1 + 0.6 * np.exp(-t * 60))
    return np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t * 28) * vel

def ping(vel=0.3):  # notification deux tons
    out = np.zeros(int(0.9 * SR))
    for k, (f, d) in enumerate([(1318.5, 0), (1975.5, 0.11)]):
        n = int(0.7 * SR); t = np.arange(n) / SR
        s = (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * 2 * f * t)) * np.exp(-t * 7)
        i = int(d * SR); out[i:i + n] += s
    return out * vel

def chime(m, vel=0.25):
    n = int(1.6 * SR); t = np.arange(n) / SR; f = mtof(m)
    return (np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 3)) * np.exp(-t * 3.2) * vel

def scratch(dur=0.35, vel=0.18):
    n = int(dur * SR); t = np.arange(n) / SR
    am = 0.5 + 0.5 * np.sin(2 * np.pi * 22 * t)
    return bp_fast(rng.standard_normal(n), 1500, 5000) * am * np.sin(np.pi * t / dur) * vel

def crickets(dur, vel=0.012):
    n = int(dur * SR); t = np.arange(n) / SR; out = np.zeros(n)
    for f0, rate, ph in [(4300, 2.1, 0), (4700, 1.7, 1.3), (5200, 2.6, 2.1)]:
        chirp = (np.sin(2 * np.pi * 30 * t) > 0.3) * (np.sin(2 * np.pi * rate * t + ph) > 0.55)
        out += np.sin(2 * np.pi * f0 * t) * lp_fast(chirp.astype(float), 200)
    return out * vel * np.minimum(1, t / 1.0) * np.minimum(1, (dur - t) / 1.0)

# ---------- MUSIQUE ----------
music = buf()
BAR = 3.0  # 80 BPM, 4 temps
# Acte 1 (0–15.75) : la mineur, piano seul + nappe sombre
act1 = [(0.0, [45, 52, 57, 60]), (3.0, [45, 52, 57, 60]), (6.0, [41, 48, 53, 57]), (9.0, [38, 45, 50, 53]), (12.0, [40, 47, 52, 56])]
mel1 = [(0.0, 76), (1.5, 72), (3.0, 69), (4.5, 72), (6.0, 77), (7.5, 76), (9.0, 74), (10.5, 72), (12.0, 71), (13.5, 68)]
for t0, ch in act1:
    place(music, pad([m + 12 for m in ch[1:]], BAR + 1.0, vel=0.10, bright=900), t0, pan=0)
    place(music, piano(ch[0] - 12 + 12, 3.2, 0.22), t0, pan=-0.2)
for t0, m in mel1:
    place(music, piano(m, 2.8, 0.20), t0 + 0.02, pan=0.15)

# Actes 2 → 4 : do majeur, I–V–vi–IV
prog = [[48, 60, 64, 67], [43, 59, 62, 67], [45, 60, 64, 69], [41, 60, 65, 69]]
start = 15.75
nb = int((63.75 - start) / BAR)
for b in range(nb):
    t0 = start + b * BAR; ch = prog[b % 4]
    act = 2 if t0 < 33.75 else 3 if t0 < 51.75 else 4
    # basse
    place(music, piano(ch[0] - 12, 3.0, 0.28 if act > 2 else 0.20), t0, pan=0)
    # arpège de piano (croches)
    notes = [ch[1], ch[2], ch[3], ch[2] + 12, ch[3], ch[2], ch[1] + 12, ch[3]]
    for k, m in enumerate(notes):
        place(music, piano(m, 1.4, 0.13 if act == 2 else 0.11), t0 + k * 0.375, pan=-0.25 + 0.5 * (k % 2))
    # nappe
    place(music, pad(ch[1:], BAR + 0.8, vel=0.07 if act == 2 else 0.09 if act == 3 else 0.13,
                     bright=1400 if act < 4 else 2600), t0)
    # rythme
    for beat in range(4):
        tb = t0 + beat * 0.75
        if act == 2 and beat in (0, 2): place(music, kick(0.45), tb)
        if act >= 3: place(music, kick(0.55 if act == 3 else 0.7), tb)
        if act >= 3: place(music, hat(0.06 if act == 3 else 0.08), tb + 0.375, pan=0.3)
    # pluck « tech » en doubles croches (acte 3) / mélodie haute (acte 4)
    if act == 3:
        pat = [ch[1] + 12, ch[2] + 12, ch[3] + 12, ch[2] + 12]
        for k in range(16):
            place(music, pluck(pat[k % 4], 0.35, 0.10), t0 + k * 0.1875, pan=0.35 * (1 if k % 2 else -1))
    if act == 4:
        top = [ch[3] + 12, ch[2] + 12, ch[3] + 12, ch[1] + 24]
        for k, m in enumerate(top):
            place(music, piano(m, 2.0, 0.15), t0 + k * 0.75, pan=0.2)

# Signature finale (63.75) : accord plein + résolution, puis fondu
fin = [36, 48, 55, 60, 64, 67, 72, 76]
for m in fin: place(music, piano(m, 6.0, 0.16), 63.75, pan=(m - 60) / 40)
place(music, pad([60, 64, 67, 72], 9.0, vel=0.12, bright=2200), 63.75)
place(music, sub_boom(0.7), 63.75)
for k, m in enumerate([72, 76, 79, 84]):
    place(music, chime(m, 0.12), 66.0 + k * 0.4, pan=-0.3 + 0.2 * k)

music = reverb(music, 2.4, 0.28, seed=3)

# ---------- SONS (calés sur l'image) ----------
sfx = buf()
place(sfx, crickets(15.5), 0.0, 1.0, pan=0.0)        # nuit à Kaffrine
place(sfx, scratch(0.4), 6.55, 1.0, pan=-0.2)          # ratures
place(sfx, scratch(0.4), 7.55, 1.0, pan=-0.1)
place(sfx, sub_boom(0.28), 9.0)                         # chiffre 26,45 %
place(sfx, pop(520, 0.10), 9.05)
pass  # remplacé par un riser Pixabay                     # transition acte 1 → 2
pass  # remplacé par un riser Pixabay
for i in range(31):                                    # frappe au clavier (17 → 21,5 s)
    place(sfx, click(0.10 + 0.03 * rng.random()), 17.0 + i * 4.5 / 31 + rng.uniform(-0.02, 0.02), pan=0.35)
place(sfx, whoosh(0.35, 0.18), 21.5, pan=0.35)         # envoi du message
place(sfx, pop(1200, 0.12), 21.75, pan=0.35)
for k in range(3): place(sfx, click(0.04), 22.4 + k * 0.5, pan=0.35)   # « Jàng écrit… »
place(sfx, ping(0.22), 24.2, pan=0.35)                 # la correction arrive
for t0, f in [(27.2, 660), (28.2, 440), (29.4, 784), (30.6, 880)]:    # blocs ✅ ❌ 💡 ➡️
    place(sfx, pop(f, 0.12), t0, pan=-0.3)
pass  # remplacé par un riser Pixabay                    # transition acte 2 → 3
for t0 in (34.6, 35.4, 38.4, 45.0, 49.0):              # nœuds du schéma
    place(sfx, pop(700, 0.10), t0)
for t0 in (35.2, 38.2, 44.8, 48.8):                    # flèches
    place(sfx, whoosh(0.4, 0.07), t0)
place(sfx, whoosh(0.5, 0.12), 40.2, pan=-0.3)          # capture Dify
pass  # remplacé par un riser Pixabay                     # transition acte 3 → 4
pass  # remplacé par un riser Pixabay
place(sfx, chime(84, 0.16), 53.2, pan=0.2)             # coches vertes
place(sfx, chime(88, 0.16), 54.6, pan=0.2)
place(sfx, pop(600, 0.10), 52.6, pan=0.4)
place(sfx, pop(600, 0.08), 57.0, pan=0.4)
pass  # remplacé par un riser Pixabay
pass  # remplacé par un riser Pixabay
sfx = reverb(sfx, 1.2, 0.15, seed=5)

# ---------- MIXAGE ----------
t = np.arange(N) / SR
fade = np.minimum(1, t / 0.6) * np.minimum(1, (T - t) / 3.5)
music *= fade[:, None]; sfx *= fade[:, None]

def norm_rms(x, db):
    r = np.sqrt((x ** 2).mean()); return x * (10 ** (db / 20) / r)
music = norm_rms(music, -24)   # assez bas pour une voix off par-dessus
sfx = norm_rms(sfx, -30)
mix = music + sfx
peak = np.abs(mix).max()
if peak > 0.89: mix *= 0.89 / peak; music *= 0.89 / peak; sfx *= 0.89 / peak

def save(name, x):
    x = np.clip(x, -1, 1); d = (x * 32767).astype('<i2')
    w = wave.open(name, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(d.tobytes()); w.close()
save('sfx_ui.wav', sfx)
print('ok', round(20*np.log10(np.abs(mix).max()),1), 'dBFS crête')
