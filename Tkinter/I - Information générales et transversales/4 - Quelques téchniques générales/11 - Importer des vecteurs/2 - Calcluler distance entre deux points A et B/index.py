#-------------------------------------------------------------------------------
# Name:        Calculer la distance entre deux points A et B
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from turtle import Vec2D as vect

A = (2,3)
B = (4,1)

#Accés habituel aux coodonnées
AB = vect(B[0], B[1]) - vect(A[0], A[1])
print(abs(AB))

#Accés par  décompression aux coordonnées

AB = vect(*B) - vect(*A)
print(abs(AB))