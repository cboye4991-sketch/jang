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
✅ Ce qui est juste : ton calcul de n = 0,050 mol est correct.
❌ L'erreur : tu as divisé par 500 alors que le volume doit être en litres.
💡 La bonne méthode : convertis toujours les mL en L avant C = n/V (500 mL = 0,500 L).
➡️ À toi : on dissout 0,80 g de NaOH pour obtenir 250 mL de solution. Calcule C puis le pH.
📚 Source : exercice JNG-PC-01 — corrigé Jàng (en attente de validation par un professeur)
```

## Question 2 — rappel de cours (« pas vu en classe »)

**Élève :** `Je n'ai jamais vu l'effet photoélectrique en classe`

```
📘 Effet photoélectrique en 5 lignes :
• La lumière est faite de photons d'énergie E = h·c/λ.
• Un électron sort seulement si E ≥ W0 (travail d'extraction), donc si λ ≤ λ0 = h·c/W0.
• Énergie cinétique maximale : Ec max = E − W0.
• 1 eV = 1,6×10⁻¹⁹ J — convertis avant de soustraire.
➡️ Essaie l'exercice JNG-PC-12 (cellule au césium, λ = 500 nm).
```

## Question 3 — hors base

**Élève :** `Quelle est la météo demain à Dakar ?`

```
Je ne dispose pas de cette information dans ma base. Jàng couvre pour l'instant la Physique-Chimie de Terminale S2 : envoie l'ID d'un exercice (ex. JNG-PC-01) suivi de ta réponse.
```

## Checklist Plan B

- [ ] Ce fichier ouvert dans un onglet avant la démo
- [ ] Captures des vrais tests T1, T5, T6 (dossier `05-test/captures/`) — à faire après le montage Dify
- [ ] Schéma `docs/architecture-v2.png` sur un 2e écran ou imprimé
- [ ] Partage de connexion téléphone prêt si le Wi-Fi de la salle tombe
