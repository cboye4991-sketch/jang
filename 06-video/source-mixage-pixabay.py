"""Mixage du teaser Jàng avec les sons Pixabay (licence Pixabay) + sons d'interface synchronisés."""
import wave, numpy as np

SR = 44100; T = 73.0; N = int(SR * T)
PX = '/tmp/claude-0/px/jang-son-'

def load(name):
    w = wave.open(PX + name + '.wav'); x = np.frombuffer(w.readframes(w.getnframes()), '<i2').reshape(-1, 2) / 32768
    return x.astype(np.float64)

def seg(x, a, b): return x[int(a * SR):int(b * SR)].copy()

def loudness_match(x, db=-20.0):
    r = np.sqrt((x ** 2).mean()); return x * (10 ** (db / 20) / max(r, 1e-9))

def fades(x, fin=0.0, fout=0.0):
    n = len(x); t = np.arange(n) / SR; g = np.ones(n)
    if fin: g *= np.clip(t / fin, 0, 1)
    if fout: g *= np.clip((n / SR - t) / fout, 0, 1)
    return x * g[:, None]

def place(dst, sig, t0, gain_db=0.0):
    i = int(t0 * SR); n = min(len(sig), N - i)
    if n > 0: dst[i:i + n] += sig[:n] * 10 ** (gain_db / 20)

def loop_to(x, dur, xf=0.06):
    out = x.copy(); k = int(xf * SR)
    while len(out) < dur * SR:
        ramp = np.linspace(0, 1, k)[:, None]
        out[-k:] = out[-k:] * (1 - ramp) + x[:k] * ramp
        out = np.concatenate([out, x[k:]])
    return out[:int(dur * SR)]

music = np.zeros((N, 2))

# Acte 1 (0–16 s) : « Sad Background Music_29Sec » — prettyjohn1
a1 = loudness_match(seg(load('01-acte1-sad-background-music'), 0, 16.6), -21)
place(music, fades(a1, 0.8, 1.4), 0.0)

# Acte 2 (16–34 s) : « Kids Happy Background Music 21 Second » — BombinSound (ré majeur : même tonique que l'acte 1)
a2 = loudness_match(seg(load('04-kids-happy-21s'), 0, 18.9), -22)
place(music, fades(a2, 0.4, 1.2), 15.6)

# Acte 3 (34–52 s) : « Sport Epic Race - Loop » — Abydos_Music, bouclée
a3 = loudness_match(loop_to(load('06-sport-epic-race-loop'), 18.8), -23)
place(music, fades(a3, 0.5, 1.2), 33.8)

# Acte 4 (52–64 s) : « Event Music » — MFCC
a4 = loudness_match(seg(load('03-event-music'), 0, 13.2), -21)
place(music, fades(a4, 0.4, 1.4), 51.8)

# Carte finale (64–73 s) : fin naturelle de « Promo Music » — MFCC
a5 = loudness_match(seg(load('02-promo-music'), 5.0, 14.2), -23)
place(music, fades(a5, 0.8, 0.0), 63.8)

# Transitions : risers Pixabay (AberrantRealities), crête calée sur le changement de plan
r08 = load('08-intro-stinger-riser-08')
place(music, fades(seg(r08, 0, 5.5), 0, 2.0), 15.8 - 2.7, -7)          # acte 1 → 2
r07 = load('07-dramatic-reveal-riser-12')
place(music, fades(seg(r07, 0.8, 6.0), 0.3, 1.6), 33.9 - 2.4, -9)       # acte 2 → 3
place(music, fades(seg(r08, 0, 5.0), 0, 2.0), 51.8 - 2.7, -8)          # acte 3 → 4
r09 = load('09-epic-logo-reveal-riser-11')
place(music, fades(r09, 0, 1.5), 63.9 - 2.8, -5)                        # logo

# Sons d'interface synchronisés (frappe, notification, pops, carillons, grillons…)
w = wave.open('sfx_ui.wav'); ui = np.frombuffer(w.readframes(w.getnframes()), '<i2').reshape(-1, 2) / 32768
ui = ui[:N] * 0.7

t = np.arange(N) / SR
end = np.clip((T - t) / 2.5, 0, 1)[:, None]
music *= end; ui = ui * end

def save(name, x):
    x = np.clip(x, -1, 1); d = (x * 32767).astype('<i2')
    f = wave.open(name, 'wb'); f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes(d.tobytes()); f.close()

mix = music + ui
pk = np.abs(mix).max()
if pk > 0.89: mix *= 0.89 / pk; music *= 0.89 / pk; ui *= 0.89 / pk
save('px_musique.wav', music); save('px_sons.wav', ui); save('px_mix.wav', mix)
print('crête', round(20 * np.log10(np.abs(mix).max()), 1))
