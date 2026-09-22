# Fonctionnalités du MVP — Jàng

## Parcours utilisateur
1. L'élève envoie « Salut » au numéro WhatsApp de Jàng.
2. Le bot demande sa série (S1, S2, L…) et la matière.
3. Chaque jour, le bot envoie un exercice tiré des annales du Bac sénégalais.
4. L'élève répond (texte ou photo de sa copie).
5. Le bot corrige étape par étape : ce qui est juste, où est l'erreur, la bonne méthode.
6. Le bot propose un exercice similaire pour vérifier la compréhension.

## Fonctionnalités prioritaires
- [ ] Banque d'exercices (Google Sheets) classés par série, matière, chapitre
- [ ] Correction guidée par un prompt chain-of-thought
- [ ] Messages courts (économie de data)
- [ ] Suivi simple de progression (exercices réussis / ratés)

## Outils envisagés (no-code)
- Typebot ou Landbot connecté à WhatsApp
- Google Sheets pour les exercices et le suivi
- Claude comme moteur de correction

## Prompt du bot correcteur (brouillon)

```
# RÔLE
Tu es un professeur de [MATIÈRE] bienveillant qui prépare des élèves sénégalais au Bac [SÉRIE].

## EXERCICE
[ÉNONCÉ]

## RÉPONSE DE L'ÉLÈVE
[RÉPONSE]

## TÂCHE
Réfléchis étape par étape :
1. Résous l'exercice toi-même.
2. Compare avec la réponse de l'élève, étape par étape.
3. Identifie la première erreur et explique pourquoi c'est une erreur.

## FORMAT DE SORTIE STRICT (message WhatsApp, 6 lignes maximum)
✅ Ce qui est juste : ...
❌ L'erreur : ...
💡 La bonne méthode : ...
➡️ Essaie maintenant : [exercice similaire court]
```
