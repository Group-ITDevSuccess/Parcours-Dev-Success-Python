#-------------------------------------------------------------------------------
# Name:        Lire et e=écrire dans un fichier
# Purpose:  Cours 19
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

"""
Modes d'ouverture :
    r   (lecture seule)
    w   (écriture avec remplacement)
    a   (écriture avec ajout en fin de fichier)
    r+  (lecture/écriture dans un même de fichier)

verifier si le ficheir est fermer:
    if fic.closed:
        print("Fichier fermé")
    else:
        print("Fichier est ouverte")

Lecture :
    read()
    readline()  # Récupérer tout les lignes
    readlines() # Retourner les restes de lignes qui ne sont pas lu mais sous forme de liste
"""

# fic = open("dossier/Cours(19).txt","r")

"""
with open("dossier/Cours(19).txt","w") as fic:

    content = fic.read()
    print(content)

    nombre = 15
    fic.write(str(nombre))
    fic.write("\nSalam Alaikmur")
    fic.write(" Muriel")

    # fic.close()
    #Pas besoin de fermer le ficheir avec "with"
"""

import pickle

class Player:
    def __init__(self, nom, level):
        self.name = nom
        self.level = level

    def niveau(self):
     print("{} : ({})".format(self.name, self.level))
#Ecrire en bianire sur un fichier
"""
p1 = Player("Muriel",10)

with open("dossier/player.data","wb") as sauver:
    record = pickle.Pickler(sauver)

    record.dump(p1)
"""
#Lire un fichier en binaire
with open("dossier/player.data","rb") as sauver:
    get_record = pickle.Unpickler(sauver)
    player_one = get_record.load()

player_one.niveau()