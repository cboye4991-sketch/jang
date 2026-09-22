# Value Proposition Canvas — Jàng

> Livrable S2 — GET 409 Atelier IA · Outil 2/3
> Construit avec P-VPC-1 (Profil Client) puis P-VPC-2 (Proposition de Valeur), à partir de la [carte d'empathie S1](../01-empathize/carte-empathie.md) et des [6 Chapeaux](chapeaux-bono.md).
> Chaque élément porte son origine : **(CE)** = carte d'empathie / verbatim S1 · **(Blanc, Rouge, Noir, Jaune, Vert, Bleu)** = chapeau de Bono · **[à valider]** = hypothèse non encore entendue en interview.
> Version visuelle : [`vpc.png`](vpc.png) · [`vpc.pdf`](vpc.pdf)

## HMW définitif

« Comment pourrions-nous permettre aux élèves de Terminale scientifique des lycées de région, qui révisent seuls faute de professeur, de recevoir le soir même une explication fiable de leurs erreurs sur les exercices d'annales — depuis le téléphone qu'ils ont déjà et sans dépasser leur petit forfait data — afin d'aborder le Bac en sachant se corriger seuls ? »

---

## 👤 Profil Client — Aminata Diallo

*17 ans · Terminale S2 · lycée public de Kaffrine · Android d'entrée de gamme · WhatsApp · forfait data acheté au jour le jour · aînée de 5 enfants, révise le soir après les tâches ménagères.*

### 🔧 Jobs To Be Done

| # | Type | Ce qu'Aminata essaie d'accomplir | Origine |
|---|---|---|---|
| J1 | Fonctionnel | Faire les exercices d'annales du Bac et **vérifier si ses réponses sont justes** | CE — « Je fais les exercices des annales, mais je ne sais pas si c'est juste. » |
| J2 | Fonctionnel | **Comprendre la méthode** pour pouvoir refaire seule un exercice du même type | CE — Gains : « comprendre sa méthode, pas seulement avoir la bonne réponse » |
| J3 | Fonctionnel | **Rattraper les chapitres jamais enseignés** en physique-chimie faute de professeur | CE — « Une salle de classe sans professeur de physique-chimie pendant des semaines » |
| J4 | Fonctionnel | **Réviser dans les créneaux qu'elle a** : le soir, après les tâches, avec le forfait du jour | CE — Dit & fait ; Blanc |
| J5 | Social | **Tenir la promesse faite à sa famille** et devenir la première à entrer à l'université (bourse) | CE — « Tu es notre espoir » ; aspiration secrète |
| J6 | Émotionnel | **Se sentir capable** et ne pas « sacrifier » une matière comme ses camarades | Rouge |

### 😣 Pains

| # | Frustration / obstacle / risque | Intensité | Origine |
|---|---|---|---|
| P1 | **Aucun retour sur ses erreurs** : personne pour lui dire où et pourquoi elle se trompe, elle ne progresse pas malgré ses efforts | ★★★ | CE — douleur principale ; Rouge |
| P2 | **Chapitres jamais vus** : pas de professeur de physique-chimie pendant des semaines | ★★★ | CE ; Blanc (déficit d'enseignants) |
| P3 | **Coût** : cours particuliers trop chers, vidéos YouTube trop gourmandes en data | ★★★ | CE — obstacle majeur ; Noir R2 |
| P4 | **Annales sans corrigé expliqué** ; elle recopie les solutions trouvées sans les comprendre | ★★ | CE — Ce qu'elle a fait ; Noir R3 |
| P5 | **Peu de temps et moment contraint** : révise tard, fatiguée, connexion instable le soir | ★★ | CE ; Noir R5 [à valider pour la connexion] |
| P6 | **Anxiété et sentiment d'injustice** face aux élèves de Dakar mieux accompagnés | ★★ | Rouge |
| P7 | **Peur d'apprendre faux** : un corrigé douteux trouvé sur un groupe peut l'induire en erreur | ★ | Noir R1 [à valider] |

### 🌟 Gains

| # | Résultat désiré | Niveau | Origine |
|---|---|---|---|
| G1 | **Savoir immédiatement si c'est juste — et pourquoi** | Indispensable | CE — citation directe |
| G2 | **Comprendre la méthode** et pouvoir refaire seule un exercice similaire | Indispensable | CE — Gains |
| G3 | **Voir qu'elle progresse** (chapitres maîtrisés, erreurs qui ne reviennent plus) | Attendu | Jaune |
| G4 | **Être accompagnée comme à Dakar** avec les moyens qu'elle a déjà (téléphone, WhatsApp) | Désiré | CE — besoin profond |
| G5 | **Arriver au Bac en confiance**, viser une mention et une bourse | Inattendu / aspiration | CE — aspiration secrète |

---

## 💡 Proposition de Valeur — Jàng

*Jàng (« apprendre » en wolof) est un correcteur d'exercices du Bac qui répond sur WhatsApp. L'élève envoie sa réponse à un exercice d'annale ; Jàng lui dit ce qui est juste, où est sa première erreur, pourquoi, et lui propose aussitôt un exercice similaire.*

### 📦 Produits & Services

| # | Fonctionnalité | Statut | Origine |
|---|---|---|---|
| S1 | **Correction guidée étape par étape** d'une réponse (texte ou photo compressée) : ✅ juste / ❌ première erreur / 💡 méthode / ➡️ à toi | MVP S3 | Vert |
| S2 | **Banque d'exercices d'annales du Bac sénégalais** classés par série, matière, chapitre, **avec corrigé de référence validé par un professeur** | MVP S3 | Vert ; Noir R1 |
| S3 | **Exercice de remédiation** similaire envoyé juste après une erreur | MVP S3 | Vert |
| S4 | **Exercice du soir** envoyé à l'heure choisie par l'élève | SHOULD | Vert ; Noir R5 |
| S5 | **Mode « pas vu en classe »** : rappel de cours en 5 lignes avant l'exercice | SHOULD | Vert |
| S6 | **Bilan du dimanche** : exercices faits, réussis, point à revoir | COULD | Vert ; Jaune |

### 💊 Pain Relievers

| Pain | → Pain Reliever | Service |
|---|---|---|
| P1 — Aucun retour sur ses erreurs | → Chaque réponse reçoit une correction qui **pointe la première erreur et explique pourquoi**, en moins de 2 minutes, à toute heure | S1 |
| P2 — Chapitres jamais vus | → Rappel de cours en 5 lignes, puis un exercice gradué du plus simple au type Bac | S5, S2 |
| P3 — Coût (cours, data) | → **Gratuit pour l'élève**, messages texte de 6 lignes maximum, **aucune vidéo**, photos compressées : une correction pèse l'équivalent de quelques messages WhatsApp | S1 |
| P4 — Annales sans corrigé / recopie | → Jàng **ne donne jamais la solution complète en premier** : il corrige *sa* réponse, puis lui fait refaire un exercice similaire | S1, S3 |
| P5 — Peu de temps, soirée | → Sessions de 10 minutes, un seul exercice à la fois, à l'heure qu'elle choisit ; la conversation reprend là où elle s'est arrêtée si le réseau coupe | S4 |
| P6 — Anxiété, injustice | → Un « répétiteur de poche » disponible le soir, qui encourage et montre les progrès | S1, S6 |
| P7 — Peur d'apprendre faux | → L'IA **compare** la réponse à un corrigé de référence validé au lieu d'inventer ; en cas de doute, elle le dit et signale l'exercice à un professeur bénévole | S2 |

### 🎁 Gain Creators

| Gain | → Gain Creator | Service |
|---|---|---|
| G1 — Savoir si c'est juste et pourquoi | → Verdict immédiat ✅/❌ + explication de l'erreur, en français simple | S1 |
| G2 — Comprendre la méthode | → Bloc 💡 « la bonne méthode » + exercice similaire à refaire seule : elle prouve qu'elle a compris | S1, S3 |
| G3 — Voir sa progression | → Bilan hebdomadaire : chapitres réussis, erreur la plus fréquente, prochain objectif | S6 |
| G4 — Être accompagnée comme à Dakar | → Accompagnement individuel sur l'appli qu'elle utilise déjà, sans rien installer | S1, S4 |
| G5 — Arriver au Bac en confiance | → Exercices tirés des vrais sujets du Bac sénégalais, corrigés selon les attentes des correcteurs | S2 |

---

## ✅ FIT Check

| Pain / Gain | Couvert par | FIT |
|---|---|---|
| P1 ★★★ | S1 | ✅ fort — c'est le cœur du MVP |
| P2 ★★★ | S5 + S2 | ⚠️ partiel en S3 (S5 est un SHOULD) |
| P3 ★★★ | S1 (format texte, gratuit) | ✅ fort — à mesurer (poids réel d'une correction) |
| P4 ★★ | S1 + S3 | ✅ |
| P5 ★★ | S4 + reprise de conversation | ⚠️ partiel en S3 |
| P6 ★★ | S1 + S6 | ✅ indirect |
| P7 ★ | S2 (corrigé de référence) | ✅ — condition de la confiance |
| G1, G2 | S1 + S3 | ✅ fort |
| G3 | S6 | ⏳ post-MVP |
| G4 | S1 + S4 | ✅ |
| G5 | S2 | ✅ |

**Pain Relievers sans Pain en face :** aucun — FIT validé.
**Fonctionnalités écartées car sans besoin réel :** vidéos explicatives (contredit P3), classement entre élèves (aucun verbatim ne le demande), application à installer (contredit G4 et P3).
**Conclusion :** le FIT est fort sur le problème principal (P1 → G1/G2) ; il reste deux points partiels (P2, P5) que le backlog S3 traite en SHOULD, et une condition de confiance (P7) qui fait des corrigés de référence un élément **non négociable** du MVP.

---

## 🚀 Notre plus-value — ce que Jàng apporte que rien d'autre n'apporte à Aminata

### Énoncé de proposition de valeur

> **Pour** les élèves de Terminale scientifique des régions qui révisent seuls faute de professeur,
> **qui** ne savent jamais si leurs exercices sont justes ni pourquoi,
> **Jàng** est un correcteur d'annales du Bac sur WhatsApp
> **qui** explique la première erreur de chaque réponse et fait aussitôt refaire un exercice similaire, le soir même et pour quelques messages de data,
> **contrairement aux** PDF d'annales sans corrigé, aux cours particuliers trop chers et aux vidéos trop lourdes,
> **parce que** chaque correction s'appuie sur un corrigé de référence validé par un professeur et suit le programme du Bac sénégalais.

### Comparaison avec ce qu'Aminata utilise déjà

| Critère | PDF d'annales (groupe WhatsApp) | Cours particulier | Vidéos YouTube | IA générique (chatbot) | **Jàng** |
|---|---|---|---|---|---|
| Dit si **sa** réponse est juste | ❌ | ✅ | ❌ | ✅ | ✅ |
| Explique **pourquoi** c'est faux | ❌ | ✅ | ⚠️ cas général | ✅ | ✅ |
| Fait refaire un exercice pour vérifier | ❌ | ⚠️ selon le prof | ❌ | ⚠️ si on le demande | ✅ automatique |
| Coût pour la famille | Gratuit | ❌ trop cher | Data élevée | Data moyenne, compte à créer | Gratuit, data minimale |
| Disponible le soir après les tâches | ✅ | ❌ | ✅ | ✅ | ✅ |
| Programme et attentes du **Bac sénégalais** | ✅ | ✅ | ⚠️ | ❌ souvent générique | ✅ |
| Fiabilité de la correction | ⚠️ inconnue | ✅ | ✅ | ⚠️ peut se tromper sans le dire | ✅ corrigé de référence validé |
| Empêche de recopier sans comprendre | ❌ | ✅ | ❌ | ❌ donne la solution | ✅ corrige d'abord, montre ensuite |

### Les 4 leviers de notre plus-value

1. **Le retour personnalisé, pas le contenu.** Les annales existent déjà ; ce qui manque, c'est un regard sur *la réponse d'Aminata*. Jàng vend un retour, pas un cours.
2. **La fiabilité comme promesse.** Une IA libre peut se tromper sans le dire. Jàng compare à un corrigé validé et avoue ses doutes — c'est ce qui rend la correction utilisable pour préparer un examen.
3. **Zéro friction, zéro coût caché.** Aucune application à installer, aucun compte à créer, aucune vidéo : Jàng vit dans WhatsApp, là où circulent déjà les annales, au format d'un message.
4. **La pédagogie de l'autonomie.** Jàng ne remplace pas l'effort d'Aminata : il corrige ce qu'elle a produit, puis lui fait refaire seule. Son objectif est qu'elle n'ait plus besoin de lui le jour du Bac.

### Hypothèses à valider en S3 avant d'affirmer cette plus-value

- **H1 :** Aminata fait confiance à une correction venant d'un robot si elle sait qu'elle s'appuie sur un corrigé validé par un professeur. *[à valider en interview]*
- **H2 :** une correction complète (réponse + retour + exercice similaire) coûte moins de 100 Ko de data. *[à mesurer sur le prototype]*
- **H3 :** après une correction, l'élève réussit l'exercice similaire au moins 6 fois sur 10. *[à mesurer au test]*
