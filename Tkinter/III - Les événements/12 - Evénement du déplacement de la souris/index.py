#-------------------------------------------------------------------------------
# Name:        Evénement du déplacement de la souris
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

root = Tk()
root.title("Evénement du déplacement de la souris")
cnv = Canvas(root, width=200, height=200)
cnv.pack()

cnv.create_rectangle(50,50,150,150, fill='gray')

def mouvement(event):
    if 50 < event.x < 150 and 50 < event.y < 150:
       print("INside")
    else:
         print("OUTside")

#Le mouvement de la souris sur le canevas entraîne l'exécution de la fonction mouvement
cnv.bind("<Motion>", mouvement)

#Si on capture le souris mais avec la bouton gauche
"""
cnv.bind("<B1-Motion>",mouvement)
"""
root.mainloop()