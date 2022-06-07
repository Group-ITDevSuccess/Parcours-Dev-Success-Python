#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     03/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

class Eleves:
    def __init__(self, nom, prenom, age, numero):
        print("Voici un éleve")
        self.nom = nom
        self.prenom = prenom
        self._age = age
        self._numero = numero

    def _getage(self):
        return self._age

    def _setage(self, age_entrer):
        try:
            if age_entrer < 0:
                self._age = 0
            else:
                self._age = age_entrer
        except:
            print("Entrer un nombre")
    age = property(_getage,_setage)

#Programme principal
e1 = Eleves("TSIDIANY","Muriel", 21, 32)

print(e1.age)

e1.age = "dss"
print(e1.age)