# Module D — Fonctionnalités IA innovantes pour Jàng (P-Idées)

> Méthode du tutoriel S5+ §5 : partir du HMW et d'une douleur précise du VPC, transposer un pattern du catalogue §5.2, noter avec la grille §5.3, **l'équipe choisit**.
> Rappel HMW [Projet] : explication **fiable** de ses erreurs, **le soir même**, sur **son téléphone**, **sans dépasser son forfait data**, **afin de savoir se corriger seule**.

## Proposition 1 — « Vérifie mon exercice similaire » (boucle d'entraînement)

- **Phrase :** Pour Aminata, quand elle a refait l'exercice similaire proposé dans ➡️ À TOI, l'agent compare son résultat à la réponse vérifiée de la base afin qu'elle sache, le soir même, si elle sait maintenant se corriger seule.
- **Douleur / gain :** G2 « comprendre la méthode et pouvoir refaire seule un exercice similaire » ; critère de réussite de la démo S6 [Projet] : « un élève qui s'est trompé réussit l'exercice similaire sans aide ».
- **Patterns :** 4 Garde-fou métier par RAG (« recopier, ne jamais calculer ») + 5 Sortie actionnable (bouton qui pré-remplit le message).
- **Impact Dify :** la colonne `Reponse_similaire` existe déjà dans `jang_exercices_pc_ts2.csv` [Projet] ; une règle dans le Chercheur pour le format `JNG-PC-07 · similaire : a = …` (comparer à `Reponse_similaire`, ne jamais recalculer) ; une variante du Rédacteur (verdict ✅/❌ court, sans réexpliquer tout le cours).
- **Impact application :** bouton « J'ai fait l'exercice similaire » sous chaque correction → pré-remplit `JNG-PC-xx · similaire : ` dans la zone de saisie (`ChatJang.tsx`).
- **Risque éthique + garde-fou :** une réponse de référence fausse validerait une erreur → « corrigé Jàng, en attente de validation par un professeur » reste affiché ; si la réponse est fausse, on ne donne pas le résultat, seulement l'indice de la 1re erreur.

| Alignement HMW | Valeur en soutenance | Faisabilité | Risque maîtrisé | Dépendance | **Total** |
|---|---|---|---|---|---|
| 5 | 5 | 5 | 4 | 5 | **24 / 25** |

## Proposition 2 — « Photo de ma copie » (photo → extraction)

- **Phrase :** Pour Aminata, quand son calcul est long à taper au téléphone (fractions, puissances de 10, racines), l'agent lit la photo de sa copie manuscrite et en extrait sa réponse afin qu'elle reçoive sa correction sans tout ressaisir.
- **Douleur :** P5 « peu de temps, révise tard, fatiguée » ; saisie des formules pénible sur un Android d'entrée de gamme [Analyse].
- **Pattern :** 3 Photo → extraction (multimodal) + 6 Validation humaine.
- **Impact Dify :** variable fichier dans DÉBUT, nœud LLM vision (Gemini Flash-Lite accepte les images [Hypothèse — à confirmer dans Dify]) qui transcrit la réponse, puis la chaîne actuelle.
- **Impact application :** bouton « Prendre une photo » + **compression dans le navigateur** (≤ 100 Ko) + écran « Jàng a lu : … — c'est bien ça ? » avant envoi ; upload via la fonction serveur (`/v1/files/upload`).
- **Risque :** **contradiction avec la contrainte data du HMW** (une photo pèse 1–3 Mo sans compression) ; photos de personnes interdites ; écriture mal lue → validation obligatoire avant correction.

| Alignement HMW | Valeur en soutenance | Faisabilité | Risque maîtrisé | Dépendance | **Total** |
|---|---|---|---|---|---|
| 3 | 5 | 2 | 3 | 4 | **17 / 25** |

## Proposition 3 — « Mon bilan du soir » (progression de la session)

- **Phrase :** Pour Aminata, à la fin de sa séance de révision, l'agent résume les exercices corrigés ce soir (chapitre, juste / erreur) afin qu'elle voie ce qu'elle maîtrise et quel chapitre revoir demain.
- **Gain :** G3 « voir qu'elle progresse (chapitres maîtrisés, erreurs qui ne reviennent plus) ».
- **Patterns :** 9 Mémoire de session + 10 Synthèse de lot.
- **Impact Dify :** aucun pour la version simple (la 2e ligne de chaque correction donne déjà « Physique · Lois de Newton ») ; option : un nœud de synthèse.
- **Impact application :** encart « Ce soir » au-dessus du chat (compteurs par chapitre, en mémoire React uniquement), bouton « Résumer ma séance ».
- **Risque :** données d'apprentissage d'une mineure → **rien n'est stocké** (perdu au rechargement), aucune donnée envoyée en plus à Dify.

| Alignement HMW | Valeur en soutenance | Faisabilité | Risque maîtrisé | Dépendance | **Total** |
|---|---|---|---|---|---|
| 3 | 4 | 4 | 5 | 5 | **21 / 25** |

## Recommandation [Analyse]

**Proposition 1.** Elle ferme la boucle promise par le HMW (« afin de savoir se corriger seule ») et se démontre en moins de 2 minutes : T1 (erreur repérée) → l'élève refait l'exercice similaire → ✅. Elle réutilise une donnée déjà dans la base (`Reponse_similaire`), ne coûte aucune clé ni service, et respecte la contrainte data. La proposition 2 est la plus spectaculaire mais contredit la contrainte data et demande une séance entière ; à garder pour une V3.

**Tests prévus pour la proposition 1 :** T7 `JNG-PC-07 · similaire : a = 3,4 m/s² ; v = 3,2 m/s` (juste → ✅ bravo, chapitre maîtrisé) ; T8 `JNG-PC-01 · similaire : C = 0,02/250 = 0,00008 mol/L` (faux → ❌ indice sur l'erreur, sans donner 0,080 mol/L).
