#coding utf-8

# La procédure de conversion des données de projection MTM zone 8 en coordonnées de longitude et de latitude
# a été trouvée sur ce site: https://gis.stackexchange.com/questions/78838/how-to-convert-projected-coordinates-to-lat-lon-using-python


# IMPORTATION DES FONCTIONS NÉCESSAIRES
import csv
from pyproj import Proj, transform

# PRÉPARATION BASIQUE DE LA LECTURE DU FICHIER CSV QUI RÉPERTORIE LES ARBRES PUBLICS DE MONTRÉAL
fichier = "tousarbres2.csv"
nouveaucsv = "nouveau.csv"
f1 = open(fichier)
lignes = csv.reader(f1)
next(lignes)

# BOUCLE QUI DÉFINIT LES VARIABLES EN FONCTION DE LA VALEUR DE PROJECTION QUI APPARAIT DANS LES COLONNES 8 ET 9 DE CHAQUE LIGNE (CHAQUE ARBRE).
for arbre in lignes:
    coordXarbres = str.strip(arbre[8])
    coordYarbres = str.strip(arbre[9])

    # AVEC LES FONCTIONS PROJ ET TRANSFORM DU MODULE PYPROJ, J'AJOUTE LE CODE DES DONNÉES DE PROJECTION MTM ZONE 8 EN ENTRÉE (INPUT)
    # ET CELUI DES COORDONNÉES LAT-LONG EN SORTIE (OUTPUT). CES CODES ONT ÉTÉ TROUVÉS DANS CE RÉPERTOIRE DES RÉFÉRENCES SPATIALES: http://spatialreference.org/ref/epsg/
    inProj = Proj(init='EPSG:2017')
    outProj = Proj(init='EPSG:4326')
    x1,y1 = coordXarbres,coordYarbres
    x2,y2 = transform(inProj,outProj,x1,y1)
    # print (x2,y2)
    
    # JE FAIS UNE LISTE QUI CONTIENT MES COORDONNÉES CONVERTIES
    listefinale = [x2,y2]
    # print(coordXarbres, coordYarbres)
    
    # J'ÉCRIS CES COORDONNÉES CONVERTIES DANS UN NOUVEAUX FICHIER CSV. LES DEUX COLONNES CRÉÉES POURRONT ALORS ÊTRE AJOUTÉES AU CSV ORIGINAL «tousarbres2.csv»
    écrire = open(nouveaucsv,"a")
    pouet = csv.writer(écrire)
    pouet.writerow(listefinale)
    
    # MISE À JOUR: TOUTE L'OPÉRATION DE CONVERSION-ÉCRITURE A FONCTIONNÉ. TOUTEFOIS, POUR UNE RAISON QUI M'ÉCHAPPE, LA CARTOGRAPHIE DES DONNÉES CONVERTIES DANS CARTO
    # MOTNRE UNE GRANDE IMPRÉCISION (DES ARBRES SONT LOCALISÉS DANS LE FLEUVE ST-LAURENT, PAR EXEMPLE). JE DEVRAI DONC M'EN REMETTRE À QGIS POUR CONVERTIR CORRECTEMENT
    # LES VALEURS DE PROJECTION EN COORDONNÉES LAT-LONG.
