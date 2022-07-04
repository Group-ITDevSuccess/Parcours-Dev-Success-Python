#-------------------------------------------------------------------------------
# Name:        La Modularité
# Purpose:  Cours 8
#
# Author:      Muriel
#
# Created:     01/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#coding:utf-8
#---------------------------------------------
#Une autre type de fonction : fonction lambda :

salut = lambda: print("Salam Alaikum")

salut()


ttc = lambda prixHT: prixHT + (prixHT * (20/100)) #prixHT est un variable

print(ttc(24))

calcule = lambda a, b : a + b

print(calcule(15,6))

#-----------------------------------------------
#Modalité:

"""
NB: les modules sont des fichiers.
Importer un module: import <nom_module>
                    from <nom_module> import <nom_fonction>
                    from <nom_module> import *
            NB: si on utilise from <...> import <...> on ne precise pas lors
            declaration: ex: math.sqrt(45) mais comme ça sqrt(45) directement
        exemple:
            from math import sqrt
            from math import sin
"""
import math

result = math.sqrt(100)

print (result)

sinus = math.sin(42)
print (sinus)

#Effacer le terminal ou reinitialiser notre interpreter
"""
import os

os.system("clear") #sur Mac et linux : os.system("clear") et sur CMD : os.system("cls")
"""

import include.module as module     #Si le moducle est dans une sous-dossier
#import module as module            Si le module se trouver dans le meme dossier

module.au_revoir()
module.parler("Muriel","Barak'Allah")
