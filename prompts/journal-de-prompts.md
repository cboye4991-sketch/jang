# Journal de Prompts — Jàng

> Livrable S2 — démarré en S1. Chaque prompt utilisé est documenté : technique, résultat, critique, itération.

---

## Entrée 1 — Découverte du secteur (Prompt S1)

- **Date :** 22/09/2026 · **Outil :** Claude
- **Technique :** Prompt contextualisé (rôle + tâche + format)

**Prompt :**
```
Tu es un expert en éducation secondaire au Sénégal.
Identifie les 3 principaux problèmes que rencontrent les élèves de Terminale
dans les lycées des régions (hors Dakar) pour préparer le Bac.
Pour chaque problème, indique :
- La cause principale
- L'impact sur la vie quotidienne
- Une piste de solution technologique accessible
```

**Résultat (résumé) :** manque de professeurs dans certaines matières scientifiques ; accès limité aux ressources et corrigés ; coût de la data et des cours particuliers.

**Critique :** pertinent mais générique ; aucune donnée chiffrée vérifiable. Toute statistique devra être vérifiée avant d'être citée.

**Itération :** préciser la série (S2) et la région (Kaffrine) pour obtenir un résultat plus ancré.

---

## Entrée 2 — Guide d'interview (Prompt S2)

- **Technique :** Rôle + format imposé

**Prompt :**
```
Tu es un UX Researcher spécialisé dans les usages numériques en Afrique de l'Ouest.
Je dois interviewer une élève de Terminale S2 de 17 ans qui vit à Kaffrine
et fait face au problème suivant : elle révise seule sans professeur ni corrigé
et ne sait pas si ses exercices sont justes.
Génère un guide d'interview d'empathie avec :
1. 3 questions d'ouverture
2. 5 questions d'exploration en profondeur ('Pourquoi ?' et 'Racontez-moi...')
3. 2 questions sur les aspirations et les gains attendus
Format : questions numérotées, courtes, sans jargon technique.
```

**Résultat :** voir [`01-empathize/guide-interview.md`](../01-empathize/guide-interview.md).

**Critique :** les questions sont claires ; nous avons ajouté une question sur l'usage du téléphone, absente de la première version.

---

## Entrée 3 — Générateur de HMW (Prompt S3)

- **Technique :** Rôle + observations + critères + format

**Prompt :**
```
Tu es un facilitateur en Design Thinking.
Voici les observations clés de notre interview avec Aminata, 17 ans, Terminale S2 à Kaffrine :
Observation 1 : Elle récupère des annales en PDF dans le groupe WhatsApp de sa classe.
Observation 2 : Elle recopie les solutions trouvées sans les comprendre.
Observation 3 : Elle coupe ses données mobiles pour économiser son forfait.
La frustration principale identifiée est : elle n'a aucun moyen de savoir si ses exercices sont justes ni pourquoi.
Génère 5 énoncés 'Comment pourrions-nous...' (HMW) qui reformulent cette frustration
en opportunité de conception.
Critères : ni trop vague, ni trop précis, ne propose pas encore de solution.
Format : liste numérotée, 1 phrase par énoncé.
```

**Résultat :** voir [`02-define/hmw.md`](../02-define/hmw.md) — HMW n°1 retenu.

**Critique :** le HMW n°3 proposait déjà un canal (WhatsApp), donc une solution ; écarté.

---

## Entrée 4 — Carte d'empathie (Prompt S4)

- **Technique :** Markdown Prompting (format de sortie strict)

**Prompt :** template S4 complété avec le persona d'Aminata et nos observations (voir en-tête de la carte).

**Résultat :** voir [`01-empathize/carte-empathie.md`](../01-empathize/carte-empathie.md).

**Critique :** la structure est directement exploitable. Les observations reposent sur nos interviews croisées ; elles seront confrontées à des interviews de vrais lycéens.

---

# Séance 2 — Les 5 prompts métier (TP guidé) + prompts VPC / HMW

> Format demandé : technique, prompt exact, résumé de la réponse, note /5 avec justification, itération si < 3/5.

## P1 — Les 3 problèmes du persona (Zero-Shot)

- **Date :** S2 · **Outil :** Claude.ai · **Technique :** Zero-Shot (Rôle + Contexte + Tâche + Format)

**Prompt :**
```
Tu es consultant en éducation secondaire au Sénégal.
Notre persona est Aminata, 17 ans, élève en Terminale S2 dans un lycée public de Kaffrine.
Elle révise seule le soir sur un smartphone Android d'entrée de gamme, avec un forfait data acheté au jour le jour,
et n'a pas eu de professeur de physique-chimie pendant plusieurs semaines.
Identifie les 3 principaux problèmes d'Aminata pour préparer le Bac.
Réponds sous forme de tableau en français : Problème | Cause | Conséquence sur ses révisions.
```

**Résumé de la réponse :** (1) aucun retour sur ses erreurs → elle répète les mêmes fautes ; (2) chapitres non enseignés → lacunes de cours avant même l'exercice ; (3) coût des ressources (cours particuliers, data) → elle se limite aux PDF gratuits.

**Note : 4/5** — les 3 problèmes correspondent exactement à nos verbatims S1. -1 : la réponse reste qualitative (aucune donnée) ; les faits chiffrés ont été ajoutés à la main, avec leurs sources, dans `docs/chapeaux-bono.md`.

**Itération :** aucune nécessaire (≥ 3/5).

---

## P2 — 5 idées de fonctionnalités MVP (Zero-Shot)

- **Technique :** Zero-Shot

**Prompt :**
```
Tu es Product Manager spécialisé dans les services numériques pour l'éducation en Afrique de l'Ouest.
Contexte : des élèves de Terminale scientifique en région révisent seuls les annales du Bac sénégalais,
sans corrigé expliqué, sur un smartphone d'entrée de gamme avec très peu de data.
Propose 5 idées de fonctionnalités pour un MVP qui les aide à savoir si leurs exercices sont justes et pourquoi.
Pour chaque idée : nom court, description en 1 phrase, consommation data estimée (faible/moyenne/forte).
Format : liste numérotée.
```

**Résumé de la réponse :** correcteur par message ; exercice du jour ; mini-vidéos explicatives ; quiz QCM par SMS ; tableau de progression.

**Note : 3/5** — idées pertinentes mais deux contredisent nos contraintes (vidéos = data forte ; tableau de progression = application web à ouvrir). La réponse n'expliquait pas comment garantir une correction juste.

**Itération :** ajout de la contrainte « aucune vidéo, tout doit fonctionner dans une messagerie déjà installée, et chaque correction doit pouvoir être vérifiée ». Résultat v2 : correcteur par message, exercice du soir, rappel de cours en 5 lignes, corrigés de référence validés par un professeur, bilan hebdomadaire par message → repris comme Produits & Services du VPC (S1 à S6). **v2 : 4/5.**

---

## P3 — Défi → Solution dans notre secteur (Few-Shot)

- **Technique :** Few-Shot (2 exemples puis la vraie question)

**Prompt :**
```
Voici des exemples de défis éducatifs au Sénégal et de solutions numériques adaptées :

Défi : Des élèves de CM2 en zone rurale n'ont pas de livres de lecture à la maison.
Solution : Des histoires courtes en français et en wolof envoyées en messages vocaux aux parents, 3 fois par semaine.

Défi : Des collégiens oublient les dates des compositions et n'ont pas d'agenda.
Solution : Un rappel par SMS envoyé par l'établissement 3 jours avant chaque composition, avec la liste des chapitres.

Défi : Des élèves de Terminale S en région refont les annales du Bac mais ne savent jamais pourquoi leur réponse est fausse.
Solution :
```

**Résumé de la réponse :** « Un correcteur par messagerie : l'élève envoie sa réponse, reçoit en 6 lignes ce qui est juste, la première erreur et la bonne méthode, puis un exercice similaire à refaire. »

**Note : 5/5** — les exemples ont imposé le format court et le réflexe « canal déjà utilisé + faible coût » ; la solution tient en une phrase, exactement au niveau de détail voulu. C'est la meilleure formulation de notre MVP à ce stade.

---

## P4 — Analyse cause → obstacle → solution (Chain-of-Thought)

- **Technique :** Chain-of-Thought

**Prompt :**
```
Tu es un expert en éducation et en technologies éducatives en Afrique de l'Ouest.
Analyse le problème suivant : les élèves de Terminale scientifique des lycées de région révisent seuls
et ne savent pas si leurs exercices d'annales sont justes ni pourquoi.
Réfléchis étape par étape :
Étape 1 : Identifie la cause principale du problème dans le contexte des régions du Sénégal (ex. Kaffrine).
Étape 2 : Décris l'obstacle principal qui empêche une solution classique (cours particuliers, plateforme en ligne, vidéos) de fonctionner.
Étape 3 : Propose une solution technologique accessible à Aminata, 17 ans, Android d'entrée de gamme, forfait au jour le jour.
Développe chaque étape avant de conclure. Termine par les 2 risques principaux de ta solution.
```

**Résumé de la réponse :** cause = absence ou rotation des professeurs de sciences + corrigés non expliqués ; obstacle = coût (cours) et poids data (plateformes, vidéos) + besoin d'un retour *personnalisé* ; solution = correcteur conversationnel sur messagerie. Risques : correction erronée d'une IA ; recopie de la solution sans compréhension.

**Note : 5/5** — le raisonnement étape par étape a fait apparaître le risque de fiabilité, absent de P1 et P2. Ce risque est devenu le R1 du Chapeau Noir et est désormais intégré au HMW définitif.

---

## P5 — Prompt libre : simulation de correction par Jàng (rôle + contraintes + format strict)

- **Technique :** Libre — prompt système de rôle + Chain-of-Thought caché + format de sortie verrouillé (test du futur moteur du MVP)

**Prompt :**
```
# RÔLE
Tu es Jàng, un correcteur bienveillant qui prépare des élèves sénégalais au Bac S2 en physique-chimie.

# EXERCICE (annale Bac)
On dissout 2,0 g d'hydroxyde de sodium (NaOH) dans 500 mL d'eau. Calcule la concentration molaire de la solution.
Données : M(Na) = 23 g/mol ; M(O) = 16 g/mol ; M(H) = 1 g/mol.

# CORRIGÉ DE RÉFÉRENCE (validé)
n = m/M = 2,0/40 = 0,050 mol ; C = n/V = 0,050/0,500 = 0,10 mol/L

# RÉPONSE DE L'ÉLÈVE
n = 2/40 = 0,05 mol ; C = 0,05/500 = 0,0001 mol/L

# TÂCHE
Compare la réponse de l'élève au corrigé, étape par étape, sans montrer ce raisonnement.
Ne donne PAS la solution complète en premier.

# FORMAT DE SORTIE STRICT (message WhatsApp, 6 lignes maximum, français simple)
✅ Ce qui est juste :
❌ L'erreur :
💡 La bonne méthode :
➡️ Essaie maintenant : [exercice similaire court]
```

**Résumé de la réponse :** ✅ calcul de la quantité de matière correct ; ❌ le volume doit être en litres (500 mL = 0,500 L) ; 💡 toujours convertir en L avant C = n/V ; ➡️ exercice similaire avec 250 mL.

**Note : 4/5** — erreur identifiée juste, format respecté (5 lignes), ton encourageant. -1 : la qualité dépend du corrigé de référence fourni ; sans lui, rien ne garantit que l'IA ne se trompe pas → le corrigé validé devient obligatoire (Pain Reliever P7 du VPC).

**Itération :** le bloc « CORRIGÉ DE RÉFÉRENCE » est conservé dans toutes les versions. Prochaine itération S3 : même test avec une photo de copie manuscrite, puis sans corrigé de référence pour mesurer l'écart.

---

## P-VPC-1 — Profil Client (handout VPC)

- **Technique :** Markdown Prompting (format strict)
- **Prompt :** template P-VPC-1 complété avec : « Aminata Diallo, 17 ans, élève de Terminale S2, Kaffrine » · « Elle révise seule sans professeur et ne sait jamais si ses exercices sont justes » · « Smartphone Android d'entrée de gamme » · « Si quelqu'un pouvait juste me dire où je me trompe, je pourrais avancer seule. »
- **Résultat :** 4 Jobs, 4 Pains, 4 Gains → complétés et tracés dans [`docs/vpc.md`](../docs/vpc.md).
- **Note : 4/5** — éléments fidèles à la carte d'empathie ; ceux qui n'ont pas été entendus en interview (connexion instable le soir, peur d'apprendre faux) sont gardés mais marqués *[à valider]* (règle « Est-ce qu'on a entendu ça ? »).

## P-VPC-2 — Proposition de Valeur

- **Technique :** Markdown Prompting, continuation de conversation
- **Prompt :** template P-VPC-2 avec « Jàng — un correcteur d'exercices du Bac qui répond sur WhatsApp : l'élève envoie sa réponse, Jàng explique son erreur et lui fait refaire un exercice similaire. »
- **Résultat :** Produits & Services, Pain Relievers, Gain Creators, FIT Check → [`docs/vpc.md`](../docs/vpc.md).
- **Note : 4/5** — FIT correct ; la réponse proposait des « vidéos courtes » en Pain Reliever de P2 : retiré car contredit P3 (data).

## P-HMW — HMW définitif

- **Technique :** Rôle + insights structurés (Blanc / Noir / Bleu + FIT) + format strict
- **Prompt :** template P-HMW complété avec notre draft S1, Chapeau Blanc (déficit d'enseignants, taux de réussite 2025), Chapeau Noir (R1 fiabilité, R2 data), Chapeau Bleu (recentrer sur les séries scientifiques), FIT P1→S1 et P3→format texte.
- **Résultat :** 3 versions (A trop précise, B trop large, C bien calibrée) → C retenue, voir [`docs/hmw-definitif.md`](../docs/hmw-definitif.md).
- **Note : 5/5** — la version C passe les 3 questions de validation (persona, 3 solutions possibles, risque du Chapeau Noir intégré).

---

## Modèle pour les prochaines entrées

```
## Entrée N — [Titre]
- Date : · Outil : · Technique : (zero-shot / few-shot / chain-of-thought / markdown)
**Prompt :**
**Résultat (résumé) :**
**Critique :** (ce qui manque, hallucinations repérées)
**Itération :** (ce qu'on a changé et pourquoi)
```
