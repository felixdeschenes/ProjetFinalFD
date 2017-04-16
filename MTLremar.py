#coding utf-8

import csv

fichier = "arbresMTLconsolideEDM5240.csv"
nouveaucsv = "arbresremarquablesMTL-EDM5240.csv"
f1 = open(fichier)
lignes = csv.reader(f1)
next(lignes)

listerema = [ ]

for arbre in lignes:
    rema = str.strip(arbre[18])
    if "O" in rema:
        mtl2 = arbre
        print(mtl2)
        écrire = open(nouveaucsv,"a")
        pouet = csv.writer(écrire)
        pouet.writerow(mtl2)
    else:
        pass
 
