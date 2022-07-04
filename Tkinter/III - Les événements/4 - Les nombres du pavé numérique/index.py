#-------------------------------------------------------------------------------
# Name:        Les nombres du pavé numérique
# Purpose:
#
# Author:      Muriel
#
# Created:     17/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas
from random import randrange

SIDE = 200

root = Tk()
root.title("Les nombres du pavé numérique")
cnv = Canvas(root,width=SIDE, height=SIDE, bg="ivory")
cnv.pack(padx=10, pady=10)
#On donne la focus au canvas
""""
Comme ça, l'application réagit à l'appui sur une touche.
"""
cnv.focus_set()

def dessiner(event):
#On capture la chaîne repésentant l'appui
    """
    Elle commence par KP_; le caractère suivant; l'indice 3 donc, représente sur
    le chiffre sur lequel on a appuyé. Ce caractère est converti en vrai entier
    avec la la fonction int

    """
    n = int(event.keysym[3])
#On est en mesure, avec range(n) de dessiner la bonne nombre de carrés.
    for i in range(n):
        a =randrange(SIDE)
        b =randrange(SIDE)
        cnv.create_rectangle(a, b, a  + 20, b + 20, fill = "red")
"""
Seules les touches 1,2 et 3 du pavé numérique qui est la caractère d'indice 3
dans la chaîne représentant l'événement, comme la chaîne "KP_1".
"""
cnv.bind('<KP_1>',dessiner)
cnv.bind('<KP_2>',dessiner)
cnv.bind('<KP_3>',dessiner)

root.mainloop()