# Jàng × Dify — mise en place S3 + S5

> **GET 409 · Séance 5 — Intégration & RAG avec Dify**, adaptée à Jàng.
> La séance 3 (agents Dify) n'avait pas été faite : ce guide monte les deux d'un coup. La séance 4 (MVP Lovable/Bolt) est reportée volontairement ; le branchement au MVP est prêt dans [`webhook/prompt-lovable.md`](webhook/prompt-lovable.md).
> Durée estimée : **1 h 15** · Outil : [dify.ai](https://cloud.dify.ai)

## Ce qu'on construit

```
Élève ──query──▶ RÉCUPÉRATION (Jang_KB_v1) ──▶ CHERCHEUR ──▶ CORRECTEUR ──answer──▶ Élève
                  14 exercices + 14 fiches      retrouve       corrige en
                  (CSV + PDF)                   l'exercice     6 lignes WhatsApp
```

Pour Jàng, le RAG n'est pas un bonus : c'est la **promesse de fiabilité du VPC** (Pain Reliever P7). Au lieu d'inventer une correction, l'agent compare la réponse de l'élève à un **corrigé de référence** stocké dans la base.

## Fichiers de la base (dossier `knowledge/`)

| Fichier | Contenu | Chunk | Chevauchement |
|---|---|---|---|
| [`jang_exercices_pc_ts2.csv`](knowledge/jang_exercices_pc_ts2.csv) | 14 exercices type Bac PC Terminale S2 : énoncé, corrigé de référence, résultat, erreur fréquente, exercice similaire + réponse | 500 | 50 |
| [`jang_fiches_cours_pc_ts2.pdf`](knowledge/jang_fiches_cours_pc_ts2.pdf) | 14 fiches « pas vu en classe » (5 lignes par chapitre) + ce que Jàng ne couvre pas | 300 | 50 |

Tous les résultats du CSV ont été recalculés. Les exercices sont **rédigés par l'équipe** sur le modèle du Bac (pas copiés d'annales officielles) et portent le statut « À faire valider par un professeur » — à dire honnêtement en démo et dans la note d'éthique.

> Pourquoi 500 et pas 300 comme dans le tutoriel NiayesBiz ? Une ligne de notre CSV (énoncé + corrigé) fait ~250–350 tokens. À 300, un exercice serait coupé en deux et le corrigé séparé de son énoncé.

---

## Partie 1 — Base de connaissances (≈ 20 min)

1. Dify → **Connaissances** → **+ Créer des connaissances** → *Importer à partir d'un fichier* → `jang_exercices_pc_ts2.csv` → **Suivant**.
2. Réglages : **Longueur du morceau 500** · **Chevauchement 50** · Mode d'index **Haute qualité** si un modèle d'embedding est disponible, sinon **Économique** (index inversé) · Top K **3**.
3. **Enregistrer & Traiter** → attendre *Intégration terminée*.
4. `…` → **Paramètres** → renommer la base **`Jang_KB_v1`**.
5. Dans la base : **Ajouter un fichier** → `jang_fiches_cours_pc_ts2.pdf` → morceau **300** / chevauchement **50** → Enregistrer & Traiter.
6. **Documents** : les deux fichiers doivent afficher 🟢 *Disponible*. → 📸 **Capture L2-a**
7. **Test de récupération** : lancer R1 à R5 du [plan de tests](tests-rag.md#a-test-de-récupération-dify--connaissances--jang_kb_v1--test-de-récupération). → 📸 **Capture R1 + R5**

## Partie 2 — Workflow multi-agents (S3, ≈ 30 min)

1. **Studio** → **Créer une application** → *Créer à partir de rien* → type **Workflow** → nom **`Jang_Correcteur_v1`**.
2. Nœud **DÉBUT** → ajouter la variable `query` (Paragraphe, obligatoire, 1000 caractères).
3. `+` après DÉBUT → **Récupération de connaissances** → requête = `Début · query` · connaissances = `Jang_KB_v1`.
4. `+` → **LLM** → renommer **CHERCHEUR** → modèle au choix ([recommandations](prompts-agents.md#choix-du-modèle)), température 0 → **CONTEXTE** = `Récupération de connaissances · result` → coller SYSTEM et USER depuis [`prompts-agents.md`](prompts-agents.md#nœud-chercheur-llm--température-0).
5. `+` → **LLM** → renommer **CORRECTEUR** → température 0,2 → coller SYSTEM et USER ([ici](prompts-agents.md#nœud-correcteur-llm--température-02)) ; insérer les variables `CHERCHEUR · text` et `Début · query` avec `{`.
6. `+` → **FIN** → variable de sortie `answer` = `CORRECTEUR · text`.
7. **Exécuter** → tester T1 et T6. → 📸 **Capture L2-b** (canevas complet DÉBUT → RÉCUPÉRATION → CHERCHEUR → CORRECTEUR → FIN)

## Partie 3 — Publication et API (≈ 10 min)

1. **Publier** → **Publier la mise à jour**.
2. **Publier ▸ Accéder à la référence API** → URL : `https://api.dify.ai/v1/workflows/run`.
3. **Clé API** → **+ Créer une nouvelle clé secrète** → copier (`app-…`, affichée une seule fois) → la garder dans un gestionnaire de mots de passe, **jamais dans le dépôt**.
4. Tester sans MVP depuis un terminal :
   ```bash
   export DIFY_API_KEY="app-..."
   bash dify/webhook/test-api.sh
   bash dify/webhook/test-api.sh "Quelle est la météo demain à Dakar ?"
   ```
5. Lancer T1 → T7 du [plan de tests](tests-rag.md#b-tests-de-bout-en-bout-workflow--exécuter-ou-script-webhooktest-apish) et remplir la colonne *Résultat obtenu*.

## Partie 4 — Branchement au MVP (à la reprise de S4)

Coller le prompt de [`webhook/prompt-lovable.md`](webhook/prompt-lovable.md) dans Lovable, remplacer la clé, vérifier la checklist.

---

## Livrables S5 — état

| # | Livrable | Pts | État |
|---|---|---|---|
| L1 | MVP V2 en ligne avec formulaire RAG | 30 | ⏸️ Bloqué tant que S4 n'est pas fait — prompt prêt |
| L2 | Pipeline RAG : capture base indexée + agent connecté + URL workflow | 30 | 📦 Fichiers prêts — à monter dans Dify (Parties 1–3) |
| L3 | Schéma d'architecture V2 | 20 | ✅ [`docs/architecture-v2.png`](../docs/architecture-v2.png) · [PDF](../docs/architecture-v2.pdf) |
| L4 | Journal de prompts S5 (≥ 3 prompts) | 20 | ✅ Rédigé — résultats des tests à compléter ([journal](../prompts/journal-de-prompts.md#séance-5--rag--intégration-dify)) |
| S6 | Note d'éthique d'une page | — | ✅ [`docs/note-ethique-rag.md`](../docs/note-ethique-rag.md) |
| S6 | Plan B (réponses simulées) | — | ✅ [`soutenance/plan-b-s6.md`](../soutenance/plan-b-s6.md) |

## Dépannage rapide

| Problème | Solution |
|---|---|
| La base ne s'indexe pas | CSV en UTF-8 avec virgules : ne pas le rouvrir/réenregistrer dans Excel (qui passe en point-virgule) |
| Test de récupération vide (mode Économique) | Utiliser les mots exacts de la base (ID `JNG-PC-xx`, « Dipôle RC ») |
| `{{#context#}}` non reconnu | CONTEXTE du CHERCHEUR relié à la récupération **avant** de publier |
| Erreur 401 | Clé mal copiée ou régénérée → Paramètres de l'app → Clé API |
| Réponse vide | Lire `data.outputs.answer` (workflow), pas `answer` (chatflow) |
