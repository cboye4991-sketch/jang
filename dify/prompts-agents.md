# Workflow Dify « jang » — agents et branchement RAG

> **S3** (fait dans Dify le 23/09/2026) : Début → Chercheur → SI/SINON → Rédacteur.
> **S5** (28/09/2026) : ajout du nœud **Récupération Jang_KB_v1** avant le Chercheur et injection du contexte dans son prompt.
> Sauvegarde de la version S3 : application **« jang (sauvegarde S3) »** dans le Studio Dify.

```
Début (query) ─▶ Récupération Jang_KB_v1 ─▶ Chercheur ─▶ SI/SINON ─┬─ contient « INSUFFISANT » ─▶ Sortie  (message_erreur)
                                                                    └─ sinon ─────────────────────▶ Rédacteur ─▶ Sortie 2 (text)
```

| Nœud | Rôle | Réglages |
|---|---|---|
| **Début** | Variable `query` (paragraphe, obligatoire) — « Ton exercice et ta réponse » | |
| **Récupération Jang_KB_v1** *(S5)* | Cherche l'exercice et son corrigé de référence dans la base | Requête = `Début · query` · Top K = 3 |
| **Chercheur** (LLM) | Analyse la réponse, établit la résolution de référence, repère la première erreur | Contexte = `Récupération · result` · format de sortie strict (MATIÈRE / EXERCICE / RÉPONSE DE RÉFÉRENCE / PREMIÈRE ERREUR / NOTION / EXERCICE SIMILAIRE / SOURCES) ou `INSUFFISANT : …` |
| **SI/SINON** | Garde-fou : si le Chercheur écrit INSUFFISANT, on s'arrête | Condition : `Chercheur.text` contient `INSUFFISANT` |
| **Sortie** | Renvoie la raison du refus | `message_erreur` = `Chercheur.text` |
| **Rédacteur** (LLM) | Met en forme la correction pour WhatsApp (✅ ❌ 💡 ➡️, 90 mots max, tutoiement) | Entrée = `Chercheur.text` |
| **Sortie 2** | Correction finale | `text` = `Rédacteur.text` |

Via l'API : la correction est dans `data.outputs.text`, un refus dans `data.outputs.message_erreur`.

## Ce qui a été ajouté au prompt SYSTEM du Chercheur (S5)

Le prompt S3 est conservé tel quel ; ce bloc est ajouté à la fin :

```
BASE DE CONNAISSANCES JÀNG (exercices et corrigés de référence) :
{{#context#}}

RÈGLES RAG (prioritaires sur l'étape 2) :
- Si l'exercice de l'élève correspond à un exercice de la base (même ID JNG-PC-xx ou même énoncé),
  ta RÉPONSE DE RÉFÉRENCE reprend exactement le Corrige_reference et le Resultat_final de la base,
  ton EXERCICE SIMILAIRE est celui de la base, et SOURCES indique l'ID, par exemple
  « JNG-PC-01 — corrigé Jàng, en attente de validation par un professeur ».
- Si l'élève envoie seulement l'ID (ex. « JNG-PC-07 : a = 8,5 m/s² »), reprends l'énoncé dans la base :
  l'énoncé est alors considéré comme complet.
- Si l'élève dit ne pas avoir vu un chapitre (demande de cours), ce n'est JAMAIS un cas INSUFFISANT,
  même sans exercice ni réponse. Retourne la sortie SUFFISANTE avec RÉPONSE DE L'ÉLÈVE : « aucune —
  demande de cours », PREMIÈRE ERREUR : « Aucune (demande de cours) », NOTION À REVOIR : la fiche de
  cours du chapitre tirée de la base, EXERCICE SIMILAIRE : l'exercice du chapitre dans la base.
- Si l'exercice n'est pas dans la base, applique ta méthode habituelle et écris dans SOURCES
  « hors base Jàng — résolution non vérifiée par un professeur ».
- Si la question ne concerne ni un exercice ni un chapitre de Physique-Chimie ou de Mathématiques
  de Terminale S (météo, actualité, autre matière), réponds INSUFFISANT.
```

**Pourquoi ce choix plutôt qu'un nouveau workflow :** le Chercheur S3 résolvait l'exercice lui-même (« refaite étape par étape à partir des seules données de l'énoncé »), ce qui laisse un risque d'erreur du modèle. Avec le RAG, dès que l'exercice est dans la base, la référence n'est plus inventée : elle est recopiée depuis un corrigé vérifié. Le SI/SINON et le Rédacteur de S3 restent inchangés.

## Ce qui a été ajouté au prompt SYSTEM du Rédacteur (S5, après les tests)

Deux règles insérées dans ses RÈGLES STRICTES :

```
- CAS PAS VU EN CLASSE : si l'élève n'a envoyé aucune réponse à corriger (il dit ne pas avoir vu un
  chapitre), ne fais ni ✅ ni ❌ : remplace-les par une section « 📚 LE COURS EN BREF » (3 à 5 lignes
  tirées de NOTION À REVOIR), puis garde 💡 et ➡️.
- Écris les formules en texte simple lisible sur WhatsApp (ex. : C = n/V, 500 mL = 0,500 L, 10^-3).
  N'utilise jamais LaTeX, ni $, ni \frac, ni \text.
```

Raisons : au test T1, Gemini écrivait `$C = \frac{n}{V}$` (illisible sur WhatsApp) ; au test T5, il répondait « Aucune erreur, bravo » à un élève qui demandait un cours.

## Prompts S3 d'origine

Prompts complets du Chercheur et du Rédacteur : voir l'application « jang (sauvegarde S3) » dans Dify, ou l'onglet du nœud dans le workflow.

## Modèles

| Nœud | S3 | S5 (publié le 28/09) |
|---|---|---|
| Chercheur (temp. 0), Rédacteur (temp. 0,3) | OpenAI `gpt-5.6-luna` (crédits d'essai Dify, épuisés le 28/09) | **`gemini-3.5-flash-lite`** (clé gratuite Google AI Studio), 1 nouvelle tentative automatique |
| Embeddings de la base | — | **`gemini-embedding-001`**, recherche sémantique, Top K 3 |

Versions publiées dans Dify : « S5 RAG + Gemini », puis « S5 RAG v2 » (cas « pas vu en classe »).
