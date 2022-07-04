#-------------------------------------------------------------------------------
# Name:        Gestion de curseur
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *
from random import randrange

root = Tk()
root.title("Mon fenêtre avec curseur personnaliser")
cnv =Canvas(root, width=400, height=400)
cnv.pack()

old=None

def rayon(r):
    global old
    r = int(r)
    cnv.delete(old)
    old = cnv.create_oval(200-r,200-r,200+r,200+r)

r = randrange(0,200)
rayon(r)

curseur = Scale(root, orient="horizontal", command=rayon, from_=0, to=200)
curseur.set(r )
curseur.pack()


root.mainloop()