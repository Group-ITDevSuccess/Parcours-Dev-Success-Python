#-------------------------------------------------------------------------------
# Name:        Les focntions
# Purpose:  Cours 7
#
# Author:      Muriel
#
# Created:     01/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#coding:utf-8

"""
Fonction vues:  print(), input()
                type(), int(), float(), bool()

"""

#Crééz son propre fonction :

def info(nom="???",message="!!! "):
    print ("Pour {} : {}".format(nom, message))

info()

#Parametre infinie :
def show_inventory(*list_items):
    for item in list_items:
        print(item)

show_inventory("epee")
show_inventory("epee","arc","potion de mana")

#fonction qui retourne de valeur

def calculer_somme(nombre1, nombre2):

    resultat = nombre1 + nombre2
    return resultat

print(calculer_somme(5,16))
