# Plan de tests RAG — Jàng_KB_v1

> S5 · Prompt S2 « Tester la base de connaissances » adapté à Jàng.
> Tests lancés le 28/09/2026 sur le brouillon du workflow « jang » (Gemini, clé gratuite). Captures d'écran à ajouter dans `05-test/captures/`.

## A. Test de récupération (Dify → Connaissances → Jang_KB_v1 → Test de récupération)

On teste la base **seule**, avant de la brancher sur l'agent.

Résultats du 28/09/2026 — recherche **sémantique**, Top K 3. Premier passage avec `text-embedding-3-small` (crédits Dify), repassé ensuite avec **`gemini-embedding-001`**, la configuration finale :

| # | Type | Requête | Chunk attendu | Résultat obtenu (score) | OK ? |
|---|---|---|---|---|---|
| R1 | Directe | `JNG-PC-01 NaOH concentration` | Ligne JNG-PC-01 | Gemini : JNG-PC-01 (0,75) · fiche bases fortes (0,75) · JNG-PC-04 (0,72) | ✅ |
| R2 | Directe | `satellite altitude 800 km vitesse` | Ligne JNG-PC-09 | Gemini : JNG-PC-09 (0,78) · fiche gravitation (0,69) · JNG-PC-08 (0,65) | ✅ |
| R3 | Indirecte | `je n'ai pas vu le condensateur` | Fiche « Dipôle RC » ou JNG-PC-10 | Gemini : fiche Dipôle RC (0,69) · JNG-PC-10 (0,69) · périmètre (0,65) | ✅ |
| R4 | Indirecte | `comment trouver le pH d'un acide faible` | Fiche « Acides faibles » ou JNG-PC-03 | Gemini : JNG-PC-03 (0,79) · fiche acides faibles (0,78) · JNG-PC-04 (0,77) | ✅ |
| R5 | Hors-base | `météo demain à Dakar` | Aucun chunk pertinent | Gemini : en-tête des fiches (0,59) · périmètre (0,55) · interférences (0,54) — rien de pertinent, scores nettement plus bas | ✅ |

Même série en mode **Économique** (mots-clés, sans crédit) : R2 `satellite altitude vitesse` → renvoie l'exercice du **proton** (JNG-PC-11) au lieu du satellite ; R1 → fiches sans rapport. **Conclusion : le mode Économique ne convient pas au français de notre base ; la recherche sémantique est nécessaire** (d'où la clé Gemini).

> Seuil de score : l'écart entre bons résultats (0,68–0,79) et hors-base (≤ 0,59) est faible avec Gemini. Le seuil est laissé désactivé ; c'est le Chercheur qui refuse le hors-programme (INSUFFISANT).


## B. Tests de bout en bout (workflow → Exécuter, ou script `webhook/test-api.sh`)

| # | Message de l'élève (`query`) | Comportement attendu | Résultat obtenu |
|---|---|---|---|
| T1 | `JNG-PC-01 : n = 2/40 = 0,05 mol ; C = 0,05/500 = 0,0001 mol/L` | `text` : ✅ n juste · ❌ volume laissé en mL · 💡 convertir en L · ➡️ exercice 0,80 g / 250 mL · source JNG-PC-01 | ✅ Volume en mL repéré, méthode sans le résultat, exercice 0,80 g / 250 mL de la base (flash-lite, 38 s) |
| T2 | `JNG-PC-07 : a = g cos 30 = 8,5 m/s²` | ❌ projection avec cos au lieu de sin · ne donne pas v = 4,4 m/s | ✅ cos au lieu de sin repéré, exercice similaire α = 20° de la base (36 s) |
| T3 | `JNG-PC-13 : 24 jours = 3 périodes donc A = 8,0×10^6 / 3 = 2,7×10^6 Bq` | ✅ 3 périodes · ❌ diviser par 2³ = 8 | ✅ « divisé par 3 au lieu de 2^3 », exercice carbone 14 de la base (70 s, avec nouvelles tentatives) |
| T4 | `JNG-PC-02 : pH = 2 puis pH = 3 après dilution` | ✅ tout juste · félicitations · ➡️ exercice HNO₃ | ✅ « Aucune erreur, bravo 👏 », exercice HNO₃ de la base (117 s) |
| T5 | `Je n'ai jamais vu l'effet photoélectrique en classe` | Probablement `message_erreur` (pas de réponse d'élève à corriger) — à observer et noter | ⚠️→✅ 1er essai : « Aucune erreur, bravo » hors sujet, puis INSUFFISANT. Deux règles ajoutées (Chercheur + Rédacteur) → « 📚 LE COURS EN BREF » sur le dipôle RC + exercice de la base (31 s) |
| T6 | `Quelle est la météo demain à Dakar ?` | `message_erreur` : « INSUFFISANT : … ne relève pas du programme de Terminale S » | ✅ `message_erreur` : « INSUFFISANT : … ne concerne pas le programme de PC ou de Maths de Terminale S » |
| T7 | `Corrige mon exercice de SVT sur la génétique` | `message_erreur` (matière non couverte) | ✅ `message_erreur` : « INSUFFISANT : la question concerne les SVT… » (17 s) |
| T8 | Exercice hors base : `Une voiture de masse 1000 kg passe de 0 à 20 m/s en 10 s… Ma réponse : F = m·v = 20 000 N` | Correction avec SOURCES « hors base Jàng — résolution non vérifiée par un professeur » | ❌→✅ En v2, refusé à tort (« niveau collège/seconde »). **Corrigé en v3 par la base fixe programme** (30/09) : a = Δv/Δt = 2,0 m/s², F = m·a = 2 000 N, erreur m·v (quantité de mouvement) repérée (15 s) |
| T9 | Hors base, constante absente de l'énoncé : `Un photon a une longueur d'onde de 500 nm… Ma réponse : E = h·λ = 3,3×10⁻⁴⁰ J` | Le Chercheur prend c dans la base fixe | ✅ (v3) E = h·c/λ = 3,97×10⁻¹⁹ J avec c = 3,0×10⁸ m/s de la base fixe ; erreur h·λ repérée (7 s) |

## B bis. RAG à deux recherches — base fixe programme (30/09/2026, version « S5 RAG v3 »)

Appliqué d'après le tutoriel *GET 409 — S5 — Tutoriel Dify RAG à deux recherches*, pour corriger T8.

- **Base fixe `Jang_Programme_v1`** : [`knowledge/jang_programme_constantes_ts2.md`](knowledge/jang_programme_constantes_ts2.md), une seule ligne de 850 caractères (chapitres du programme PC TS2 et constantes). Séparateur `\n\n`, longueur 1000 : **1 morceau**. Un premier jet de 1 122 caractères était coupé en 2 morceaux et a été raccourci.
- **Variable ENV** `requete_programme` = « programme Terminale S2 chapitres constantes » (requête fixe).
- **RECUP_PROGRAMME** (requête = ENV, Top K 3) → **MODÈLE (base fixe)** (`{% for item in donnees %}{{ item.content }}{% endfor %}`) → bloc « BLOC PROGRAMME » dans le prompt du Chercheur.
- Trace vérifiée sur T8 : RECUP_PROGRAMME renvoie le morceau, MODÈLE sort le texte brut, le Chercheur classe l'exercice en « Lois de Newton » et ne refuse plus.

Non-régression v3 (30/09) : T1 ✅ (volume en mL, 8 s) · T6 ✅ `message_erreur` météo · T7 ✅ `message_erreur` SVT · T8 ✅ · T9 ✅. La règle « jamais hors niveau » ne fait pas accepter les autres matières.

## B ter. Réponse illisible et ID non retrouvé (30/09/2026, version « S5 RAG v4 »)

**Problème vu sur le site :** `JNG-PC-01 : grtefcxcv` → refus avec une **fausse raison** (« JNG-PC-01 ne figure pas dans la base »). Trace : la recherche sémantique, égarée par le mot sans sens, renvoyait les fiches satellites / photon / alcools, jamais JNG-PC-01.

| Essai | Résultat |
|---|---|
| Recherche **hybride** (sémantique 0,6 + mots-clés 0,4) | ❌ JNG-PC-01 toujours absent ; « condensateur » moins bien classé (périmètre avant Dipôle RC). Annulé, retour au sémantique. |
| **Nœud Code EXTRAIRE_ID** (regex `JNG-PC-xx` → requête = énoncé de référence de l'exercice) | ✅ JNG-PC-01 (CSV + fiche) en tête de la récupération |

| # | Message | Attendu | Résultat v4 |
|---|---|---|---|
| T10 | `JNG-PC-01 : grtefcxcv` | Refus avec la bonne raison | ✅ « INSUFFISANT : ta réponse à JNG-PC-01 est illisible. Envoie ton calcul ou ton résultat, par exemple : JNG-PC-01 : C = … mol/L et pH = … » (5 s) |
| T11 | `C'est ce que j'ai fais` (message de suite) | Refus : Jàng ne garde pas l'historique | ✅ « INSUFFISANT : l'énoncé de l'exercice et la réponse n'ont pas été fournis. » — limite connue : chaque message est traité seul |

Non-régression v4 : T1 ✅ · T2 ✅ (cos/sin) · T6 ✅ · T7 ✅. **T8 a d'abord re-échoué** (« cinématique élémentaire hors programme ») : la condition « relève du programme » de l'étape 3 l'emportait sur la règle du bloc. Condition réécrite (« d'un chapitre listé dans le BLOC PROGRAMME ») → T8 ✅ deux fois de suite.

## C. Critères de réussite (rappel HMW / VPC)

- **Fiabilité :** sur T1–T4, l'erreur pointée est celle du corrigé de référence (0 erreur inventée).
- **Pédagogie :** la solution complète n'est jamais donnée d'emblée (T1–T3).
- **Limites :** T6 et T7 sortent par `message_erreur`, sans invention.
- **Data :** chaque correction fait 90 mots maximum (hypothèse H2 : une correction < 100 Ko).

## D. Réglages à tester si ça ne marche pas

| Symptôme | Réglage |
|---|---|
| Mauvais exercice retrouvé | Top K 3 → 5 ; exiger l'ID JNG-PC-xx dans la question |
| Aucun chunk en mode Haute qualité | Seuil désactivé ou 0,4 |
| Le Chercheur ignore la base | Vérifier `{{#context#}}` dans son prompt et CONTEXTE = `Récupération Jang_KB_v1 · result` |
| « quota exceeded » | Crédits épuisés → clé API dans Intégrations → Fournisseur de modèles |

## E. Constats Gemini gratuit (28/09/2026)

- `gemini-2.5-flash` : refusé aux nouvelles clés.
- `gemini-3.5-flash` : bonne qualité, mais **quota gratuit de 20 requêtes**, vite épuisé (chaque test = 2 requêtes, plus les nouvelles tentatives).
- `gemini-3.5-flash-lite` (**retenu**) : quota séparé, qualité suffisante avec le RAG, ~30 s par test ; saturations ponctuelles (« high demand ») → 1 nouvelle tentative automatique par agent.
- **Pour la démo S6 :** ne pas lancer de tests juste avant ; garder le Plan B prêt ; envisager le plan Pro de Dify via « Faire vérifier l'éducation ».
