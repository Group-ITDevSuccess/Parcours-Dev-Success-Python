#-------------------------------------------------------------------------------
# Name:        Les tuples
# Purpose:  Cours 17
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

#Créer un tuple

"""
(!) Tuple : conteneur immuable (dont on ne peut pas modifier les valeurs)

Création de tupe:
                    mon_tuple = ()      #Tuple Vide
                    mon_tuple = (45,)   #Une seul valeur
                    mon_tuple = 45,     #Idem qu'au-dessus
                    mon_tuple = (4,8)   #Plusieur valeurs

Accès aux Valeurs : mon_tuple[X]        #Valeur d'indice X

2 raisons d'utliser les tuples :
    * Affectation mulptiple de variable
(nombre1, nombre2) = (14, 16)

    * retour multiple de fonction
"""

def get_player_position():
    posX = 149
    posY = 86

    return (posX, posY)

#Programme principal

CoordX = 0
CoordY = 0

print("Position de joueur :({}/{})".format(CoordX,CoordY))

(CoordX,CoordY) = get_player_position()

print("Position de joueur :({}/{})".format(CoordX,CoordY))


