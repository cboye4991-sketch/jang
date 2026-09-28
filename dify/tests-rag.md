# Plan de tests RAG — Jàng_KB_v1

> S5 · Prompt S2 « Tester la base de connaissances » adapté à Jàng.
> Colonne **Résultat obtenu** à remplir pendant les tests, avec une capture d'écran par test.

## A. Test de récupération (Dify → Connaissances → Jang_KB_v1 → Test de récupération)

On teste la base **seule**, avant de la brancher sur l'agent.

| # | Type | Requête | Chunk attendu | Score attendu | Résultat obtenu |
|---|---|---|---|---|---|
| R1 | Directe | `JNG-PC-01 NaOH concentration` | Ligne JNG-PC-01 (NaOH, 0,10 mol/L) | Élevé | |
| R2 | Directe | `satellite altitude 800 km vitesse` | Ligne JNG-PC-09 | Élevé | |
| R3 | Indirecte | `je n'ai pas vu le condensateur` | Fiche « Dipôle RC » ou ligne JNG-PC-10 | Moyen | |
| R4 | Indirecte | `comment trouver le pH d'un acide faible` | Fiche « Acides faibles » ou JNG-PC-03 | Moyen | |
| R5 | Hors-base | `météo demain à Dakar` | Aucun chunk pertinent | Faible / vide | |

> Mode **Économique** (index inversé) : la recherche fonctionne par mots-clés. Si R3/R4 ne remontent rien, reprendre les mots exacts de la fiche (« Dipôle RC », « acide faible ») — c'est la limite connue de ce mode, à noter dans le journal.

## B. Tests de bout en bout (workflow → Exécuter, ou script `webhook/test-api.sh`)

| # | Message de l'élève (`query`) | Comportement attendu | Résultat obtenu |
|---|---|---|---|
| T1 | `JNG-PC-01 : n = 2/40 = 0,05 mol ; C = 0,05/500 = 0,0001 mol/L` | ✅ n juste · ❌ volume laissé en mL · 💡 convertir en L · ➡️ exercice 0,80 g / 250 mL | |
| T2 | `JNG-PC-07 : a = g cos 30 = 8,5 m/s²` | ❌ projection avec cos au lieu de sin · ne donne pas v = 4,4 m/s | |
| T3 | `JNG-PC-13 : 24 jours = 3 périodes donc A = 8,0×10^6 / 3 = 2,7×10^6 Bq` | ✅ 3 périodes · ❌ diviser par 2³ = 8 | |
| T4 | `JNG-PC-02 : pH = 2 puis pH = 3 après dilution` | ✅ tout juste · félicitations · ➡️ exercice HNO₃ | |
| T5 | `Je n'ai jamais vu l'effet photoélectrique en classe` | Fiche en 5 lignes + propose JNG-PC-12 | |
| T6 | `Quelle est la météo demain à Dakar ?` | « Je ne dispose pas de cette information dans ma base… » | |
| T7 | `Corrige mon exercice de SVT sur la génétique` | Même message hors-base (matière non couverte) | |

## C. Critères de réussite (rappel HMW / VPC)

- **Fiabilité :** sur T1–T4, l'erreur pointée est celle du corrigé de référence (0 erreur inventée).
- **Pédagogie :** la solution complète n'est jamais donnée d'emblée (T1–T3).
- **Limites :** T6 et T7 déclenchent le message hors-base, sans invention.
- **Data :** chaque réponse fait 6 lignes maximum (hypothèse H2 : une correction < 100 Ko).

## D. Réglages à tester si ça ne marche pas

| Symptôme | Réglage |
|---|---|
| Mauvais exercice retrouvé | Top K 3 → 5 ; exiger l'ID JNG-PC-xx dans la question |
| Aucun chunk en mode Haute qualité | Seuil 0,5 → 0,3 |
| Le CORRECTEUR invente un corrigé | Vérifier que le CHERCHEUR a bien `{{#context#}}` et que son CONTEXTE est relié à la récupération |
| Réponse trop longue | Rappeler « 6 lignes maximum » dans le USER du CORRECTEUR |
