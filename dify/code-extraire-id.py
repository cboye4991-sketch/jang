import re

EXERCICES = {
    "JNG-PC-01": "JNG-PC-01 Solutions et pH des bases fortes : On dissout 2,0 g d'hydroxyde de sodium (NaOH) dans de l'eau pour obtenir 500 mL de",
    "JNG-PC-02": "JNG-PC-02 Acides forts : Une solution d'acide chlorhydrique a une concentration C = 1,0×10^-2 mol/L. Calculer son",
    "JNG-PC-03": "JNG-PC-03 Acides faibles, Ka et pKa : On prépare une solution d'acide éthanoïque CH3COOH de concentration C = 1,0×10^-2 mol/L.",
    "JNG-PC-04": "JNG-PC-04 Dosage acide faible / base forte : On dose Va = 20,0 mL d'une solution d'acide éthanoïque par une solution d'hydroxyde de",
    "JNG-PC-05": "JNG-PC-05 Cinétique chimique : Au cours d'une réaction totale, la concentration du réactif limitant A passe de 0,040",
    "JNG-PC-06": "JNG-PC-06 Alcools et oxydation ménagée : On réalise l'oxydation ménagée du butan-2-ol par une solution acidifiée de dichromate de",
    "JNG-PC-07": "JNG-PC-07 Lois de Newton (plan incliné) : Un solide de masse m = 0,50 kg, lâché sans vitesse initiale, glisse sans frottement sur",
    "JNG-PC-08": "JNG-PC-08 Mouvement dans le champ de pesanteur : Une bille est lancée horizontalement avec une vitesse v0 = 5,0 m/s depuis une hauteur h =",
    "JNG-PC-09": "JNG-PC-09 Gravitation et satellites : Un satellite décrit une orbite circulaire à l'altitude h = 800 km autour de la Terre.",
    "JNG-PC-10": "JNG-PC-10 Dipôle RC : Un condensateur de capacité C = 100 µF, initialement déchargé, est chargé à travers une",
    "JNG-PC-11": "JNG-PC-11 Particule dans un champ magnétique : Un proton pénètre avec une vitesse v = 1,0×10^6 m/s perpendiculairement à un champ",
    "JNG-PC-12": "JNG-PC-12 Effet photoélectrique : Une cellule au césium (travail d'extraction W0 = 1,9 eV) est éclairée par une lumière de",
    "JNG-PC-13": "JNG-PC-13 Radioactivité et décroissance : L'iode 131 a une période radioactive T = 8,0 jours. Un échantillon a une activité A0 =",
    "JNG-PC-14": "JNG-PC-14 Interférences lumineuses (fentes de Young) : Deux fentes distantes de a = 1,0 mm sont éclairées par une lumière monochromatique de"
}


def main(query: str) -> dict:
    # Repère un ID du type JNG-PC-01 (tolère « jng pc 1 », « JNG-PC 01 »…)
    m = re.search(r"JNG[\s_-]*PC[\s_-]*0*(\d{1,2})", query or "", re.IGNORECASE)
    # Mode « vérification » : l'élève renvoie sa réponse à l'EXERCICE SIMILAIRE (S5+, module D)
    mode = "similaire" if re.search(r"\bsimilaire\b", query or "", re.IGNORECASE) else "correction"
    if m:
        id_ex = "JNG-PC-%02d" % int(m.group(1))
        if id_ex in EXERCICES:
            # Requête = énoncé de référence : la recherche retrouve l'exercice
            # même si la réponse de l'élève est illisible ou très courte.
            return {"requete_recherche": EXERCICES[id_ex], "id_exercice": id_ex, "mode": mode}
        return {"requete_recherche": query, "id_exercice": id_ex + " (hors base)", "mode": mode}
    return {"requete_recherche": query, "id_exercice": "aucun", "mode": "correction"}
