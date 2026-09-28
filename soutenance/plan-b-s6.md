# Plan B — démo S6 en cas de panne API

> Obligatoire selon le syllabus (prompt S6 de la bibliothèque S5, adapté à Jàng).
> Réponses simulées **cohérentes avec notre CSV** (`dify/knowledge/jang_exercices_pc_ts2.csv`), à copier-coller ou à montrer en capture si Dify ne répond pas.
> Règle d'honnêteté : annoncer au jury qu'il s'agit de réponses préenregistrées.
> ⚠️ Les trois réponses ci-dessous sont des **modèles rédigés avant le montage Dify**. Après les tests T1, T5 et T6, remplacez-les par les sorties réelles du workflow (copier-coller) : le message au jury ne sera vrai qu'à cette condition.

## Message à lire si le service tombe (≈ 15 s)

« Le service Dify ne répond pas en ce moment, ce qui arrive avec les offres gratuites. Nous passons à des réponses enregistrées lors de nos tests : ce sont les sorties réelles de notre workflow sur les mêmes questions. L'architecture reste celle du schéma affiché. »

## Question 1 — correction avec erreur

**Élève :** `JNG-PC-01 : n = 2/40 = 0,05 mol ; C = 0,05/500 = 0,0001 mol/L`

```
―――――――――
📘 JÀNG — TA CORRECTION
Chimie · Solutions et pH des bases fortes
―――――――――
✅ CE QUI EST JUSTE
Ton calcul de n = 2,0/40 = 0,050 mol est correct.
―――――――――
❌ TA PREMIÈRE ERREUR
Tu as divisé par 500 : le volume doit être en litres, pas en mL.
―――――――――
💡 LA MÉTHODE
Convertis toujours avant C = n/V : 500 mL = 0,500 L. Refais ton calcul.
―――――――――
➡️ À TOI
On dissout 0,80 g de NaOH pour obtenir 250 mL de solution. Calcule C puis le pH.
―――――――――
⚠️ Jàng peut se tromper : en cas de doute, demande à un professeur.
```

## Question 2 — exercice juste

**Élève :** `JNG-PC-02 : pH = 2 puis pH = 3 après dilution`

```
―――――――――
📘 JÀNG — TA CORRECTION
Chimie · Acides forts
―――――――――
✅ CE QUI EST JUSTE
pH = −log C = 2,0, puis 3,0 après dilution par 10.
―――――――――
❌ TA PREMIÈRE ERREUR
Aucune erreur, bravo 👏 Résultat : pH = 2,0 puis 3,0.
―――――――――
➡️ À TOI
Calcule le pH d'une solution d'acide nitrique à 5,0×10⁻³ mol/L.
―――――――――
⚠️ Jàng peut se tromper : en cas de doute, demande à un professeur.
```

## Question 3 — hors base

**Élève :** `Quelle est la météo demain à Dakar ?`

```
INSUFFISANT : la question ne relève pas du programme de Terminale S.
```
*(sortie `message_erreur` du workflow — dans le MVP, affichée sous la forme « Je ne peux pas corriger ce message : la question ne relève pas du programme de Terminale S. »)*

## Checklist Plan B

- [ ] Ce fichier ouvert dans un onglet avant la démo
- [ ] Captures des vrais tests T1, T4, T6 (dossier `05-test/captures/`) — à faire après le montage Dify
- [ ] Schéma `docs/architecture-v2.png` sur un 2e écran ou imprimé
- [ ] Partage de connexion téléphone prêt si le Wi-Fi de la salle tombe
