# S5+ — Quatre fonctionnalités côté application (01/10/2026)

> Choisies par l'équipe après « Vérifie mon similaire » (module D) : **indices progressifs, Bac blanc chronométré, réponse vocale, Défi WhatsApp**.
> Code : `src/components/ChatJang.tsx`, `src/lib/voix.ts`, `src/lib/defi.ts`, `src/lib/exercices-bac.ts`, `src/routes/exercices.tsx` (dépôt `jang-bac-helper`). Dify : version « S5+ v7 (indices) ».

| Fonctionnalité | Pour Aminata | Pattern (catalogue §5.2) | Dify | Application | Data |
|---|---|---|---|---|---|
| **💡 Indices progressifs** | Bloquée avant même de répondre : 3 coups de pouce gradués au lieu de la solution | 4 Garde-fou RAG + 6 humain dans la boucle (elle décide quand demander) | `EXTRAIRE_ID` : mode `indice` + sortie `niveau` (1 à 3) ; Chercheur : indice dosé tiré de `Corrige_reference` ; Rédacteur : « 📘 JÀNG — INDICE N/3 » | bouton « 💡 Indice N/3 » (actif dès qu'un ID est tapé, désactivé après 3 et pendant un Bac blanc) | ≈ 0,5 Ko |
| **🎲 Bac blanc · 15 min** | S'entraîner aux conditions du jour J : exercice imposé, temps limité, sans indice | 10 (lot) adapté : tirage + chrono | aucune modification (correction habituelle) | tirage parmi les 14 exercices de la base (énoncé + données), compte à rebours dans l'en-tête, « ⏱ Bac blanc terminé en X min » avant la correction | ≈ 1 Ko |
| **🔊 Réponse vocale** | Écouter sa correction le soir, yeux fatigués, ou en faisant autre chose | 2 Lecture à voix haute | aucune | bouton 🔊 / ⏹ sous chaque réponse ; texte rendu prononçable (émojis retirés, « m/s² » → « mètres par seconde carrée », « 10^-3 » → « dix puissance moins 3 », « = » → « égale ») | **0** (voix du téléphone) |
| **📲 Défier un camarade** | Réviser à plusieurs, comme dans le groupe WhatsApp de la classe (G4) | 5 Sortie actionnable | aucune | lien `wa.me` pré-rempli que l'élève envoie elle-même ; le lien `…/exercices/?ex=JNG-PC-07` ouvre Jàng avec l'exercice présenté et la saisie prête | négligeable |

## Indices progressifs — règle ajoutée au Chercheur (v7)

```
- MODE INDICE (prioritaire sur la règle « ID sans réponse ») : si le mode du message est « indice »,
  l'élève n'a pas encore répondu et demande l'indice {{niveau}} sur 3 de l'exercice {{id_exercice}}.
  Ce n'est jamais INSUFFISANT si l'ID est dans la base. […] NOTION À REVOIR : l'indice, tiré de
  Corrige_reference et dosé selon le niveau — niveau 1 : seulement la loi, la relation ou la grandeur
  à utiliser, sans formule ni valeur ; niveau 2 : la formule littérale à appliquer, sans valeur
  numérique ; niveau 3 : la première étape du calcul avec les valeurs de l'énoncé, et rien au-delà.
  Ne donne JAMAIS Resultat_final ni l'étape finale. EXERCICE SIMILAIRE : « Aucun — demande d'indice ».
```

Rédacteur : « CAS INDICE » (titre « 📘 JÀNG — INDICE N/3 », une seule section 💡 INDICE, ➡️ « Essaie maintenant, puis envoie ta réponse : JNG-PC-xx : … ou demande l'indice suivant », pas de ✅/❌).

## Tests

| # | Entrée / action | Attendu | Résultat 01/10 |
|---|---|---|---|
| T9 | `JNG-PC-07 · indice 1` | la loi à utiliser, sans formule | ✅ « bilan des forces… 2e loi de Newton… projetant sur l'axe » |
| T10 | `JNG-PC-07 · indice 2` | la formule littérale, sans valeur | ✅ « a = g × sin alpha … v² = 2 × a × d » |
| T11 | `JNG-PC-07 · indice 3` | 1re étape chiffrée, pas le résultat | ✅ « a = 9,8 × sin(30°) » — 4,9 m/s² non donné |
| T11b | `JNG-PC-09 · indice 1` | ID réel dans ➡️ À TOI | ❌ 1er essai « [ID] : … » affiché tel quel → précision du Rédacteur → ✅ « JNG-PC-09 : … » |
| T12 | Bac blanc (site) | chrono 15:00, saisie pré-remplie, bouton désactivé, temps affiché à l'envoi, chrono retiré | ✅ (test automatisé du site statique) |
| T13 | Défi (site) | lien `wa.me` avec l'URL `?ex=` ; ouverture du lien → exercice présenté + saisie `JNG-PC-09 : ` | ✅ |
| T14 | Réponse vocale (site) | 🔊 sous les réponses longues, ⏹ pour arrêter ; texte prononçable | ✅ texte vérifié ; voix réelle à écouter sur téléphone |
| T1–T7 | rejoués après v7 | inchangés | ✅ après la règle « DEMANDE DE SOLUTION » (T5 avait régressé) — [tests-t1-t6.md](tests-t1-t6.md) |

## Risques éthiques et garde-fous

| Fonctionnalité | Risque | Garde-fou |
|---|---|---|
| Indices | donner la solution par petits morceaux (dépendance) | 3 niveaux maximum, jamais le résultat final ; indices désactivés pendant le Bac blanc |
| Bac blanc | stress, sentiment d'échec | message neutre sur le temps, correction habituelle bienveillante |
| Réponse vocale | exclusion des élèves qui préfèrent le wolof | voix française uniquement, annoncée comme telle ; aucune voix wolof promise sans validation par un locuteur |
| Défi WhatsApp | diffusion de données personnelles | message sans nom ni résultat chiffré, envoyé par l'élève elle-même (aucun envoi automatique), aucun numéro collecté |
