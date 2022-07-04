#-------------------------------------------------------------------------------
# Name:        Supprimer des images à la souris
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *
from random import randrange

SIDE = 400
root=Tk()
root.title("Supprimer des images à la souris")
cnv= Canvas(root, width=SIDE, height=SIDE)
cnv.pack()

logo = PhotoImage(file="devsuccess.png")

for i in range(5):
    x, y = randrange(SIDE), randrange(SIDE)
    cnv.create_image(x, y, image = logo)

#Ligne 34 à 40
"""
La fonction clic enregistre la position (x,y) du clic (ligne 38-33) et appelle
la méthode find_closest du canevas et recherche l'item t le plus proche de la
position (x,y). L'appel récupère l'item en question (ou None si le canevas est
vide et le supprime (ligne 40) grâce à son id qui est le premier élément du tuple
(ligne 40) représentant l'item.
"""
def clic(event):
    x = event.x
    y = event.y
    t= cnv.find_closest(x,y)

    if t:
       cnv.delete(t[0])

cnv.bind("<Button>",clic)

root.mainloop()
