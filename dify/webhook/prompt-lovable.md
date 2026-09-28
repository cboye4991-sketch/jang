# Webhook MVP ↔ Dify — prompt prêt pour la reprise de S4

> S4 a été volontairement reporté : il n'y a pas encore de MVP en ligne.
> Ce prompt est prêt à coller dans Lovable (ou Bolt) **une fois le MVP V1 créé**. Seule la clé API est à remplacer.
> En attendant, l'API se teste sans interface avec [`test-api.sh`](test-api.sh).

## Ce qu'il faut noter depuis Dify

| Élément | Valeur |
|---|---|
| URL API (identique pour tous) | `https://api.dify.ai/v1/workflows/run` |
| Workflow | `jang` |
| Variable d'entrée | `query` |
| Chemin de la réponse | `data.outputs.text` (correction) · `data.outputs.message_erreur` (refus) |
| Clé API | `app-…` — **à ne jamais committer sur GitHub** |

## Prompt à coller dans Lovable

```
Dans mon MVP Jàng, ajoute sur la page d'accueil une fenêtre de discussion
qui imite une conversation WhatsApp avec le correcteur Jàng.

INTERFACE À AJOUTER :
1. Une zone de messages style WhatsApp (bulles vertes #DCF8C6 pour l'élève,
   bulles blanches pour Jàng, fond #ECE5DD).
2. Un message d'accueil de Jàng : « Salut ! Envoie l'ID d'un exercice
   (ex. JNG-PC-01) suivi de ta réponse, je te dis où est ta première erreur. »
3. Un champ de texte avec placeholder :
   "JNG-PC-01 : ma réponse..."
4. Un bouton vert #25D366 "Envoyer à Jàng"
5. Un indicateur « Jàng écrit… » (3 points animés) pendant la requête
6. Un message d'erreur rouge si la requête échoue

CONNEXION WEBHOOK DIFY :
URL : https://api.dify.ai/v1/workflows/run
Méthode : POST
Headers :
  Authorization: Bearer [COLLER_LA_CLÉ_API_ICI]
  Content-Type: application/json
Body JSON :
  { "inputs": { "query": valeurDuChampTexte },
    "response_mode": "blocking",
    "user": "jang-" + Date.now() }

TRAITEMENT DE LA RÉPONSE :
- Succès : afficher response.data.outputs.text dans une bulle Jàng,
  en conservant les retours à la ligne et les emojis ✅ ❌ 💡 ➡️
- Si outputs.text est vide et outputs.message_erreur existe : afficher dans une bulle
  « Je ne peux pas corriger ce message : » suivi de message_erreur
  sans le mot INSUFFISANT
- Erreur réseau : "Jàng est indisponible pour le moment — réessaie dans une minute"
- Timeout (>15 s) : "La réponse prend trop de temps — réessaie"

STYLE : sobre, lisible sur un petit écran Android (360 px), responsive mobile,
aucune image lourde ni vidéo (nos utilisateurs ont peu de data).
```

## Pourquoi ces choix

- **Interface WhatsApp :** la cible finale de Jàng est WhatsApp (VPC, G4). Le MVP web sert de démonstrateur en attendant un vrai numéro WhatsApp Business.
- **Timeout à 15 s** au lieu de 10 s : deux appels LLM à la suite (Chercheur puis Rédacteur).
- **Clé API côté navigateur :** acceptable pour un prototype de cours, pas en production. Pour la version finale, passer par une fonction serveur (Lovable Cloud / Supabase Edge Function) — point repris dans la [note d'éthique](../../docs/note-ethique-rag.md).

## Vérifications après intégration

- [ ] La fenêtre Jàng apparaît sur la page d'accueil
- [ ] T1 du [plan de tests](../tests-rag.md) affiche la correction dans une bulle
- [ ] T6 (météo) affiche le message hors-base
- [ ] Aucune erreur dans la console (F12)
- [ ] Réponse vide ? regarder `response.data.outputs` dans la console (F12) : `text` ou `message_erreur`
