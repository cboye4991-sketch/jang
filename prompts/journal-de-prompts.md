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

# Séance 5 — RAG & intégration Dify

> Livrable L4 (min. 3 prompts : RAG Knowledge + webhook + test de cohérence).
> Le workflow S3 « jang » (Chercheur → SI/SINON → Rédacteur) existait dans Dify ; S5 y ajoute la base RAG. S4 (MVP) est reporté ; le prompt webhook est prêt mais pas encore exécuté.
> Les notes marquées *[à compléter]* dépendent des tests dans Dify : ne pas les remplir avant d'avoir vu le résultat.

## S5-1 — Préparer les documents de la base RAG (prompt S1 de la bibliothèque)

- **Outil :** Claude · **Technique :** Prompt structuré (données + format de sortie imposé)

**Prompt :**
```
Je prépare la base de connaissances RAG de Jàng, un correcteur d'exercices du Bac
sénégalais (Physique-Chimie, Terminale S2) qui compare la réponse de l'élève à un
corrigé de référence.
Produis :
1. Un CSV (séparateur virgule, en-têtes en ligne 1) avec une ligne par exercice :
   ID, Serie, Matiere, Chapitre, Enonce, Donnees, Corrige_reference, Resultat_final,
   Erreur_frequente, Exercice_similaire, Reponse_similaire, Source, Statut_validation,
   Mise_a_jour — un exercice type Bac par chapitre du programme de Terminale S2.
2. Un Markdown avec, pour chaque chapitre, un titre H2 et un rappel de cours
   de 5 lignes maximum (mode « pas vu en classe »).
3. La liste de ce que la base ne couvre pas.
Contraintes : corrigés détaillés et vérifiables, unités SI, virgule décimale,
aucune donnée personnelle.
```

**Résultat :** [`dify/knowledge/jang_exercices_pc_ts2.csv`](../dify/knowledge/jang_exercices_pc_ts2.csv) (14 exercices) et [`jang_fiches_cours_pc_ts2.md`](../dify/knowledge/jang_fiches_cours_pc_ts2.md) / `.pdf` (14 fiches + périmètre).

**Critique : 4/5.** Structure directement indexable, une colonne « erreur fréquente » utile au Chercheur. Tous les résultats ont été **recalculés à part** (script Python) avant d'être gardés : c'est indispensable, un corrigé faux dans la base rendrait toutes les corrections fausses. −1 : ce ne sont pas des annales officielles, et aucun professeur ne les a encore relues → colonne `Statut_validation = À faire valider`.

**Itération (testée dans Dify) :** à 500 tokens, chaque exercice était coupé en 3 morceaux ; à 1000, 10 exercices sur 14 restaient coupés en deux, l'ID séparé du corrigé. À 2000, on obtient 14 morceaux, 1 par exercice. Fiches importées en Markdown (17 morceaux, un par chapitre).

---

## S5-2 — Branchement RAG dans le Chercheur S3

- **Outil :** Dify (workflow `jang`) · **Technique :** injection de contexte `{{#context#}}` + règles prioritaires ajoutées à un prompt existant

**Prompt ajouté :** bloc « BASE DE CONNAISSANCES JÀNG + RÈGLES RAG », texte complet dans [`dify/prompts-agents.md`](../dify/prompts-agents.md#ce-qui-a-été-ajouté-au-prompt-system-du-chercheur-s5).

**Pourquoi :** en S3, le Chercheur refaisait lui-même la résolution de référence : une erreur du modèle devenait une correction fausse (Chapeau Noir R1). Avec le RAG, quand l'exercice est dans la base, la référence est **recopiée** depuis un corrigé vérifié ; le SI/SINON et le Rédacteur de S3 ne changent pas. Nouvelles règles : l'élève peut n'envoyer que l'ID de l'exercice ; « pas vu en classe » renvoie à la fiche de cours ; un exercice hors base est signalé comme non vérifié.

**Résultat (28/09, Gemini `gemini-3.5-flash-lite`) :** 7 tests sur 8 validés ([détail](../dify/tests-rag.md#b-tests-de-bout-en-bout-workflow--exécuter-ou-script-webhooktest-apish)). Sur T1 à T4, le Chercheur recopie le corrigé de la base et cite « JNG-PC-xx — corrigé Jàng » ; l'erreur pointée est toujours la bonne. T6 (météo) et T7 (SVT) sont refusés par INSUFFISANT. T8 (hors base) est bien marqué « non vérifié ».

**Note : 4/5.** Le RAG fait ce qu'on attendait : plus de résolution improvisée quand l'exercice est dans la base. −1 : deux défauts vus pendant les tests, corrigés par une itération.

**Itération :** (1) Gemini écrivait les formules en LaTeX (`$\frac{n}{V}$`), illisible sur WhatsApp → règle « texte simple, jamais LaTeX » ajoutée au Rédacteur. (2) Pour « je n'ai jamais vu l'effet photoélectrique », le Rédacteur répondait « Aucune erreur, bravo », et le Chercheur répondait parfois INSUFFISANT → règle « demande de cours = jamais INSUFFISANT » dans le Chercheur et section « 📚 LE COURS EN BREF » dans le Rédacteur. Retest : cours sur le dipôle RC + exercice de la base ✅.

## S5-3 — Prompt webhook MVP ↔ Dify (prompt E3 adapté)

- **Outil :** Lovable (ou Bolt) · **Technique :** Prompt de génération d'interface avec spécification API

**Prompt :** [`dify/webhook/prompt-lovable.md`](../dify/webhook/prompt-lovable.md).

**Adaptations par rapport au modèle GreenSprint :** interface qui imite WhatsApp (notre canal cible) ; `inputs.query` et lecture de `data.outputs.text` / `data.outputs.message_erreur` (API workflow, deux sorties) ; timeout 15 s car deux appels LLM à la suite ; aucune image ni vidéo (contrainte data).

**Résultat :** *[pas encore exécuté — S4 reporté]*. En attendant, l'API est testée sans interface avec [`dify/webhook/test-api.sh`](../dify/webhook/test-api.sh).

---

## S5-4 — Test de cohérence de la base (prompt S2 de la bibliothèque)

- **Outil :** Dify → Test de récupération · **Technique :** Zero-Shot, 5 requêtes (directes, indirectes, hors-base)

**Résultat (28/09) :** R1–R4 ✅ en recherche sémantique : le bon exercice ou la bonne fiche arrive en 1re position (scores 0,45 à 0,68). R5 (hors base) non testé, crédits épuisés. Détail : [plan de tests](../dify/tests-rag.md).

**Note : 4/5.** La recherche sémantique retrouve même les requêtes indirectes (« je n'ai pas vu le condensateur » → Dipôle RC). −1 : en mode Économique (plan gratuit), `satellite altitude vitesse` renvoie l'exercice du proton : l'index par mots-clés ne comprend pas notre français. **Itération :** passer la base en Haute qualité avec l'embedding Gemini (gratuit) ; seuil de score désactivé, car 0,5 aurait écarté R3.

---

## S5-5 — RAG à deux recherches : base fixe programme + constantes (tutoriel S5)

- **Date :** 30/09/2026 · **Outil :** Dify (workflow « jang ») · **Technique :** RAG à deux recherches (base recherchée + base fixe lue en entier) ; débogage Chain-of-Thought sur la TRACE
- **Problème de départ (T8) :** un exercice hors base au programme (voiture, 2e loi de Newton) était refusé : « INSUFFISANT : niveau collège/seconde ». Le Chercheur devinait le programme.

**Débogage (prompt de la section 8 du tutoriel, adapté) :** « Tu es un expert des workflows Dify… Raisonne étape par étape et ne propose AUCUNE modification de prompt tant que les branchements n'ont pas été vérifiés. » avec : chaîne DÉBUT → RECUP_1 → CHERCHEUR, question T8, résultat attendu/obtenu, SORTIES de la TRACE.
→ Diagnostic : branchements corrects (la récupération renvoie JNG-PC-07, le plus proche) ; la cause est l'absence de référentiel du programme dans le contexte, donc le Chercheur juge le niveau « au jugé ».

**Prompt ajouté au Chercheur :** bloc « BLOC PROGRAMME » + 3 règles (voir [`dify/prompts-agents.md`](../dify/prompts-agents.md#bloc-programme-ajouté-au-chercheur-s5-v3-3009)). Base fixe d'une ligne, requête fixe en variable ENV, nœud MODÈLE Jinja.

**Résultat :** T8 ✅ (F = m·a = 2 000 N, erreur m·v repérée) ; T9 nouveau ✅ (c = 3,0×10⁸ m/s pris dans la base fixe, E = 3,97×10⁻¹⁹ J) ; non-régression T1, T6, T7 ✅. Publié en « S5 RAG v3 ».

**Critique :** 1er jet de la base fixe trop long (1 122 caractères → 2 morceaux) ; raccourci à 850 caractères pour rester en 1 morceau. La règle « jamais hors niveau » pourrait faire accepter trop large : T6 (météo) et T7 (SVT) vérifiés, toujours refusés.
**Itération :** si le programme officiel change, mettre à jour une seule ligne de la base fixe, sans toucher au prompt.

---

## S5-6 — Réponse illisible : ID non retrouvé par la recherche

- **Date :** 30/09/2026 · **Outil :** Dify + site Lovable · **Technique :** débogage sur la TRACE (prompt section 8 du tutoriel), puis correction par un nœud Code
- **Problème :** sur le site, `JNG-PC-01 : grtefcxcv` → « Je ne peux pas corriger ce message ». Dans Dify, la vraie raison était fausse : « JNG-PC-01 ne figure pas dans la base ».

**Localisation (TRACE) :** le 1er nœud en défaut est la **Récupération** : la recherche sémantique ne lit pas l'ID comme un mot-clé, et le mot sans sens l'égare (satellites, photon, alcools). Le Chercheur n'y est pour rien : il n'a jamais reçu JNG-PC-01.

**Essai 1 — recherche hybride :** échec (ID toujours absent, R3 dégradé). Annulé.
**Essai 2 — nœud Code EXTRAIRE_ID :** une expression régulière repère l'ID et la requête devient l'énoncé de référence → exercice retrouvé à coup sûr. Deux règles ajoutées au Chercheur (ID repéré, réponse illisible).

**Résultat :** T10 ✅ « ta réponse à JNG-PC-01 est illisible… » ; T1, T2, T6, T7 ✅. T8 a régressé puis a été corrigé en réécrivant la condition « programme » de l'étape 3. Publié en « S5 RAG v4 ».

**Critique :** le site Lovable affiche une phrase fixe au lieu de `message_erreur` : l'élève ne voit pas la raison. Chaque message est traité seul (« C'est ce que j'ai fais » n'a pas de contexte).
**Itération :** prompt Lovable L-ERR prêt (afficher `message_erreur` sans le mot INSUFFISANT), à lancer quand les crédits reviennent.

---

## S5+-1 — Tutoriel S5+ appliqué à Jàng (Phase 0, modules A à F)

- **Date :** 01/10/2026 · **Outil :** Claude (avec le tutoriel S5+ joint), Dify, VS Code · **Technique :** protocole imposé par le document (fiche projet → parcours → une étape à la fois)
- **Prompt de démarrage (§0.1, complété) :** « Voici le tutoriel GET409 S5+… applique-le à MON projet, pas à l'exemple Kayit. Équipe : Cheikh BOYE & Adama DIOP — Jàng ; HMW : [HMW S2] ; utilisateur : élèves de Terminale S des lycées de région ; agent : query → correction (`text`) ou refus (`message_erreur`) ; MVP : Lovable (dépublié) ; dépôt : jang-bac-helper ; macOS, VS Code oui ; objectif : tout. »

**Résultat :** [fiche projet et parcours](../07-s5plus/fiche-projet-et-parcours.md). Stack détectée : TanStack Start (SSR) → clé côté serveur, piste 1 Cloudflare. Module A déjà fait (Gemini Flash-Lite, clé de l'équipe). Module E : erreurs lisibles dans le chat. Module B : [T1–T6](../07-s5plus/tests-t1-t6.md) → **T3 en échec** (cours donné pour un ID seul) → 1 règle ajoutée au Chercheur → v5 publiée, T1–T6 + T8 + T10 réussis. Module F : scripts macOS Cloudflare, essai à blanc réussi. Module D : [3 propositions notées](../07-s5plus/module-d-fonctionnalites.md).

**Critique :** la limite « knowledge base request rate limit » du plan Dify gratuit fait échouer une série de tests enchaînés (2 recherches par correction) : risque pour la démo si plusieurs personnes testent en même temps.
**Itération :** espacer les tests de 15 s ; pour la soutenance, garder le Plan B prêt.
**Note : 4/5.**

---

## S5+-2 — Module D : « Vérifie mon similaire » (P-Idées → P-Spec → P-Dify → P-Code → P-Test)

- **Date :** 01/10/2026 · **Outil :** Claude, Dify, VS Code · **Technique :** prompts P-Idées / P-Spec / P-Dify / P-Code / P-Test du tutoriel S5+ §5.4
- **P-Idées :** « À partir de ma fiche projet, de mon HMW et de mon VPC, propose 3 fonctionnalités IA… note /5 sur les 5 critères… recommandation. » → vérification de l'exercice similaire (24/25), photo de la copie (17/25), bilan du soir (21/25). **Choix de l'équipe : la 1re.**
- **P-Spec / P-Dify / P-Code :** voir [module D](../07-s5plus/module-d-fonctionnalites.md) — sortie `mode` dans `EXTRAIRE_ID`, règle VÉRIFICATION dans le Chercheur et le Rédacteur, bouton « ✍️ J'ai fait l'exercice similaire » dans le chat.

**Résultat :** T7 ✅ (« TA VÉRIFICATION… Chapitre maîtrisé ! »). **T8 ❌ au 1er essai : erreur inventée** — l'élève avait écrit 0,02 (= n, juste), Jàng lui reprochait d'avoir oublié de diviser par M. Itération : comparaison étape par étape, « chaque valeur qui figure dans Reponse_similaire est juste ; une seule erreur » → T8 ✅. T1–T6 rejoués ✅. Publié en « S5+ v6 (similaire) ».

**Critique :** la vérification repose entièrement sur `Reponse_similaire` : la validation des corrigés par un professeur reste le prérequis avant un vrai pilote.
**Note : 4/5.**

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
