#-------------------------------------------------------------------------------
# Name:        Déplacer un  objet à la souris
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

root= Tk()
root.title("Déplacer un objet à la souris")
cnv = Canvas(root, width=300, height=200)
cnv.pack(padx=10, pady=10)

rect= cnv.create_rectangle(30,30,130,130, fill="lightblue", outline='')

#Ligne 23 à 36:
"""
Le principe est qu'une variable old enregistre la dernière position de la souris,
ce qui permet de savoir, à l'instant courant, de combien (ligne 37) on doit
déplacer l'objet. Cette position est initialisée au clic qui précède le glisser-époser
(ligne 34-35)

"""
old = [None, None]

def clic(event):
    old[0] = event.x
    old[1] = event.y

#event.x-old[0], event.y-old[1]
"""
Représente le vecteur de déplacement entre le moment courant et le dernier
enregistrement de position.

"""
def glisser(event):
    cnv.move(rect, event.x-old[0], event.y-old[1])
    #On met a jour la position de la souris
    old[0] = event.x
    old[1] = event.y

cnv.bind("<B1-Motion>", glisser)
cnv.bind("<Button-1>", clic)

root.mainloop()


