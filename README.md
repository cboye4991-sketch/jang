# Jàng — Réviser le Bac avec son téléphone

> **GET 409 — Atelier IA** · Swiss UMEF University, Campus de Dakar · 2025–2026
> Enseignant : M. Malick Faye Diagne

## Notre HMW définitif (S2)

> **Comment pourrions-nous permettre aux élèves de Terminale scientifique des lycées de région, qui révisent seuls faute de professeur, de recevoir le soir même une explication fiable de leurs erreurs sur les exercices d'annales — depuis le téléphone qu'ils ont déjà et sans dépasser leur petit forfait data — afin d'aborder le Bac en sachant se corriger seuls ?**

<details><summary>HMW draft S1 et ce qui a changé</summary>

*S1 :* « Comment pourrions-nous permettre aux élèves de Terminale vivant en région de savoir si leurs exercices sont justes — et pourquoi — avec un simple téléphone et peu de data ? »

Le HMW S2 garde le cœur du problème et ajoute ce que la séance 2 nous a appris : la **cause** (absence de professeur dans les séries scientifiques), l'exigence de **fiabilité** de la correction (Chapeau Noir), le **moment** (le soir) et la **finalité** (savoir se corriger seul). Détail : [`docs/hmw-definitif.md`](docs/hmw-definitif.md).
</details>

## Notre proposition de valeur

> Pour les élèves de Terminale scientifique des régions qui révisent seuls faute de professeur, **Jàng** est un correcteur d'annales du Bac sur WhatsApp qui explique la première erreur de chaque réponse et fait aussitôt refaire un exercice similaire — le soir même, pour quelques messages de data — en s'appuyant sur des corrigés validés par un professeur.

Value Proposition Canvas complet : [`docs/vpc.md`](docs/vpc.md) · version image : [`docs/vpc.png`](docs/vpc.png)

## Le problème

Dans plusieurs lycées des régions, des élèves de Terminale passent une partie de l'année sans professeur dans certaines matières scientifiques. Ils révisent seuls avec des annales en PDF partagées sur WhatsApp, sans corrigé détaillé et sans personne pour leur dire *pourquoi* leur réponse est fausse. Les cours particuliers sont trop chers et les vidéos consomment trop de data.

## Notre persona

**Aminata Diallo, 17 ans**, élève en Terminale S2 à Kaffrine — voir la [carte d'empathie](01-empathize/carte-empathie.md).

## La solution envisagée (MVP)

Un **bot WhatsApp** qui :
1. envoie chaque jour un exercice tiré des annales du Bac sénégalais ;
2. reçoit la réponse de l'élève (texte ou photo) ;
3. corrige **étape par étape**, en expliquant l'erreur, dans des messages courts et légers en data.

Outils envisagés : Typebot / Landbot + WhatsApp, Google Sheets pour la banque d'exercices, un modèle d'IA (Claude) piloté par nos prompts.

## Structure du dépôt

| Dossier | Phase Design Thinking | Contenu |
|---|---|---|
| `01-empathize/` | Empathize | Carte d'empathie, guide d'interview, notes |
| `02-define/` | Define | Énoncés HMW et choix final |
| `03-ideate/` | Ideate | Pistes de solutions |
| `04-prototype/` | Prototype | Fonctionnalités MVP, maquettes |
| `05-test/` | Test | Retours utilisateurs |
| `prompts/` | Transverse | Journal de prompts |
| `docs/` | S2 — Idéation & Décision | 6 Chapeaux, VPC, HMW définitif |
| `soutenance/` | — | Pitch 90 s (S1), pitch HMW 2 min (S2) |

## Avancement

| Séance | Livrables | Statut |
|---|---|---|
| S1 — Empathie | [Carte d'empathie](01-empathize/carte-empathie.md) · [HMW draft](02-define/hmw.md) · [Journal de prompts](prompts/journal-de-prompts.md) | ✅ |
| S2 — Idéation & Prompt Engineering | [6 Chapeaux](docs/chapeaux-bono.md) · [VPC](docs/vpc.md) · [HMW définitif](docs/hmw-definitif.md) · [Journal P1–P5](prompts/journal-de-prompts.md#séance-2--les-5-prompts-métier-tp-guidé--prompts-vpc--hmw) · [Pitch 2 min](soutenance/pitch-hmw-s2.md) | ✅ |
| S3 — Multi-agents Dify | Agent correcteur, workflow, schéma d'architecture | ⏳ |

## Équipe

| Nom | Rôle |
|---|---|
| Cheikh BOYE | Membre de l'équipe |
| Adama DIOP | Membre de l'équipe |
