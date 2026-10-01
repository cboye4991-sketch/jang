# S5+ — Cinq fonctionnalités côté application (01/10/2026)

> Choisies par l'équipe après « Vérifie mon similaire » (module D) : **indices progressifs, Bac blanc chronométré, réponse vocale, Défi WhatsApp**.
> Code : `src/components/ChatJang.tsx`, `src/lib/voix.ts`, `src/lib/defi.ts`, `src/lib/exercices-bac.ts`, `src/routes/exercices.tsx` (dépôt `jang-bac-helper`). Dify : version « S5+ v7 (indices) ».

| Fonctionnalité | Pour Aminata | Pattern (catalogue §5.2) | Dify | Application | Data |
|---|---|---|---|---|---|
| **💡 Indices progressifs** | Bloquée avant même de répondre : 3 coups de pouce gradués au lieu de la solution | 4 Garde-fou RAG + 6 humain dans la boucle (elle décide quand demander) | `EXTRAIRE_ID` : mode `indice` + sortie `niveau` (1 à 3) ; Chercheur : indice dosé tiré de `Corrige_reference` ; Rédacteur : « 📘 JÀNG — INDICE N/3 » | bouton « 💡 Indice N/3 » (actif dès qu'un ID est tapé, désactivé après 3 et pendant un Bac blanc) | ≈ 0,5 Ko |
| **🎲 Bac blanc · 15 min** | S'entraîner aux conditions du jour J : exercice imposé, temps limité, sans indice | 10 (lot) adapté : tirage + chrono | aucune modification (correction habituelle) | tirage parmi les 14 exercices de la base (énoncé + données), compte à rebours dans l'en-tête, « ⏱ Bac blanc terminé en X min » avant la correction | ≈ 1 Ko |
| **🔊 Réponse vocale** | Écouter sa correction le soir, yeux fatigués, ou en faisant autre chose | 2 Lecture à voix haute | aucune | bouton 🔊 / ⏹ sous chaque réponse ; texte rendu prononçable (émojis retirés, « m/s² » → « mètres par seconde carrée », « 10^-3 » → « dix puissance moins 3 », « = » → « égale ») | **0** (voix du téléphone) |
| **🎤 Note vocale** (ajoutée à la demande de l'équipe) | Répondre en parlant quand taper des formules au téléphone est pénible | 1 Entrée vocale + 6 humain dans la boucle | aucune | bouton « 🎤 Vocal » : dictée du navigateur (français), conversion en notation (« 0 virgule 05 sur 500 » → `0,05/500`, « mètres par seconde au carré » → `m/s²`, « fois 10 puissance moins 2 » → `×10^-2`, « JNG PC sept » → `JNG-PC-07`) ; le texte s'écrit dans la zone de saisie, l'élève relit et envoie | quelques Ko (texte seulement, aucun fichier audio) |
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
| T15 | Note vocale (site, reconnaissance simulée) : « JNG PC 7 a égale g fois sinus 30 égale 4 virgule 9 mètres par seconde au carré » | `JNG-PC-07 : a = g × sin 30 = 4,9 m/s²` dans la saisie, « Relis ta réponse… », rien d'envoyé | ✅ |
| T1–T7 | rejoués après v7 | inchangés | ✅ après la règle « DEMANDE DE SOLUTION » (T5 avait régressé) — [tests-t1-t6.md](tests-t1-t6.md) |

## Risques éthiques et garde-fous

| Fonctionnalité | Risque | Garde-fou |
|---|---|---|
| Indices | donner la solution par petits morceaux (dépendance) | 3 niveaux maximum, jamais le résultat final ; indices désactivés pendant le Bac blanc |
| Bac blanc | stress, sentiment d'échec | message neutre sur le temps, correction habituelle bienveillante |
| Réponse vocale | exclusion des élèves qui préfèrent le wolof | voix française uniquement, annoncée comme telle ; aucune voix wolof promise sans validation par un locuteur |
| Note vocale | voix envoyée à un tiers ; mauvaise transcription d'une valeur ; exclusion des élèves qui parlent wolof | sur Chrome Android la reconnaissance passe par Google (signalé) mais aucun audio n'est envoyé à Jàng ni stocké ; l'élève relit toujours avant d'envoyer ; français seulement, le clavier reste disponible |
| Défi WhatsApp | diffusion de données personnelles | message sans nom ni résultat chiffré, envoyé par l'élève elle-même (aucun envoi automatique), aucun numéro collecté |
