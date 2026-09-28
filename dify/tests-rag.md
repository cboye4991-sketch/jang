# Plan de tests RAG — Jàng_KB_v1

> S5 · Prompt S2 « Tester la base de connaissances » adapté à Jàng.
> Colonne **Résultat obtenu** à remplir pendant les tests, avec une capture d'écran par test.

## A. Test de récupération (Dify → Connaissances → Jang_KB_v1 → Test de récupération)

On teste la base **seule**, avant de la brancher sur l'agent.

Résultats du 28/09/2026 — recherche **sémantique** (embedding `text-embedding-3-small`, Top K 3) :

| # | Type | Requête | Chunk attendu | Résultat obtenu (score) | OK ? |
|---|---|---|---|---|---|
| R1 | Directe | `JNG-PC-01 NaOH concentration` | Ligne JNG-PC-01 | JNG-PC-01 (0,58) · fiche bases fortes (0,55) · JNG-PC-04 (0,50) | ✅ |
| R2 | Directe | `satellite altitude 800 km vitesse` | Ligne JNG-PC-09 | JNG-PC-09 (0,56) · fiche gravitation (0,41) · JNG-PC-07 (0,33) | ✅ |
| R3 | Indirecte | `je n'ai pas vu le condensateur` | Fiche « Dipôle RC » ou JNG-PC-10 | JNG-PC-10 (0,45) · fiche Dipôle RC (0,42) · JNG-PC-12 (0,30) | ✅ |
| R4 | Indirecte | `comment trouver le pH d'un acide faible` | Fiche « Acides faibles » ou JNG-PC-03 | JNG-PC-03 (0,68) · JNG-PC-02 (0,67) · fiche acides faibles (0,66) | ✅ |
| R5 | Hors-base | `météo demain à Dakar` | Aucun chunk pertinent | Non testé : crédits d'essai Dify épuisés pendant les tests | ⏳ |

Même série en mode **Économique** (mots-clés, sans crédit) : R2 `satellite altitude vitesse` → renvoie l'exercice du **proton** (JNG-PC-11) au lieu du satellite ; R1 → fiches sans rapport. **Conclusion : le mode Économique ne convient pas au français de notre base ; la recherche sémantique est nécessaire** (d'où la clé Gemini).

> Seuil de score : les bons résultats sont entre 0,45 et 0,68 avec cet embedding. Un seuil à 0,5 (valeur du cours) aurait écarté R3 → garder le seuil désactivé ou à 0,4.


## B. Tests de bout en bout (workflow → Exécuter, ou script `webhook/test-api.sh`)

| # | Message de l'élève (`query`) | Comportement attendu | Résultat obtenu |
|---|---|---|---|
| T1 | `JNG-PC-01 : n = 2/40 = 0,05 mol ; C = 0,05/500 = 0,0001 mol/L` | `text` : ✅ n juste · ❌ volume laissé en mL · 💡 convertir en L · ➡️ exercice 0,80 g / 250 mL · source JNG-PC-01 | |
| T2 | `JNG-PC-07 : a = g cos 30 = 8,5 m/s²` | ❌ projection avec cos au lieu de sin · ne donne pas v = 4,4 m/s | |
| T3 | `JNG-PC-13 : 24 jours = 3 périodes donc A = 8,0×10^6 / 3 = 2,7×10^6 Bq` | ✅ 3 périodes · ❌ diviser par 2³ = 8 | |
| T4 | `JNG-PC-02 : pH = 2 puis pH = 3 après dilution` | ✅ tout juste · félicitations · ➡️ exercice HNO₃ | |
| T5 | `Je n'ai jamais vu l'effet photoélectrique en classe` | Probablement `message_erreur` (pas de réponse d'élève à corriger) — à observer et noter | |
| T6 | `Quelle est la météo demain à Dakar ?` | `message_erreur` : « INSUFFISANT : … ne relève pas du programme de Terminale S » | |
| T7 | `Corrige mon exercice de SVT sur la génétique` | `message_erreur` (matière non couverte) | |
| T8 | Exercice hors base, énoncé complet + réponse | Correction avec SOURCES « hors base Jàng — résolution non vérifiée par un professeur » | |

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
