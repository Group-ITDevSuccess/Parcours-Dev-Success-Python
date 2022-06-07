#-------------------------------------------------------------------------------
# Name:        Les héritages
# Purpose:  Cours 14
#
# Author:      Muriel
#
# Created:     05/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding: utf-8


"""
Fonction utlise:
    isinstace (<objet>, <classe>):  vérifie qu'un objet
                                    est de la classe renseignée

    issubclass(<classe_fille>, <classe_mere>) : verifie qu'un
                                            classe est fille d'une autre

"""
#Classe Mère:
class Vehicule:
    def __init__(self, nom_vehicule, quantite_essence):
        self.nom = nom_vehicule
        self.essence = quantite_essence

    def se_deplacer(self):
        print("La Voiture {} se deplace....".format(self.nom))

#Classe Fille:
class Voiture(Vehicule):
    def __init__(self, nom_voiture, essence, puissance):
        Vehicule.__init__(self, nom_voiture,essence)
        self.puissance = puissance

    def se_deplacer(self):
        print("Je roule ....")
class Avion(Vehicule):
    def __init__(self, nom, essence, marchandise):
        Vehicule.__init__(self, nom, essence)
        self.marchandise = marchandise

    def se_deplacer(self):
        print("Je Vole...")

#Programme Principal
"""
v1 = Vehicule("F22 Raptor",254)
v1.se_deplacer()
print(v1.nom)
"""
voiture1 = Voiture("Toyota Supra",90,420)
voiture1.se_deplacer()

print(voiture1.puissance, "CH")

avion1 =  Avion("F22 Raptor",2450, "Missile")

avion1.se_deplacer()
print("Il transport {}".format(avion1.marchandise))