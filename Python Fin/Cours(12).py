#-------------------------------------------------------------------------------
# Name:        Les méthodes
# Purpose:  Cours 12
#
# Author:      Muriel
#
# Created:     03/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

"""
Méthode (d'instance): fonction sur une instance (objet)
Méthode de classse  : fonction sur une classe
Méthode statique    : fonction indépendant mais "lié" a une classe
"""

class Humain:
    """
    Classe pour les Humains
    """
    lieu_habitatsion = "Terre"

    def __init__(self, nom, age): #Methode
        self.nom = nom
        self.age = age

    def parler(self, message): #self = méthode standard
        print("{} à dis : {}".format(self.nom,message))

    def changer_planete(cls, nouvelle_planete): #cls = méthode de classe
        Humain.lieu_habitatsion = nouvelle_planete
    changer_planete = classmethod(changer_planete)

    def definition(): #Méthode Statique
        print("Allah Akbar")

    definition = staticmethod(definition)
#Programme Principal

h1 = Humain("Muriel",21)

h1.parler("Salam Alaikum ! ")

print("Planet actuelle {} ".format(Humain.lieu_habitatsion))

Humain.changer_planete("Mars")
print("Planet actuelle : {} ".format(Humain.lieu_habitatsion))

Humain.definition()