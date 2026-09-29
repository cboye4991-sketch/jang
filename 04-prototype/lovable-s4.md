# S4 — MVP Jàng avec Lovable.dev

> GET 409 · Séance 4 (faite après S5) · Template « Lovable.dev — Du prompt à l'URL live » adapté à Jàng.
> Règle d'or : **1 prompt = 1 modification.** Si la génération échoue 2 fois → simplifier.

| Fiche d'identité | |
|---|---|
| Équipe | Cheikh BOYE · Adama DIOP |
| Projet | Jàng — correcteur d'exercices du Bac |
| Persona | Aminata Diallo · 17 ans · Terminale S2 · Kaffrine · Android d'entrée de gamme |
| Projet Lovable | « Jàng: Your Bac Coach » (lovable.dev, compte de Cheikh) |
| URL obtenue | `jang-bac-helper.lovable.app` — **dépubliée le 29/09** en attendant la version finale (voir journal) |

## Choix de conception

- **3 pages** comme demandé : Accueil · Exercices · Contact.
- **Les données sont celles de notre base RAG** (`dify/knowledge/jang_exercices_pc_ts2.csv`) : les ID JNG-PC-xx affichés sur le site sont ceux que le correcteur Dify reconnaît. Une carte « Maths — en préparation » montre honnêtement le périmètre (critère « Indisponible » du template).
- **Pas de statistiques inventées** : les 3 chiffres de l'accueil décrivent le projet (14 exercices, 14 fiches, objectif < 100 Ko), pas de faux résultats d'élèves.
- **Couleurs WhatsApp** (#128C7E / #25D366) : l'élève doit reconnaître un univers familier ; site léger, sans image lourde ni vidéo (contrainte data du HMW).
- **Itération fonctionnelle = la fenêtre de correction reliée à Dify** : le même MVP sert pour le L1 de S4 et le L1 de S5.

## Prompt d'initialisation (E1)

```
Crée une application web complète appelée Jàng.

# CONTEXTE
Jàng (« apprendre » en wolof) est un correcteur d'exercices du Bac sénégalais
pour les élèves de Terminale scientifique des lycées de région qui révisent seuls
faute de professeur. L'élève envoie sa réponse à un exercice d'annale ; Jàng lui dit
où est sa première erreur, pourquoi, et lui donne un exercice similaire —
depuis le téléphone qu'il a déjà, avec très peu de data.

# PAGES À CRÉER (3 pages)
1. ACCUEIL
   → Header : logo emoji 📘 + nom « Jàng »
   → Hero : titre « Tu révises seul ? Jàng te dit où tu t'es trompé. »
     sous-titre « Envoie ta réponse à un exercice du Bac, reçois ta première erreur
     expliquée et un exercice pour t'entraîner. Gratuit, sans application à installer. »
     2 boutons CTA : « Corriger un exercice » (vers Exercices)
     et « Je suis professeur bénévole » (vers Contact)
   → Section « Comment ça marche » en 3 étapes :
     1. Choisis un exercice et note son ID (ex. JNG-PC-01)
     2. Envoie l'ID et ta réponse
     3. Reçois ta première erreur, la méthode et un exercice similaire
   → Section chiffres : « 14 exercices type Bac » · « 14 fiches de cours » ·
     « < 100 Ko par correction »
   → Footer : « Projet étudiant GET 409 — Swiss UMEF University, Campus de Dakar ·
     Corrigés en cours de validation par des professeurs »
2. EXERCICES
   → Liste de 6 cartes avec : ID, matière, chapitre, énoncé court, statut
   → Boutons de filtre : Tous | Chimie | Physique | Maths
   → Chaque carte a une pastille « Corrigé disponible » (vert) ou
     « En préparation » (rouge), et un bouton « Copier l'ID »
3. CONTACT
   → Titre : « Professeur ? Aidez-nous à valider les corrigés »
   → Formulaire : Nom complet, E-mail, Téléphone, Message
   → Bouton d'envoi vert #128C7E
   → Adresse : Swiss UMEF University — Campus de Dakar, Sénégal

# DESIGN
→ Couleur principale : #128C7E (vert WhatsApp foncé)
→ Couleur secondaire : #FFFFFF (blanc)
→ Accent : #25D366 (vert WhatsApp clair)
→ Police : Inter (sans-serif moderne)
→ Style : moderne, épuré, rassurant, textes courts en français simple
→ Responsive mobile first (breakpoint 768px), lisible sur un écran de 360 px
→ Navigation fixe en haut avec les 3 pages
→ Aucune image lourde ni vidéo : nos utilisateurs ont très peu de data

# DONNÉES (6 exercices — ID | matière | chapitre | énoncé court | statut)
1. JNG-PC-01 | Chimie | Solutions et pH | 2,0 g de NaOH dans 500 mL : calcule C puis le pH | Corrigé disponible
2. JNG-PC-03 | Chimie | Acides faibles | pH d'une solution d'acide éthanoïque à 1,0×10⁻² mol/L (pKa = 4,8) | Corrigé disponible
3. JNG-MA-01 | Maths | Suites numériques | Étudier la convergence d'une suite récurrente | En préparation
4. JNG-PC-07 | Physique | Lois de Newton | Solide sur un plan incliné à 30° : accélération et vitesse après 2,0 m | Corrigé disponible
5. JNG-PC-10 | Physique | Dipôle RC | R = 10 kΩ, C = 100 µF : constante de temps et tension à t = τ | Corrigé disponible
6. JNG-PC-12 | Physique | Effet photoélectrique | Cellule au césium éclairée à 500 nm : énergie cinétique maximale | Corrigé disponible

# STACK TECHNIQUE
→ React + Tailwind CSS + Vite
```

## Prompts d'itération (L3 — au moins 3)

À envoyer **un par un**, après avoir testé le résultat du précédent.

| # | Type | Prompt | Pourquoi |
|---|---|---|---|
| P1 | Correction | *à écrire après la génération, selon ce qui est faux (texte, donnée, pastille)* | Corriger ce que Lovable a mal généré |
| P2 | Visuelle | « Sur la page Accueil, ajoute sous le hero une fine bannière vert clair #DCF8C6 avec 3 badges : 📶 Moins de 100 Ko par correction · 📱 Aucune application à installer · 🆓 Gratuit pour l'élève » | Rendre visible la promesse data/coût du VPC (P3) |
| P3 | Fonctionnelle | Fenêtre de correction reliée à Dify : voir ci-dessous | Feature principale — L1 de S5 |
| P4 | Libre | « Sur mobile (moins de 768px), transforme le menu en menu hamburger et vérifie que les cartes Exercices passent sur une seule colonne » | Test smartphone — 70 % des utilisateurs |

### P3 — Fenêtre de correction reliée au workflow Dify

```
Ajoute sur la page Exercices, au-dessus de la liste, une fenêtre « Corrige mon exercice »
qui imite une conversation WhatsApp avec Jàng :
- fond #ECE5DD, bulles vertes #DCF8C6 pour l'élève et blanches pour Jàng ;
- message d'accueil de Jàng : « Salut ! Envoie l'ID d'un exercice suivi de ta réponse.
  Exemple : JNG-PC-01 : C = 0,05/500 = 0,0001 mol/L » ;
- un champ de texte et un bouton vert « Envoyer à Jàng » ;
- un indicateur « Jàng écrit… » (3 points animés) pendant l'attente ;
- sur chaque carte, un clic sur « Copier l'ID » remplit aussi le champ avec « JNG-PC-xx : ».

La réponse vient d'un workflow Dify. N'appelle PAS l'API depuis le navigateur :
crée une fonction serveur (Lovable Cloud / edge function) « corriger » qui fait
POST https://api.dify.ai/v1/workflows/run
Header Authorization: Bearer <secret DIFY_API_KEY>, Content-Type: application/json
Body : { "inputs": { "query": <texte de l'élève> }, "response_mode": "blocking",
         "user": "jang-web-" + identifiant anonyme aléatoire }
Demande-moi la valeur du secret DIFY_API_KEY au lieu de l'écrire dans le code.

Traitement de la réponse :
- afficher data.outputs.text dans une bulle Jàng en gardant les retours à la ligne et les emojis ;
- si data.outputs.text est vide et data.outputs.message_erreur existe :
  afficher « Je ne peux pas corriger ce message. Envoie l'ID d'un exercice de la liste
  suivi de ta réponse. » ;
- erreur réseau : « Jàng est indisponible pour le moment — réessaie dans une minute » ;
- délai de 60 secondes maximum : « La réponse prend trop de temps — réessaie ».
```

> **Pourquoi une fonction serveur :** le dépôt GitHub doit être public (L2). Une clé API écrite dans le code du navigateur y serait visible par tous (note d'éthique, point 2). La clé Dify est à créer dans Dify → jang → Accès API → Clé API, et à coller **par l'équipe** quand Lovable la demande.
> **Pourquoi 60 s :** Gemini gratuit met 4 à 40 s selon la charge (voir `dify/tests-rag.md`).

## Checklist de test (template, étape 3)

- [ ] 📘 Jàng dans le header
- [ ] Navigation Accueil | Exercices | Contact
- [ ] Hero + 2 CTA
- [ ] 6 cartes + pastilles vert/rouge
- [ ] Filtres Tous / Chimie / Physique / Maths fonctionnels
- [ ] Formulaire Contact : 4 champs + bouton vert + adresse
- [ ] (P3) T1 envoyé depuis la fenêtre → correction affichée
- [ ] Testé sur smartphone réel

## Journal des itérations (L3)

> Prompts envoyés le 28–29/09/2026 depuis le compte Lovable de l'équipe. Texte exact des prompts : voir plus haut (E1, P3) et ci-dessous.

| # | Type | Prompt envoyé (résumé) | Résultat | Analyse |
|---|---|---|---|---|
| E1 | Initialisation | Prompt complet ci-dessus (contexte, 3 pages, design, 6 exercices, stack) | ✅ 3 pages générées du premier coup (« Thought for 54s ») : hero + 2 CTA, « Comment ça marche », chiffres, 6 cartes avec pastilles, filtres Tous/Chimie/Physique/Maths, formulaire Contact | Le template en 6 sections (contexte, pages, fonctionnalités, design, données, stack) a évité toute itération corrective de structure. Les données tirées de la base RAG rendent le site cohérent avec le correcteur. |
| P1 | Correction | « Sur la carte JNG-MA-01 (En préparation), remplace le bouton « Copier l'ID » par un bouton désactivé gris « Bientôt disponible ». Les autres cartes ne changent pas. » | ✅ | Défaut repéré au test : l'élève pouvait copier l'ID d'un exercice que Jàng ne sait pas corriger. « Les autres cartes ne changent pas » a protégé le reste. |
| P2 | Visuelle | « Sur la page Accueil, ajoute juste sous le hero une fine bannière vert clair #DCF8C6 avec 3 badges (empilés sur mobile) : 📶 Moins de 100 Ko par correction · 📱 Aucune application à installer · 🆓 Gratuit pour l'élève. Ne change rien d'autre. » | ✅ | Rend visible la promesse data/coût du VPC (Pain P3). |
| P3 | Fonctionnelle | Fenêtre « Corrige mon exercice » style WhatsApp reliée au workflow Dify via une fonction serveur, clé `DIFY_API_KEY` en secret (texte complet plus haut) | ✅ Lovable a créé une fonction serveur « corriger » (pas d'edge function possible sur ce type de projet), a demandé le secret (collé par l'équipe) et a corrigé seul les 3 points « Jàng écrit… » invisibles au 1er essai. **Test de bout en bout (29/09) : T1 envoyé depuis le site → correction Dify correcte** (volume en mL, exercice 0,80 g / 250 mL de la base). | Feature principale du MVP ; sert aussi de L1 pour S5. La clé reste côté serveur : le dépôt peut être public sans l'exposer. |
| P4 | Visuelle | « Rends le site plus illustré sans l'alourdir : illustration SVG dans le hero (élève + téléphone + bulles ❌/✅), icônes SVG pour les 3 étapes, bande de couleur et icône de matière sur chaque carte (Chimie violet, Physique bleu, Maths orange). Ne change ni les textes, ni le chat, ni les filtres. » | ✅ | Remarque de l'équipe : le site était « trop basique ». Les exemples du cours proposent photo-placeholders et animations ; on a choisi du **SVG dessiné en code** (quelques Ko) plutôt que des photos, pour rester fidèle à la contrainte data du HMW. Coût : ~4 crédits Lovable (le plus cher de la série, comme annoncé dans le document « Prompts Itérations »). |
| P5 | Fonctionnelle | Animations CSS légères : fade-in au défilement, compteurs animés (14, 14, 100), bulles du hero qui apparaissent et flottent, bulles du chat qui glissent, cartes qui se soulèvent au survol, respect de `prefers-reduced-motion` | ⏸️ **En pause — crédits Lovable gratuits épuisés** (5 par jour, rechargés à minuit UTC). À relancer avec « Finaliser ». | Les itérations visuelles consomment 3 à 5 fois plus qu'une correction : faire les corrections d'abord. |

### Publication (L1)

- 28/09 : le site a été publié **par erreur** sur `jang-bac-helper.lovable.app` (clic sur Publish pendant l'itération P2), puis **dépublié le 29/09 à la demande de l'équipe** en attendant la version finale.
- À faire : republier après P5 → noter l'URL dans e-Academy.

## Design v2 — « le cahier corrigé » (à appliquer quand les crédits reviennent)

Maquette de référence : [`maquette-jang-v2.html`](maquette-jang-v2.html) (aussi publiée comme page Claude pour la relecture).
Idée : le site ressemble à une page de **cahier à carreaux corrigée au stylo rouge**, où arrive la conversation WhatsApp avec Jàng. Le rouge est réservé aux corrections (comme sur une copie) ; le vert reste la couleur de la marque.

Deux prompts groupés pour tenir dans les 5 crédits du jour (les itérations visuelles coûtent cher). Envoyer le premier, vérifier l'aperçu, puis le second.

### D1 — Identité et hero

```
Refais l'identité visuelle du site sans toucher aux textes des pages Exercices et Contact, ni à la logique du chat :
- Fond de page : papier à carreaux discret (carreaux de 24px, lignes #DCE8E4 sur #F6F9F8), en CSS uniquement.
- Couleurs : vert marque #0E7565, encre #10231E, texte secondaire #52665F, rouge correction #D2382A
  (le rouge sert UNIQUEMENT aux annotations de correction), bulle élève #DCF8C6, fond de chat #ECE5DD.
  Couleurs de matière : Chimie #7C4DDB, Physique #0B84C6, Maths #C77700.
- Polices Google Fonts, 2 graisses maximum chacune : titres « Schibsted Grotesk » 800, texte « Atkinson Hyperlegible »
  400/700 (très lisible sur petit écran), identifiants et formules « IBM Plex Mono » 500, annotations manuscrites « Caveat » 600.
- Logo : « Jàng » en Schibsted Grotesk 800, suivi du mot « apprendre » en Caveat rouge (masqué sous 480px).
- Hero de l'Accueil : titre « Tu révises seul ? Jàng te montre où tu t'es trompé. » avec le mot « trompé. » souligné
  d'un trait de stylo rouge dessiné en SVG. Au-dessus, un petit sur-titre en IBM Plex Mono majuscules :
  « BAC · TERMINALE S2 · PHYSIQUE-CHIMIE ». Sous les boutons, la bannière des 3 promesses devient une ligne discrète
  en IBM Plex Mono : « ✓ moins de 100 Ko par correction ✓ rien à installer ✓ gratuit pour l'élève ».
- Remplace l'illustration de l'élève par un téléphone (cadre sombre arrondi) qui montre une conversation Jàng :
  bulle élève « JNG-PC-01 : n = 2/40 = 0,05 mol ; C = 0,05/500 = 0,0001 mol/L » où « 0,05/500 » est entouré au stylo rouge
  (ellipse SVG) avec l'annotation « en litres ! » en Caveat rouge ; puis la bulle Jàng avec 4 rubriques colorées
  (CE QUI EST JUSTE en vert, TA PREMIÈRE ERREUR en rouge, LA MÉTHODE en orange, À TOI en bleu).
  Au chargement, la scène se joue une fois : bulle élève, « Jàng écrit… », ellipse rouge qui se dessine, réponse.
  Un lien « Rejouer la démo » sous le téléphone. Tout reste visible au repos ; respecte prefers-reduced-motion.
Deux colonnes au-delà de 880px (texte à gauche, téléphone à droite), une seule colonne sur mobile.
```

### D2 — Sections, cartes et animations

```
Continue la refonte « cahier corrigé » :
1. Accueil : ajoute après le hero une section « Les annales, tu les as déjà. Ce qui manque, c'est la correction. »
   avec deux fiches côte à côte : « PDF d'annales du groupe WhatsApp » (✗ rouge : personne ne te dit si ta réponse
   est juste ; le corrigé donne tout sans expliquer ; tu recopies sans comprendre) et « Avec Jàng », bordure verte
   (✓ : ta réponse est comparée à un corrigé de référence ; seule ta première erreur est expliquée ; un exercice
   similaire pour vérifier).
2. « Comment ça marche » : 3 étapes numérotées en grands chiffres verts, séparées par des filets comme des lignes
   de cahier, avec les exemples « JNG-PC-07 » et « JNG-PC-07 : a = 8,5 m/s² » en IBM Plex Mono sur fond vert clair.
   Retire la section des 3 chiffres (déjà dite dans les promesses).
3. Cartes Exercices : fond blanc réglé comme une fiche (lignes horizontales discrètes), identifiant en IBM Plex Mono
   dans la couleur de la matière, chapitre en petites capitales colorées, pastille de statut arrondie ;
   elles se soulèvent légèrement au survol. Filtres en pastilles : l'actif en encre foncée.
4. Fenêtre « Corrige mon exercice » (page Exercices, au-dessus des filtres) : garde-la au même endroit et garde
   sa logique, change seulement son style : en-tête vert #0E7565 « Corrige mon exercice · Jàng en ligne »,
   fond #ECE5DD, zone de saisie en IBM Plex Mono sur fond papier, bouton vert « Envoyer à Jàng »,
   largeur maximale 720px. Dans les réponses de Jàng, colore les titres de rubrique (CE QUI EST JUSTE vert,
   TA PREMIÈRE ERREUR rouge #D2382A, LA MÉTHODE orange, À TOI bleu).
5. Encart professeurs sur fond encre #10231E : « Vu et corrigé » en Caveat rouge, titre « Professeur de PC ? Relisez
   nos corrigés. », bouton clair « Proposer mon aide » vers Contact.
6. Animations légères en CSS : apparition en fondu des sections au défilement (visibles par défaut si le JS
   ne tourne pas), bulles du chat qui glissent depuis le bas. Respecte prefers-reduced-motion.
Ne change pas la logique du chat ni la fonction serveur « corriger ».
```

## Captures (L4)

| Capture | Fichier |
|---|---|
| Mobile — Accueil avec illustration | [`05-test/captures/s4-mobile-accueil.jpg`](../05-test/captures/s4-mobile-accueil.jpg) |
| Mobile — Exercices (V1, avant P1) | [`05-test/captures/s4-mobile-exercices-v1.jpg`](../05-test/captures/s4-mobile-exercices-v1.jpg) |
| Mobile — Correction T1 dans la fenêtre Jàng | [`05-test/captures/s4-mobile-chat-T1.jpg`](../05-test/captures/s4-mobile-chat-T1.jpg) |
| Desktop | *à faire après la publication finale* |

## Note d'itération (½ page, L4)

La première génération était correcte mais très sobre : textes, cartes et boutons, sans illustration. Nous avons itéré dans l'ordre conseillé par le cours : d'abord une **correction** (P1, désactiver la copie de l'ID d'un exercice non couvert, pour ne pas envoyer l'élève vers une erreur), puis deux **ajouts visuels** (P2, bannière qui rend visibles nos trois promesses ; P4, illustrations), et une **fonctionnalité** (P3, la fenêtre de correction reliée à notre workflow Dify). P3 a transformé une vitrine en produit testable : l'élève tape « JNG-PC-01 : sa réponse » et reçoit en quelques secondes sa première erreur, la méthode et un exercice similaire. Pour les visuels, nous avons refusé les photos : notre persona, Aminata, a un forfait au jour le jour, donc toutes les images sont des SVG dessinés dans le code. Deux difficultés : Lovable ne permettait pas d'edge function et a proposé une fonction serveur équivalente, et le forfait gratuit (5 crédits par jour) a interrompu l'itération sur les animations. Leçon : une itération visuelle coûte bien plus qu'une correction, il faut les grouper et les faire en dernier.
