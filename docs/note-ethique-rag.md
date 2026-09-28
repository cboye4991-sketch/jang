# Note d'éthique IA — le système RAG de Jàng

> Livrable S6 (préparé en S5) · GET 409 · Équipe Cheikh BOYE & Adama DIOP · Septembre 2026
> Construite avec le prompt S4 « Rédiger la note d'éthique RAG » (Chain-of-Thought), adapté à Jàng. Une page.

**Le système :** l'élève envoie sa réponse à un exercice ; le workflow Dify « jang » (Chercheur → SI/SINON → Rédacteur) la compare à un corrigé de référence stocké dans la base `Jang_KB_v1` (14 exercices type Bac + 14 fiches de cours, Physique-Chimie Terminale S2) et renvoie la première erreur en 90 mots au maximum.

## 1. Qualité et biais des données

**Constat.** La base ne couvre qu'une matière, une série et un exercice par chapitre. Les exercices sont rédigés par l'équipe sur le modèle du Bac, pas tirés d'annales officielles, et leurs corrigés n'ont pas encore été relus par un professeur. Les élèves de L, de BFEM ou d'autres matières, ainsi que ceux qui rédigent autrement que le corrigé type, sont mal servis : une méthode juste mais différente risque d'être comptée fausse.
**Recommandation.** Faire valider chaque corrigé par un professeur de PC (colonne `Statut_validation`) avant toute ouverture à de vrais élèves. Ajouter pour chaque exercice les méthodes alternatives acceptées. Documenter publiquement le périmètre (fiche « Ce que Jàng ne couvre pas »).

## 2. Confidentialité et souveraineté

**Constat.** La base ne contient **aucune donnée personnelle** : seulement des énoncés et des corrigés. Mais chaque question d'élève transite par Dify Cloud et par le fournisseur du modèle (Google Gemini, hors Sénégal), avec un identifiant `user`. Les élèves visés ont 17 ans en moyenne : ce sont des mineurs. La loi sénégalaise n° 2008-12 sur les données personnelles et la CDP s'appliquent dès qu'on relie un message à un numéro WhatsApp. Enfin, la clé API est visible dans le code du prototype.
**Recommandation.** Identifiant `user` anonyme (jamais le numéro de téléphone) ; ne pas demander de nom ; informer l'élève et ses parents que les messages sont traités par une IA hébergée à l'étranger. Clé API dans une fonction serveur dès la version de production, jamais dans le dépôt GitHub.

## 3. Fiabilité et responsabilité

**Constat.** Même avec le RAG, le modèle peut mal lire un calcul ou juger fausse une réponse juste. Pour un élève qui révise seul, une mauvaise correction est pire que pas de correction (Chapeau Noir, R1). La responsabilité revient à l'équipe qui publie l'outil, pas à l'élève.
**Recommandation.** Le Rédacteur pointe une seule erreur, le Chercheur cite l'exercice source, et chaque correction rappelle « en cas de doute, demande à un professeur ». Refuser les questions hors programme au lieu d'improviser (sortie INSUFFISANT, tests T6/T7) et signaler « non vérifié » tout exercice hors base. Mesurer le taux d'erreurs de correction sur un jeu de réponses d'élèves avant toute diffusion (hypothèse H3).

## 4. Impact socio-économique

**Constat.** Jàng est gratuit et léger en data : il réduit l'écart avec les élèves de Dakar qui paient des cours particuliers. Il peut aussi concurrencer les répétiteurs locaux, souvent des étudiants qui vivent de ces cours, et pousser l'État à compter sur un robot plutôt que d'affecter des professeurs.
**Recommandation.** Positionner Jàng comme un complément, pas un remplaçant : impliquer les répétiteurs et professeurs comme validateurs rémunérés ou bénévoles des corrigés. Garder l'objectif pédagogique de l'autonomie : Jàng réussit si l'élève n'en a plus besoin le jour du Bac.

---
*Engagement de l'équipe :* aucune démonstration auprès de vrais élèves tant que les corrigés ne sont pas validés par un professeur.
