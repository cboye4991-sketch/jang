# HMW Définitif — Jàng

> Livrable S2 — GET 409 Atelier IA · Outil 3/3 (Décision)
> Construit avec le prompt P-HMW à partir du HMW draft S1, des [6 Chapeaux](chapeaux-bono.md) et du FIT Check du [VPC](vpc.md).

## HMW Draft S1

« Comment pourrions-nous permettre aux élèves de Terminale vivant en région de savoir si leurs exercices sont justes — et pourquoi — avec un simple téléphone et peu de data ? »

## HMW Définitif S2

> **« Comment pourrions-nous permettre aux élèves de Terminale scientifique des lycées de région, qui révisent seuls faute de professeur, de recevoir le soir même une explication fiable de leurs erreurs sur les exercices d'annales — depuis le téléphone qu'ils ont déjà et sans dépasser leur petit forfait data — afin d'aborder le Bac en sachant se corriger seuls ? »**

---

## Ce qui change entre S1 et S2

| Élément du HMW | Draft S1 | Définitif S2 | Pourquoi ce changement |
|---|---|---|---|
| **Qui** | « élèves de Terminale vivant en région » | « élèves de Terminale **scientifique** des lycées de région, **qui révisent seuls faute de professeur** » | Le manque de professeur touche surtout les matières scientifiques (Chapeau Blanc) ; on nomme la cause du problème, pas seulement le lieu. |
| **Le problème** | « savoir si leurs exercices sont justes — et pourquoi » | « recevoir […] une explication **fiable** de leurs erreurs » | Le Chapeau Noir (R1) montre qu'une correction fausse est pire que pas de correction : la **fiabilité** devient une exigence du problème. |
| **Quand** | *(absent)* | « **le soir même** » | Aminata révise le soir après les tâches (carte d'empathie) : un retour qui arrive le lendemain ne l'aide pas. |
| **Sur quoi** | « leurs exercices » | « les exercices **d'annales** » | Ancre le HMW dans le vrai matériau de révision observé (PDF d'annales du groupe WhatsApp) et dans le Bac sénégalais. |
| **Contraintes** | « avec un simple téléphone et peu de data » | « depuis **le téléphone qu'ils ont déjà** et **sans dépasser leur petit forfait data** » | Chapeau Noir R2 : on exclut l'achat d'un appareil et on rend la contrainte data vérifiable (forfait du jour). |
| **Finalité** | *(absente)* | « afin d'aborder le Bac **en sachant se corriger seuls** » | Le gain profond du VPC (G2, G5) : l'autonomie et la confiance, pas une dépendance à l'outil. Évite aussi le risque R3 (recopier sans comprendre). |

**En résumé :** le draft S1 posait la bonne question mais restait ouvert sur *qui*, *quand* et *pour quoi faire*. Le HMW S2 garde le cœur (savoir pourquoi on se trompe) et y ajoute les trois choses apprises en S2 : la cause (absence de professeur), l'exigence de fiabilité et la finalité d'autonomie.

---

## Les 3 versions étudiées (sortie P-HMW)

### Version A — trop précise

« Comment pourrions-nous aider Aminata, élève de Terminale S2 à Kaffrine, à faire corriger ses exercices de physique-chimie sur WhatsApp chaque soir ? »
- Plus précise car : persona, matière et moment explicites.
- Risque Chapeau Noir intégré : aucun (ni fiabilité, ni data).
- Évaluation : **trop précise** — une seule élève, une seule ville, et elle **contient déjà la solution** (« sur WhatsApp ») → rejetée.

### Version B — trop large

« Comment pourrions-nous améliorer la réussite au Bac des élèves des régions du Sénégal ? »
- Plus précise car : elle ne l'est pas ; elle vise l'impact final.
- Risque Chapeau Noir intégré : aucun.
- Évaluation : **trop large** — « sauver le monde », n'importe quelle équipe pourrait l'écrire sans contexte → rejetée.

### Version C — bien calibrée ✅

L'énoncé retenu ci-dessus.
- Plus précise car : elle nomme le public (séries scientifiques, sans professeur), le moment (le soir), le matériau (annales) et la finalité (se corriger seuls).
- Risques Chapeau Noir intégrés : R1 (fiabilité) et R2 (data / téléphone existant).
- Évaluation : **bien calibrée** — précise sur le problème, ouverte sur la solution.

---

## Validation — critères du cours (slide « Choix définitif » + P-HMW)

| Critère | Résultat | Justification |
|---|---|---|
| Désigne un utilisateur réel au Sénégal | ✅ | Élèves de Terminale scientifique des lycées de région (persona : Aminata, Kaffrine) |
| Décrit une vraie frustration, pas une hypothèse | ✅ | Verbatim S1 : « Il n'y a personne pour me corriger. » |
| Assez large pour plusieurs solutions | ✅ | Voir ci-dessous : au moins 3 solutions différentes possibles |
| Assez précis pour ne pas « sauver le monde » | ✅ | Un public, un moment, un matériau, une contrainte |
| Ne contient pas de solution | ✅ | Aucun canal ni outil imposé (ni WhatsApp, ni application, ni IA) |
| N'est pas formulable par n'importe quelle équipe | ✅ | Contexte local : régions, absence de professeur, annales, forfait data |
| Intègre le risque du Chapeau Noir | ✅ | Fiabilité (R1) et data (R2) |

**3 solutions différentes qu'il autorise :**
1. Un correcteur conversationnel par messagerie (notre piste — Jàng).
2. Un réseau d'étudiants bénévoles qui corrigent des photos de copies le soir.
3. Des fiches d'annales « auto-correctrices » par SMS avec erreurs fréquentes et explications (sans internet).

---

## Pourquoi ce HMW ?

- **Ancrage :** Aminata, 17 ans, Terminale S2 à Kaffrine, révise seule la physique-chimie le soir sur un Android d'entrée de gamme avec un forfait acheté au jour le jour.
- **Actionnable :** il ouvre au moins trois pistes (correcteur conversationnel, tutorat bénévole, fiches SMS) sans en imposer une.
- **Résiste au Chapeau Noir :** il pose la fiabilité de la correction et la contrainte data comme conditions du succès, pas comme détails techniques.

## Ce que ce HMW guide en S3

La fonctionnalité prioritaire du MVP est la **boucle de correction fiable** : l'élève envoie sa réponse à un exercice d'annale de physique-chimie (S2), reçoit le soir même l'explication de sa première erreur, vérifiée contre un corrigé de référence, puis refait seule un exercice similaire.

**Critère de réussite (démo S6) :** un élève qui s'est trompé réussit l'exercice similaire sans aide, et la correction complète coûte moins de 100 Ko de data.
