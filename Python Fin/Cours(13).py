#-------------------------------------------------------------------------------
# Name:        Proriété d'encapsulation
# Purpose:  Cours 13
#
# Author:      Muriel
#
# Created:     03/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding: utf-8

"""
Propriété : manière de manipuler:contrôler des attributs
            principe d'encapsulation !
"""

class Humain:

    """Cette classe represente un Humain"""

    def __init__ (self, nom, age):
        print("Création d'un Humain")
        self.nom = nom
        self._age = age

    def _getage(self): # <getter>
        #print("Recuperation non autorise")
        try :
            return self._age #_age est une propriété
        except AttributeError:
            print("L'age n'existe pas !")

    def _setage(self, nouvel_age): # <setter>

        if nouvel_age < 0:
            self.age = 0
        else:
            self._age = nouvel_age

    def _delage(self): # <deleter>
        del self._age

    """property(<getter>, <setter>, <deleter>, <helper>) , <getter>, <setter>,..
    des accesseurs"""
    age = property(_getage, _setage,_delage, "Je suis l'age d'un Humain")

"""
#Programme principal
h1 = Humain("Murie",21)

#print(h1._age)
print(h1.age)

del h1.age

#h1._age = 14
#h1.age = -14

#print(h1._age)
print(h1.age)
"""
help(Humain.age)