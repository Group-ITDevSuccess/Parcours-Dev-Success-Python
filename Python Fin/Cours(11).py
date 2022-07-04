#-------------------------------------------------------------------------------
# Name:        Les classes et attributs
# Purpose:  Cours 11
#
# Author:      Muriel
#
# Created:     02/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#coding:utf-8

class Humain:
    """
    Classe des êtres Humains
    """

    humains_crees = 0
    def __init__(self, c_prenom, c_age = 1 ):
        print("Création d'un être Humain....")
        """
        self.prenom = "Muriel"
        self.age = 1
        """
        self.prenom = c_prenom
        self.age = c_age
        Humain.humains_crees += 1

print("Lancement du programme...")

h1 = Humain("Murie",21)
"""
#print("Prénom de h1 {}".format(h1.prenom))
print("Prénom de h1 {}".format(h1.prenom))
print("Age de h1 {}".format(h1.age))

"""
print("Humain existants : {}".format(Humain.humains_crees))

h2 = Humain("Fatima",20)
"""
print("Prénom de h2 {}".format(h2.prenom))
print("Age de h2 {}".format(h2.age))

h2.prenom = "FANO"
print("Nouveau Nom de h2 : {}".format(h2.prenom))

"""

print("Humain existants : {}".format(Humain.humains_crees))
