#-------------------------------------------------------------------------------
# Name:        Conversion de couleur némerique en exadécimal
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

def rgb_10to16(r,g,b):

    return ("#%.02x" %r + "%.02x" %g + "%.02x" %b)

#Royal Fuschia

X = input("Entrer le Couleur Red (0 à 255) : ")
Y = input("Entrer le Couleur Green (0 à 255) : ")
Z = input("Entrer le Couleur Bleu (0 à 255) : ")

if (int(X) >= 0 and int(X) <= 255) and (int(Y) >= 0 and int(Y) <= 255) and (int(Z) >= 0 and int(Z) <= 255):
    result = rgb_10to16(int(X),int(Y),int(Z))
else:
    print("Valeur saisie faut !")
    result = 0
if (result == 0):
    print("Réessayer")
else:
    print("La couleur en hexadecimal : ",result)