# Jàng — Fiches « pas vu en classe » · Physique-Chimie Terminale S2

> Base de connaissances Jang_KB_v1 · Septembre 2026
> Une fiche par chapitre, 5 lignes maximum : ce qu'il faut savoir avant de faire l'exercice.
> Rédigé par l'équipe Jàng (Cheikh BOYE, Adama DIOP) à partir du programme de PC Terminale S. **Statut : à faire valider par un professeur.**
> Exercices associés : voir `jang_exercices_pc_ts2.csv` (colonne ID).

## Solutions et pH des bases fortes (JNG-PC-01)
- Quantité de matière : n = m/M (m en g, M en g/mol).
- Concentration molaire : C = n/V avec **V en litres** (500 mL = 0,500 L).
- Base forte (NaOH, KOH) : [HO⁻] = C, donc pH = 14 + log C à 25 °C.
- Produit ionique de l'eau : Ke = [H₃O⁺]·[HO⁻] = 1,0×10⁻¹⁴ à 25 °C.
- Piège : oublier de convertir les mL en L.

## Acides forts (JNG-PC-02)
- Un acide fort (HCl, HNO₃) réagit totalement avec l'eau : [H₃O⁺] = C.
- pH = −log C, valable pour 10⁻⁶ < C < 10⁻¹ mol/L.
- Diluer 10 fois divise C par 10 et **augmente le pH de 1**.
- Le pH n'est jamais multiplié ni divisé par 10.
- Piège : appliquer cette formule à un acide faible.

## Acides faibles, Ka et pKa (JNG-PC-03)
- Un acide faible ne réagit que partiellement avec l'eau : couple AH/A⁻.
- Ka = [A⁻]·[H₃O⁺]/[AH] et pKa = −log Ka. Plus le pKa est petit, plus l'acide est fort.
- Acide faiblement dissocié : pH ≈ ½(pKa − log C).
- Vérifier ensuite que pH > −log C (sinon l'approximation est fausse).
- pH = pKa + log([A⁻]/[AH]).

## Dosage acide faible / base forte (JNG-PC-04)
- À l'équivalence, les réactifs ont été mélangés dans les proportions stœchiométriques : Ca·Va = Cb·VbE.
- Le point d'équivalence se repère par la méthode des tangentes parallèles ou la dérivée dpH/dV.
- À la demi-équivalence (Vb = VbE/2) : pH = pKa.
- Le pH à l'équivalence est supérieur à 7 (base conjuguée faible en solution).
- Piège : inverser Va et VbE dans la formule.

## Cinétique chimique (JNG-PC-05)
- Vitesse moyenne de disparition d'un réactif : v = −Δ[A]/Δt (toujours positive).
- Vitesse instantanée : v = −d[A]/dt = opposé de la pente de la tangente à la courbe [A] = f(t).
- Temps de demi-réaction t½ : durée pour que l'avancement atteigne la moitié de sa valeur finale.
- Facteurs cinétiques : température, concentration des réactifs, catalyseur.
- La vitesse diminue au cours du temps car les réactifs s'épuisent.

## Alcools et oxydation ménagée (JNG-PC-06)
- Classe d'un alcool = nombre d'atomes de carbone liés au carbone fonctionnel (primaire, secondaire, tertiaire).
- Primaire → aldéhyde (oxydant en défaut) → acide carboxylique (oxydant en excès).
- Secondaire → cétone. Tertiaire → pas d'oxydation ménagée.
- Tests : DNPH positive pour aldéhydes et cétones ; liqueur de Fehling et réactif de Tollens positifs pour les aldéhydes seulement.
- Oxydant usuel : dichromate de potassium ou permanganate en milieu acide.

## Lois de Newton — plan incliné (JNG-PC-07)
- Faire le bilan des forces (poids, réaction, frottements) dans un référentiel galiléen.
- 2e loi de Newton : ΣF = m·a, puis projeter sur l'axe du mouvement.
- Sans frottement sur un plan incliné d'angle α : a = g·sin α (ne dépend pas de la masse).
- Mouvement rectiligne uniformément accéléré : v² − v0² = 2·a·d ; x = ½·a·t² + v0·t.
- Piège : projeter avec cos α au lieu de sin α sur l'axe de la pente.

## Mouvement dans le champ de pesanteur (JNG-PC-08)
- Seul le poids agit : a = g (vertical, vers le bas).
- Lancer horizontal : x = v0·t (mouvement uniforme) et y = ½·g·t² (chute, axe vers le bas).
- Durée de chute depuis la hauteur h : t = √(2h/g).
- Portée : x = v0·t. Équation de la trajectoire : y = g·x²/(2·v0²) (parabole).
- Piège : oublier le facteur ½.

## Gravitation et satellites (JNG-PC-09)
- Force de gravitation : F = G·M·m/r², où r = R + h (distance au centre de la Terre).
- Au sol : g0 = G·M/R², donc G·M = g0·R².
- Orbite circulaire : mouvement uniforme, v = √(g0·R²/r).
- Période : T = 2π·r/v. 3e loi de Kepler : T²/r³ = constante.
- Piège : prendre r = h ou oublier de convertir les km en m.

## Dipôle RC (JNG-PC-10)
- Charge : uC(t) = E(1 − e^(−t/τ)) ; décharge : uC(t) = E·e^(−t/τ).
- Constante de temps : τ = R·C (en secondes si R en Ω et C en F).
- À t = τ, le condensateur est chargé à 63 % (ou déchargé à 37 %).
- Charge ou décharge pratiquement terminée au bout de 5τ.
- Piège : ne pas convertir µF → F (×10⁻⁶) et kΩ → Ω (×10³).

## Particule dans un champ magnétique (JNG-PC-11)
- Force de Lorentz : F = q·v∧B, perpendiculaire à la vitesse et au champ.
- Elle ne travaille pas : la valeur de la vitesse reste constante.
- Si v est perpendiculaire à B : mouvement circulaire uniforme de rayon R = m·v/(|q|·B).
- Application : spectrographe de masse, cyclotron.
- Piège : erreurs de puissances de 10 sur m et q.

## Effet photoélectrique (JNG-PC-12)
- La lumière est formée de photons d'énergie E = h·ν = h·c/λ.
- Émission d'électrons seulement si E ≥ W0 (travail d'extraction), soit λ ≤ λ0 = h·c/W0.
- Énergie cinétique maximale des électrons : Ec max = E − W0.
- Conversion : 1 eV = 1,6×10⁻¹⁹ J.
- Piège : soustraire des joules et des eV, ou oublier de convertir les nm en m.

## Radioactivité et décroissance (JNG-PC-13)
- Loi de décroissance : N(t) = N0·e^(−λt) et A(t) = A0·e^(−λt).
- Période (demi-vie) T : durée au bout de laquelle la moitié des noyaux s'est désintégrée ; λ = ln2/T.
- Après n périodes, il reste N0/2ⁿ noyaux.
- L'activité A = λ·N s'exprime en becquerels (Bq).
- Piège : diviser par n au lieu de 2ⁿ.

## Interférences lumineuses — fentes de Young (JNG-PC-14)
- Deux sources cohérentes produisent des franges brillantes et sombres alternées.
- Différence de marche : δ = a·x/D.
- Interfrange : i = λ·D/a (distance entre deux franges brillantes consécutives).
- Frange brillante si δ = k·λ ; frange sombre si δ = (k + ½)·λ.
- Piège : ne pas tout convertir en mètres avant le calcul.

## Ce que Jàng ne couvre pas encore
- Seul le programme de **Physique-Chimie de Terminale S2** est couvert (14 chapitres, 1 exercice chacun).
- Pas de mathématiques, pas de SVT, pas de séries L, pas de sujets de BFEM.
- Pour tout autre sujet, Jàng doit répondre qu'il ne dispose pas de l'information.
