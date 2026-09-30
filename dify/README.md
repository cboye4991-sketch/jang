# Jàng × Dify — mise en place S3 + S5

> **GET 409 · Séance 5 — Intégration & RAG avec Dify**, adaptée à Jàng.
> **État au 28/09/2026 :** le workflow S3 « jang » existait déjà dans Dify. La base **Jang_KB_v1** a été créée et branchée devant le Chercheur (détail : [`prompts-agents.md`](prompts-agents.md)). La séance 4 (MVP) est reportée volontairement ; le branchement au MVP est prêt dans [`webhook/prompt-lovable.md`](webhook/prompt-lovable.md).
> ✅ **30/09/2026 : version « S5 RAG v3 »** — RAG à deux recherches : base fixe `Jang_Programme_v1` (programme TS2 + constantes) lue à chaque question, ce qui corrige T8 ([détail](tests-rag.md#b-bis-rag-à-deux-recherches--base-fixe-programme-30092026-version--s5-rag-v3-)).
> ✅ **Publié le 28/09/2026** (version « S5 RAG v2 ») avec la clé Gemini gratuite : `gemini-3.5-flash-lite` pour les agents, `gemini-embedding-001` pour la base. 7 tests sur 8 validés ([plan de tests](tests-rag.md)).

## Ce qui tourne dans Dify

```
Début ─▶ Récupération Jang_KB_v1 ─▶ RECUP_PROGRAMME ─▶ MODÈLE ─▶ Chercheur ─▶ SI/SINON ─┬─▶ Sortie (message_erreur)   si INSUFFISANT
                                                                                         └─▶ Rédacteur ─▶ Sortie 2 (text)
```

Pour Jàng, le RAG n'est pas un bonus : c'est la **promesse de fiabilité du VPC** (Pain Reliever P7). Au lieu de refaire l'exercice lui-même, le Chercheur reprend le **corrigé de référence** stocké dans la base.

## Fichiers de la base (dossier `knowledge/`)

| Fichier | Contenu | Chunk | Chevauchement |
|---|---|---|---|
| [`jang_exercices_pc_ts2.csv`](knowledge/jang_exercices_pc_ts2.csv) | 14 exercices type Bac PC Terminale S2 : énoncé, corrigé de référence, résultat, erreur fréquente, exercice similaire + réponse | 2000 → **14 morceaux, 1 par exercice** | 0 |
| [`jang_fiches_cours_pc_ts2.md`](knowledge/jang_fiches_cours_pc_ts2.md) (version PDF : [`.pdf`](knowledge/jang_fiches_cours_pc_ts2.pdf)) | 14 fiches « pas vu en classe » (5 lignes par chapitre) + ce que Jàng ne couvre pas | 500 → 17 morceaux | 0 |
| [`jang_programme_constantes_ts2.md`](knowledge/jang_programme_constantes_ts2.md) — **base fixe** `Jang_Programme_v1` | Chapitres du programme PC TS2 + constantes (g, h, c, e, G, Ke…), une seule ligne | séparateur `\n\n`, 1000 → 1 morceau | 0 |

Tous les résultats du CSV ont été recalculés. Les exercices sont **rédigés par l'équipe** sur le modèle du Bac (pas copiés d'annales officielles) et portent le statut « À faire valider par un professeur » — à dire honnêtement en démo et dans la note d'éthique.

> **Pourquoi pas 300 comme dans le tutoriel NiayesBiz ?** Testé : à 500, Dify coupait chaque exercice en 3 morceaux ; à 1000, encore 10 exercices sur 14 en deux, avec l'ID séparé du corrigé (les symboles ×, √, τ, Ω comptent pour beaucoup de tokens). À 2000, chaque exercice tient en un morceau (312 à 485 tokens). Les fiches de cours ont été importées en Markdown, un titre par chapitre, et le PDF est gardé dans le dépôt pour le livrable.

---

## Partie 1 — Base de connaissances ✅ (faite le 28/09)

- Dify → **Connaissance** → **Jang_KB_v1** : 2 documents 🟢 *Disponible* (CSV + fiches). → 📸 **Capture L2-a** à faire
- Tests de récupération R1–R4 réussis en recherche sémantique (voir [plan de tests](tests-rag.md)).
- Mode : **Haute qualité**, `gemini-embedding-001`, recherche **sémantique**, Top K 3 (le mode Économique a été testé et écarté).

## Partie 2 — Workflow ✅ (S3 existant + nœud RAG ajouté le 28/09)

- Studio → **jang** : nœud **Récupération Jang_KB_v1** entre Début et Chercheur ; contexte injecté dans le Chercheur ([détail](prompts-agents.md)).
- Modèles `gemini-3.5-flash-lite`, workflow **publié**. → 📸 **Capture L2-b** à faire (canevas complet)

## Partie 3 — Publication et API (≈ 10 min)

1. **Publier** → **Publier la mise à jour**.
2. **Publier ▸ Accéder à la référence API** → URL : `https://api.dify.ai/v1/workflows/run`.
3. **Clé API** → **+ Créer une nouvelle clé secrète** → copier (`app-…`, affichée une seule fois) → la garder dans un gestionnaire de mots de passe, **jamais dans le dépôt**.
4. Tester sans MVP depuis un terminal :
   ```bash
   export DIFY_API_KEY="app-..."
   bash dify/webhook/test-api.sh
   bash dify/webhook/test-api.sh "Quelle est la météo demain à Dakar ?"   # → message_erreur
   ```
5. Lancer T1 → T7 du [plan de tests](tests-rag.md#b-tests-de-bout-en-bout-workflow--exécuter-ou-script-webhooktest-apish) et remplir la colonne *Résultat obtenu*.

## Partie 4 — Branchement au MVP (à la reprise de S4)

Coller le prompt de [`webhook/prompt-lovable.md`](webhook/prompt-lovable.md) dans Lovable, remplacer la clé, vérifier la checklist.

---

## Livrables S5 — état

| # | Livrable | Pts | État |
|---|---|---|---|
| L1 | MVP V2 en ligne avec formulaire RAG | 30 | ⏸️ Bloqué tant que S4 n'est pas fait — prompt prêt |
| L2 | Pipeline RAG : capture base indexée + agent connecté + URL workflow | 30 | ✅ Publié et testé — reste à faire les 2 captures d'écran |
| L3 | Schéma d'architecture V2 | 20 | ✅ [`docs/architecture-v2.png`](../docs/architecture-v2.png) · [PDF](../docs/architecture-v2.pdf) |
| L4 | Journal de prompts S5 (≥ 3 prompts) | 20 | ✅ Rédigé — résultats des tests à compléter ([journal](../prompts/journal-de-prompts.md#séance-5--rag--intégration-dify)) |
| S6 | Note d'éthique d'une page | — | ✅ [`docs/note-ethique-rag.md`](../docs/note-ethique-rag.md) |
| S6 | Plan B (réponses simulées) | — | ✅ [`soutenance/plan-b-s6.md`](../soutenance/plan-b-s6.md) |

## Dépannage rapide

| Problème | Solution |
|---|---|
| La base ne s'indexe pas | CSV en UTF-8 avec virgules : ne pas le rouvrir/réenregistrer dans Excel (qui passe en point-virgule) |
| Test de récupération vide (mode Économique) | Utiliser les mots exacts de la base (ID `JNG-PC-xx`, « Dipôle RC ») |
| `{{#context#}}` non reconnu | CONTEXTE du Chercheur relié à la récupération **avant** de publier |
| « quota exceeded » | Crédits d'essai épuisés → ajouter une clé API (Intégrations → Fournisseur de modèles) |
| Erreur 401 | Clé mal copiée ou régénérée → Paramètres de l'app → Clé API |
| Réponse vide | Lire `data.outputs.text` (correction) ou `data.outputs.message_erreur` (refus) |
