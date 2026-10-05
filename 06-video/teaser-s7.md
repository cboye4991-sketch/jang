# Jàng — Vidéo teaser (S7)

> **GET 409 · Séance 7.** Livrable **L2 : vidéo MP4, 60 à 90 s, 16:9, 1080p, sous-titres obligatoires** (30 pts). Livrable **L3 : script vidéo** → [`jang-script-teaser.pptx`](jang-script-teaser.pptx) (template du cours rempli).
> Chaîne : **Script (Claude) → prompts visuels (Claude) → clips (Kling AI) → montage (CapCut) → export MP4 → Drive + e-Academy.**

## 1. Script — 4 actes × 15 s (≈ 140 mots de voix off, débit calme)

| Acte | Visuel | Voix off (texte exact) | Ton |
|---|---|---|---|
| **1 · Le problème** (0–15 s) | Nuit à Kaffrine. Une élève de Terminale S révise seule à la lumière de son téléphone, cahier de physique couvert de ratures. | « Kaffrine, 23 h. Aminata révise seule. Personne pour lui dire où elle s'est trompée. Au Bac 2026, à peine un candidat sur quatre a été admis dès le premier tour. » | urgence / émotion |
| **2 · La solution** (15–30 s) | **Enregistrement réel** du site Jàng sur téléphone : choix de JNG-PC-01, réponse tapée comme un message WhatsApp. | « Voici Jàng. Aminata choisit un exercice type Bac et envoie sa réponse, comme un message WhatsApp. Quelques secondes plus tard, Jàng lui montre sa première erreur. Pas la solution : l'erreur. » | espoir / clarté |
| **3 · L'agent IA** (30–45 s) | La correction s'affiche bloc par bloc (✅ ❌ 💡 ➡️) ; en surimpression : 2 agents IA + base de corrigés (schéma d'architecture V2 animé). | « Derrière, deux agents IA. Le premier retrouve le corrigé de référence dans notre base d'exercices, au lieu de l'inventer. Le second rédige une correction de moins de 90 mots, avec un exercice pour s'entraîner. » | innovation / précision / confiance |
| **4 · Impact + CTA** (45–60 s) | Aminata réussit l'exercice similaire et sourit. À l'écran : « 1 correction < 100 Ko », puis logo Jàng, URL du site et QR code. | « Une correction pèse moins qu'une photo WhatsApp. Notre objectif : un correcteur dans la poche de chaque élève de Terminale S en région. Jàng, en wolof : apprendre. Essaie-le sur notre site. » | conviction / appel à l'action |

**Source du chiffre (acte 1) :** Office du Bac, résultats provisoires du 1er tour du Bac général 2026 : **26,45 %** d'admis d'office (45 614 admis) — [Le Soleil](https://lesoleil.sn/actualites/education/bac-2026-plus-de-12-000-mentions-un-taux-provisoire-de-2645-au-premier-tour/), [APA News](https://fr.apanews.net/education/senegal-2645-de-reussite-au-1er-tour-du-baccalaureat-general-2026/). Afficher la source en petit à l'écran pendant l'acte 1.

**Choix assumés :**
- Pas de chiffre d'impact inventé (le template propose « Nous visons X utilisateurs ») : nous n'avons pas encore testé avec des élèves, donc l'acte 4 montre une **promesse vérifiable** (légèreté en data, hypothèse H2) plutôt qu'une projection.
- Les actes 2 et 3 utilisent **notre vrai MVP**, pas une interface générée par IA : Kling ne sait pas reproduire notre écran, et une fausse interface tromperait le jury.
- Aminata est notre **persona** (fictive) : ne pas filmer une vraie élève sans accord écrit de ses parents.

## 2. Prompts Kling AI (en anglais, 5 s, 16:9) — 2 variantes pour les plans générés

Formule du cours : **lieu + lumière · sujet + action · style · durée/format.**

| Plan | Prompt Kling |
|---|---|
| **A1-a** (0–5 s) | `Small bedroom in a rural town in Senegal at night, single warm desk lamp and phone light, a Black teenage girl in a simple school uniform studies alone, frowning at a physics notebook full of crossed-out calculations, slow push-in, cinematic, shallow depth of field, 16:9, 5 seconds` |
| **A1-b** (5–10 s) | `Extreme close-up of a handwritten physics exercise on squared paper, formula C = n / V crossed out several times, pen tapping nervously, dim warm light, cinematic realism, 16:9, 5 seconds` |
| **A1-c** (10–15 s) | `Exterior of a modest house in Kaffrine, Senegal, at night, one lit window, quiet street, sand and a baobab silhouette, starry sky, slow wide establishing shot, cinematic, 16:9, 5 seconds` |
| A2, A3 | **Pas de Kling** : enregistrement d'écran du site Jàng (téléphone ou mode mobile du navigateur) + schéma `docs/architecture-v2.png` avec zoom lent (Ken Burns) dans CapCut. |
| **A4-a** (45–52 s) | `Same Senegalese teenage girl at her desk the next morning, soft sunrise light, she solves an exercise and smiles with relief, looking at her phone, hopeful, cinematic, 16:9, 5 seconds` |
| **A4-b** (52–60 s) | `Group of Senegalese high school students in a sunny schoolyard comparing answers on their phones, laughing, warm golden light, documentary style, 16:9, 5 seconds` |

Bonnes pratiques : générer 2 à 3 variantes par plan, garder la même description de l'élève d'un plan à l'autre (cohérence du personnage), refuser tout rendu avec du texte illisible ou un logo.

**Plan B si Kling est lent** : photos libres de droits (Unsplash / Pexels, recherche « student studying night Africa », « Senegal school ») + zoom lent dans CapCut.

## 3. Variante Google Flow / Veo 3.1 (fichiers « Input Template » et « Master Prompt »)

À coller dans Storyboard Studio de Google Flow, puis passer le scénario obtenu dans le *Master Prompt* (8 s par plan) :

```
CHARACTER: Aminata, 17, Senegalese high-school student in Terminale S, braided hair, simple school uniform, determined
SETTING: a small bedroom in Kaffrine, Senegal, late at night then early morning, tense then hopeful atmosphere
STORY ARC: she is stuck alone on a physics exercise → she sends her answer to Jàng and sees her first mistake → she solves the similar exercise at sunrise and smiles
CAMERA DIRECTIONS:
Scene 1 - Wide shot - the dark room, only the desk lamp is on, she studies alone
Scene 2 - Medium shot - she sighs and looks at her crossed-out notebook
Scene 3 - Close-up - she types her answer on her phone
Scene 4 - Low angle - she reads the correction, her face lights up
Scene 5 - Bird's eye - notebook, phone and pen on the desk, she writes the right formula
Scene 6 - Dutch tilt - morning light, she closes the notebook and smiles
DIALOGUE BEATS:
Scene 2: "Personne pour me dire où je me trompe…"
Scene 3: "Allez, j'envoie à Jàng."
Scene 5: "Ah… il fallait convertir en litres !"
Scene 6: "Jàng, en wolof : apprendre."
```

⚠️ Même règle qu'avec Kling : l'écran du téléphone doit être remplacé au montage par une vraie capture du site Jàng.

## 4. Montage CapCut (≈ 60 s)

| Piste | 0–15 s | 15–30 s | 30–45 s | 45–60 s |
|---|---|---|---|---|
| Vidéo | A1-a · A1-b · A1-c | écran du site (choix JNG-PC-01, saisie) | correction qui s'affiche + schéma d'architecture | A4-a · A4-b · carte finale (logo, URL, QR) |
| Texte à l'écran | « Bac 2026 : 26,45 % d'admis au 1er tour » + source | « JNG-PC-01 : C = 0,05/500 » | « 2 agents IA · corrigés vérifiés (RAG) » | « 1 correction < 100 Ko » · URL du site |
| Voix off | acte 1 | acte 2 | acte 3 | acte 4 |
| Musique | libre de droits CapCut, **20–30 %** du volume, montée douce à l'acte 4 | | | |

Sous-titres : **Sous-titres automatiques** de CapCut, puis correction manuelle de ces mots, souvent mal reconnus :

| Écrit par l'IA de CapCut | Correction |
|---|---|
| Jang / Jean / Djang | **Jàng** |
| Cafrine / Kafrine | **Kaffrine** |
| terminal S | **Terminale S** |
| rag / rague | **RAG** |
| github point io | **github.io** |
| Aminatta | **Aminata** |

## 5. Checklist avant dépôt

- [ ] MP4, 1080p, 16:9 horizontal
- [ ] Durée **entre 60 et 90 s** (pénalité au-delà de 90 s)
- [ ] Sous-titres présents et relus (tableau ci-dessus)
- [ ] Voix off audible, calée sur les 4 actes ; musique à 20–30 %
- [ ] Source du chiffre affichée à l'acte 1
- [ ] URL du site à l'acte 4 : **cboye4991-sketch.github.io/jang-bac-helper** (+ QR code)
- [ ] Upload Google Drive → lien « Tous les utilisateurs disposant du lien » → dépôt e-Academy (L2)

## 6. Version montée (05/10/2026)

- [`jang-teaser.mp4`](jang-teaser.mp4) : 73 s, 1920×1080, 25 i/s, H.264 + AAC, sous-titres incrustés, bande-son mixée avec des sons Pixabay (voir « Crédits son »), volume normalisé à −16 LUFS.
- [`jang-teaser.srt`](jang-teaser.srt) : les 13 sous-titres minutés. Ils servent aussi de texte pour enregistrer la voix off dans CapCut.
- Les actes 2 et 3 montrent **le vrai MVP** et une **capture réelle de Dify** ; la correction affichée est une vraie réponse du workflow (JNG-PC-01, 05/10). Les actes 1 et 4 sont des illustrations (aucune image générée de personne réelle) ; Aminata est présentée comme persona fictive.
- Source des scènes : [`source-video.html`](source-video.html), rendu image par image, puis assemblé avec ffmpeg.

### Bande-son (05/10) — composée pour le teaser, libre de droits

Construite selon les usages des teasers d'app « problème → solution » : changement d'humeur au moment de la solution, transitions marquées (riser + whoosh), sons d'interface synchronisés avec l'écran, signature sonore sur le logo, musique assez basse pour une voix off.

| Moment | Musique | Sons calés sur l'image |
|---|---|---|
| Acte 1 · nuit (0–16 s) | piano seul en *la mineur*, nappe sombre | grillons de Kaffrine, ratures au stylo, impact sourd sur « 26,45 % », riser → whoosh |
| Acte 2 · l'app (16–34 s) | passage en *do majeur* (I–V–vi–IV), arpège de piano, battement léger | frappe au clavier, envoi du message, « Jàng écrit… », notification quand la correction arrive, « pop » sur ✅ ❌ 💡 ➡️ |
| Acte 3 · l'IA (34–52 s) | rythme plus « tech » : pluck en doubles croches, kick régulier | pop sur chaque bloc du schéma, souffle sur les flèches, riser |
| Acte 4 + fin (52–73 s) | version pleine (nappe lumineuse, mélodie haute) puis accord final + carillon | carillons sur les coches vertes, whoosh vers la carte finale |

Version finale : la musique synthétique a été remplacée par des sons **Pixabay**, un par scène (ci-dessous) ; les sons d'interface synchronisés sont gardés ([`source-sons-interface.py`](source-sons-interface.py)). Mixage : [`source-mixage-pixabay.py`](source-mixage-pixabay.py).

### Crédits son — Pixabay (licence de contenu Pixabay, utilisation gratuite)

| Scène | Son | Auteur |
|---|---|---|
| Acte 1 · nuit | Sad Background Music_29Sec | prettyjohn1 |
| Acte 2 · l'app | Kids Happy Background Music 21 Second | BombinSound |
| Acte 3 · l'IA | Sport Epic Race - Loop | Abydos_Music |
| Acte 4 · le matin | Event - Event Music | MFCC |
| Carte finale | Promo - Promo Music | MFCC |
| Transitions | Dramatic Intro Stinger Riser #08 · Dramatic Reveal Riser #12 | AberrantRealities |
| Logo | Epic Logo Reveal Riser #11 | AberrantRealities |

Les fichiers audio Pixabay ne sont pas déposés ici (la licence interdit de les redistribuer seuls) ; ils sont dans `Downloads/class02/sons-pixabay` sur le Mac de Cheikh.


### Version finale (05/10, 15 h) — voix off + une seule musique

- **Voix off** : synthèse vocale neuronale française **Piper**, voix *siwis* (fr_FR, qualité medium, licence **CC-BY 4.0**), générée localement, phrase par phrase, calée sur les sous-titres. Texte : [`source-texte-voix-off.py`](source-texte-voix-off.py) (« Jàng » écrit « Djang » et « WhatsApp » écrit « Ouatsap » pour la prononciation).
- **Musique** : un seul morceau du début à la fin, sans coupe — « Lofi Study - Calm Peaceful Chill Hop » de **FASSounds** (Pixabay), 75 BPM, rythmé mais doux. Il démarre dans son pont au piano (nuit, acte 1) pour que le beat revienne pile sur « Voici Jàng » (15,8 s) ; sa fin naturelle tombe sur la carte finale.
- **Mixage** : la musique baisse de 9 dB quand la voix parle (voix ≈ 10 dB au-dessus du fond), sons d'interface très légers, −16 LUFS. Script : [`source-mixage-voix-off.py`](source-mixage-voix-off.py).

Crédits à citer : voix « siwis » (Piper, CC-BY 4.0, corpus SIWIS) · musique « Lofi Study » — FASSounds / Pixabay.
