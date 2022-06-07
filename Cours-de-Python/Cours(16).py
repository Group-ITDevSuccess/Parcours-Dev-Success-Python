#-------------------------------------------------------------------------------
# Name:        Les listes
# Purpose:  Cours 16
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

#Crétaion d'une liste
"""
#inventaire = list()
#inventaire = [0]*10 pour multipler le repêtition des coontenue du liste
#inventaire = [1, 4,5, "Muriel"]
#inventaire = range(20)
#inventaire = ["Arc", "Epée", "Bouclier","Position","Fleches","Tunique"]
#inventaire = []
"""
#Parcourir une liste:
"""
i = 0
while i < len(inventaire):
    print(inventaire[i])
    i +=  1

for valeur in inventaire:
    print(valeur)
"""
#print(inventaire[:]) pour afficher tout les éléments
"""
#Acceder ujn élement

liste[X] = Affiche les éléments d'indice X
liste[-X] = Affiche Xème élément en partant de la fin

liste[:] = Affiche tout les éléments
liste[:X] = Affiche les X premiers éléments
liste[X:] = Affiche les X derniers éléments

liste[A:B] = Affiche de l'élement d'indice A à l'éléménts indice B (exclus)

#print(inventaire[:2])
print(inventaire[:])
"""
#Changer les éléments de la list
"""
inventaire[2] = "bouclier d'acier"
print(inventaire[:])
"""
#Recherche dans la liste
"""
if "Epée" in inventaire:
    print("Avoir ")
else:
    print("Non")
"""
#Ajouter une liste en fin de liste
"""
inventaire.append("Arc")
inventaire.append("Epée")
"""
#Inserer dans une listes dans un indice
"""
inventaire.insert(1,"Potion de Mana")
"""
#Suprimer un élement
"""
inventaire.remove("Arc")

del inventaire[1]
"""

#Afficher l'indice d'une liste
"""
print("Indice :", inventaire.index("Arc"))

object_a_suprimer = inventaire.index("Arc")

del inventaire[object_a_suprimer]
"""
#Trier une liste
"""
inventaire.sort()
inventaire.reverse()
"""
#Compter le nombre de éléments

"""
print("Le nombre de Arc :",inventaire.count("Arc"))
"""
#Effacer tout les listes
"""
inventaire.clear()
inventaire[:] = []
"""
#Convertir de chaine en liste
"""
chaine = "Salam Alaikum Muriel"
chaine = chaine.split(" ")
"""
#Convertir une liste en chaine
"""
inventaire = ["Salam","Alaikum","Muriel"]
phrase = " ".join(inventaire)
print(phrase)
"""
#Copier une liste
"""
import copy

liste1 = ["Arc","Epee","Bouclier"]
# Ne fait pas de copy : liste2 = liste1
liste2 = copy.deepcopy(liste1)

print("Liste 1 :",liste1[:])
print("Liste 2 :",liste2[:])

liste2.append("Cheval")

print("Liste 1 :",liste1[:])
print("Liste 2 :",liste2[:])
"""
#Concaténer une liste
"""
import copy
liste1 = ["Arc","Epee","Bouclier"]
liste2 = ["Tenue","Cheval","Soldat"]

print("Liste 1 :",liste1[:])

liste1.extend(liste2) #Meme que liste1 = liste1 + liste2

print("Liste 1 :",liste1[:])
print("Liste 2 :",liste2[:])
"""

#Les tuples
"""
for indice_objet, valeur_objet in enumerate(inventaire):
    print("Element d'indice {} -> {}".format(indice_objet, valeur_objet))
"""