#coding utf-8

import csv

# PRÉPARATION BASIQUE DE LA LECTURE DU FICHIER CSV QUI RÉPERTORIE LES ARBRES PUBLICS DE MONTRÉAL ET
# OÙ LES COORDONNÉES DE LATITUDE ET LONGITUDE ONT ÉTÉ AJOUTÉES

fichier = "arbresMTLconsolideEDM5240.csv"
nouveaucsv = "arbresremarquablesMTL-EDM5240.csv"
f1 = open(fichier)
lignes = csv.reader(f1)
next(lignes)

# À L'AIDE D'UNE BOUCLE, ON DÉFINIT UNE VARIABLE "rema" QUI CIBLE LA VALEUR DE LA COLONNE [18] DE CHAQUE LIGNE DU CSV.
# CETTE COLONNE CONTIENT LA MENTION OU NON DE «REMARQUABILITÉ».

for arbre in lignes:
    rema = str.strip(arbre[18])
    
    # SI "rema" ÉQUIVAUT À 'O' (OUI), ALORS NOTRE LIGNE IDENTIFIE UN ARBRE REMARQUABLE ET EST DÉFINIE PAR LA VARIABLE "mtl2"
    if "O" in rema:
        mtl2 = arbre
        
        # AFIN DE SUIVRE LA PROGRESSION DE L'IDENTIFICATION DES ARBRES REMARQUABLES, ON DEMANDE D'IMPRIMER LES VALEURS RETENUES.
        print(mtl2)
        
        # J'ÉCRIS LES INFORMATIONS DES ARBRES REMARQUABLES ("mtl2") DANS DANS UN NOUVEAU FICHIER CSV ("arbresremarquablesMTL-EDM5240.csv").
        écrire = open(nouveaucsv,"a")
        pouet = csv.writer(écrire)
        pouet.writerow(mtl2)
    
    # POUR TOUS LES ARBRES QUI NE SONT PAS REMARQUABLES, ON DEMANDE À PYTHON DE PASSER SON TOUR ET DE RESTER INACTIF.
    else:
        pass
