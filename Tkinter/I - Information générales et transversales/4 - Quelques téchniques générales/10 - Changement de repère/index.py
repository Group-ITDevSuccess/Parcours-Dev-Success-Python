#-------------------------------------------------------------------------------
# Name:        Changement de repère
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

def chgt(X, Y, center):
    """
    (X, Y): coordonnées dans le repère mathématique habituel
    center=(x0,y0) coordonnées dans le repère du
    canevas du centre du repère mathématique
    habituel renvoie coordonnées (x, y) du canevas
    """

    return (X+center[0], -Y+center[1])

center = (SIDE//2, SIDE//2)

X = -200
Y = 40

x, y = chgt(X,Y, center)
cnv.create_text(x, y, text= "Salam Alaikum")