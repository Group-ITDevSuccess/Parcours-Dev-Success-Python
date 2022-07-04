#-------------------------------------------------------------------------------
# Name:        Inclusion d'images sur le canevas
# Purpose:
#
# Author:      Muriel
#
# Created:     19/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *
from random import randrange

SIDE =400
root=Tk()
root.title("Mon image dans un canevas")
cnv = Canvas(root, width=SIDE, height=SIDE)
cnv.pack(pady=10, padx=10)

logo =PhotoImage(file="devsuccess.png")

for i in range(5):
    centre = (randrange(SIDE), randrange(SIDE))
    #Note:
    """
    create_image(c, image=logo), c est un coordonnée c = (c, y), on peut ecrire
    sous forme : create_image(x, y, image=logo)
    """
    cnv.create_image(centre, image=logo)

root.mainloop()