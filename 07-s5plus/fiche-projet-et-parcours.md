# S5+ — Faire vivre l'agent dans l'application, l'enrichir, la mettre en ligne

> Application du *Tutoriel GET 409 S5+ (version du 01/10/2026)* à **Jàng**, et non à l'exemple Kayit.
> Étiquettes : **[Projet]** documents de l'équipe · **[Cours]** tutoriel S5+ / supports GET 409 · **[Analyse]** proposition de Claude · **[Hypothèse]** à vérifier.

## Phase 0 — Fiche projet

| Champ | Valeur | Source |
|---|---|---|
| HMW | « Comment pourrions-nous permettre aux élèves de Terminale scientifique des lycées de région, qui révisent seuls faute de professeur, de recevoir le soir même une explication fiable de leurs erreurs sur les exercices d'annales — depuis le téléphone qu'ils ont déjà et sans dépasser leur petit forfait data — afin d'aborder le Bac en sachant se corriger seuls ? » | [Projet] `docs/hmw-definitif.md` |
| Utilisateur principal + contexte | Aminata (persona), Terminale S2 à Kaffrine ; révise seule le soir ; Android d'entrée de gamme, forfait data au jour le jour ; lit et écrit le français, parle wolof | [Projet] carte d'empathie, VPC |
| Agent Dify | App **« jang »**, type **Workflow** ; 2 nœuds LLM (Chercheur temp. 0, Rédacteur temp. 0,3) sur **`gemini-3.5-flash-lite`**, clé Gemini de l'équipe (statut actif, vérifié le 01/10) ; version publiée **« S5 RAG v4 »** | [Projet] Dify, vérifié par API console |
| Variable d'entrée (DÉBUT) | `query` (paragraphe, obligatoire) — « Ton exercice et ta réponse » | [Projet] |
| Variables de sortie | **Sortie 2** → `text` (correction) · **Sortie** → `message_erreur` (refus, commence par « INSUFFISANT : ») | [Projet] |
| Bases RAG | `Jang_KB_v1` : 14 exercices PC TS2 (CSV, 1 morceau / exercice) + 14 fiches de cours (MD) — haute qualité `gemini-embedding-001`, recherche sémantique, Top K 3 · `Jang_Programme_v1` : base fixe (programme TS2 + constantes, 1 morceau) lue par une requête ENV · nœud Code `EXTRAIRE_ID` (ID → énoncé de référence) | [Projet] `dify/` |
| Règles métier / garde-fous | Recopier le corrigé de la base au lieu de recalculer ; INSUFFISANT si hors programme, autre matière, réponse illisible, ID sans réponse ; jamais la solution complète ; 90 mots max ; pas de LaTeX ; « Jàng peut se tromper » | [Projet] `dify/prompts-agents.md` |
| MVP | Lovable « Jàng: Your Bac Coach » ; chat « Corrige mon exercice » sur la page **Exercices** (`src/components/ChatJang.tsx`) ; site Lovable dépublié depuis le 29/09 à la demande de l'équipe | [Projet] |
| Stack détectée | `@tanstack/react-start` dans `package.json`, `src/routes/`, `src/lib/corriger.functions.ts` avec `createServerFn` → **Lovable récent — TanStack Start (SSR)** ; Nitro `cloudflare-module` par défaut | [Projet] confirmé dans le dépôt (§1.3 du cours) |
| Clé API Dify | **Côté serveur** : `process.env.DIFY_API_KEY` (secret Lovable) ; en local `.env.local` (ignoré par Git) | [Projet] |
| Dépôt, accès local, OS | [`cboye4991-sketch/jang-bac-helper`](https://github.com/cboye4991-sketch/jang-bac-helper) (code, synchronisé avec Lovable) + [`cboye4991-sketch/jang`](https://github.com/cboye4991-sketch/jang) (dossier du cours) ; clone local `~/Downloads/class07/jang-bac-helper` ; **macOS** | [Projet] |
| État actuel | ✅ Workflow publié, 10/10 dernières exécutions réussies ; ✅ build local OK ; ✅ le chat affiche la vraie raison des refus ; ⚠️ aucun lien public actif (site Lovable dépublié, Vercel/Netlify exclus par l'enseignant) ; ⚠️ limite « knowledge base request rate limit » du plan Dify gratuit si les tests s'enchaînent | [Projet] / tests du 01/10 |

**Cases à compléter par l'équipe :** aucune.

## Parcours personnalisé (règle de décision §1.2)

Rien n'est cassé → **B** avant toute nouvelle fonctionnalité, puis **D** ; **C** car les crédits Lovable sont épuisés ; **F** demandé par l'équipe (lien public hors Lovable).

| Ordre | Module | Statut | Estimation | Ce qui a été fait / reste |
|---|---|---|---|---|
| — | **A** Modèle de l'agent | ✅ déjà fait | — | Gemini Flash-Lite avec la clé de l'équipe depuis le 28/09 ; régressions traitées en S5 (T8, réponse illisible) |
| 1 | **E** Erreur lisible (§6.1) | ✅ fait le 01/10 | S | Le chat affiche « Détail technique : Dify 400 : … » ou « Clé API absente du serveur », jamais la clé |
| 2 | **B** Batterie T1–T6 | ✅ fait le 01/10 | S | [`tests-t1-t6.md`](tests-t1-t6.md) — 1 correction de prompt (T3) |
| 3 | **C** Local (GitHub → VS Code + Claude Code) | ✅ fait | S | Clone, `npm install`, build et `npm run dev` validés ; routine macOS `relancer_local.command` |
| 4 | **F** Mise en ligne hors Lovable | ✅ en ligne (01/10) | S | **GitHub Pages + fonction Supabase `corriger`** (option du §4.6 « si votre agent passe déjà par une Edge Function Supabase, gardez-la ») : **https://cboye4991-sketch.github.io/jang-bac-helper/** — clé dans les secrets Supabase. Cloudflare Workers (piste 1) reste prêt en secours (essai à blanc réussi). |
| 5 | **D** Fonctionnalité innovante | ✅ « Vérifie mon similaire » choisie et livrée (01/10) | M | [`module-d-fonctionnalites.md`](module-d-fonctionnalites.md) |

## Check-list de fin de séance (§8)

| ✓ | Point | État au 01/10 |
|---|---|---|
| ✅ | Agent Dify sur un modèle avec notre clé (point vert), workflow publié | Gemini Flash-Lite, « S5+ v6 (similaire) » publiée |
| ✅ | T1–T6 écrits dans le Journal et tous réussis après la dernière modification | [tests-t1-t6.md](tests-t1-t6.md) |
| ✅ | Au moins 1 fonctionnalité innovante : spec, Dify, app, tests T7–T8 | « Vérifie mon similaire » — Dify « S5+ v6 », bouton dans le chat ([module D](module-d-fonctionnalites.md)) |
| ✅ | Code poussé sur GitHub sans `.env.local` ; Lovable synchronisé | après `git push` de l'équipe |
| 🟡 | Lien public testé depuis un autre appareil | [https://cboye4991-sketch.github.io/jang-bac-helper/](https://cboye4991-sketch.github.io/jang-bac-helper/) testé le 01/10 depuis le navigateur de Claude : T2 (correction + titres colorés + bouton) et T7 (vérification) ✅ — **reste : test depuis un téléphone** |
| ✅ | Journal L4 complété | entrée S5+-1 |
| ✅ | Note d'éthique mise à jour (1 ligne par fonctionnalité) | [§5 du registre](../docs/note-ethique-rag.md) |
| ✅ | Aucune clé collée dans un chat | clé collée uniquement dans Dify, Lovable, `.env.local` |
