#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

#RIGHT permet de bloquer le déplacement vers la dorite
RIGHT = 300

root= Tk()
root.title("Déplacer un objet à la souris")
cnv = Canvas(root, width=300, height=200)
cnv.pack(padx=10, pady=10)

rect= cnv.create_rectangle(30,30,130,130, fill="lightblue", outline='')

old = [None, None]

def clic(event):
    old[0] = event.x
    old[1] = event.y

def glisser(event):
    a, b, c, d = cnv.coords(rect)
    #c donne l'abscisse courant du bord droit du rectangle
    if c < RIGHT or event.x < old[0]:
       """
       A cause du dernier paramètre qui vaut 0, il n'y pas de déplacement du
       rectangle suivant la composant verticale.
       """
       cnv.move(rect, event.x-old[0], 0)
    old[0] = event.x
    old[1] = event.y

cnv.bind("<B1-Motion>", glisser)
cnv.bind("<Button-1>", clic)

root.mainloop()

