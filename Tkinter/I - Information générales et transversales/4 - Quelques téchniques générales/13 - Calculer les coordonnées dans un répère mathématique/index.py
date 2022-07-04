#-------------------------------------------------------------------------------
# Name:        Calculer les coordonnées dans un répère mathématique
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from turtle import Vec2D

C = (100, 100)
M = (150, 100)

CM = Vec2D(*M) - Vec2D(*C)
v = CM.rotate(60)
N = Vec2D(*C) + v

print(N)

