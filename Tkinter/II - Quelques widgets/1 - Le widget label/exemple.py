#-------------------------------------------------------------------------------
# Name:        Mon widget statique et dynamiqu
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

#Ici, il y a deux labels:
"""
* un label statique, à gauche, qui porte la mention Nombre de carré
* un label dynamique, à droite, qui indique la valeur du nombre de carrés présents sur le canevas
"""

from tkinter import *
from random import randrange

WIDTH = 400
HEIGHT = 300

COTE = 20

root = Tk()
root.title("Mon widget statique et dynamique")
cnv = Canvas(root, width = WIDTH, height= HEIGHT, bg='ivory')
cnv.pack()

def dessiner():
    global cpt
    k =  randrange(3)
    cpt += k

    for i in range(k):
        color = "#%s%s%s" % (randrange(10),randrange(10),randrange(10))
        x = randrange(WIDTH)
        y = randrange(HEIGHT)

        cnv.create_rectangle(x, y, x + COTE, y + COTE, fill = color, outline='')

descr = Label(root, text = "Nombre de \n Carrés: ", font='Arial 10 bold')
descr.pack(side = 'left')

compteur = Label(root, text = "0", font='Arial 15 bold')
compteur.pack(side='right')

def animer():
    dessiner()

    #Instruction pour mettre à jour le label compteur
    compteur['text'] = str(cpt)

    """
Toutes les demi-secondes, le texte du label est mis à jour en indiquant le nombre
de carrés aléatoires (cf. fonction dessiner lignes 13-23) présents sur le canevas
    """
    cnv.after(500, animer)

cpt = 0
animer()

root.mainloop()