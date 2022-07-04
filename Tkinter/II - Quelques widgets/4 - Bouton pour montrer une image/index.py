#-------------------------------------------------------------------------------
# Name:        Bouton pour montrer une image
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *
from random import randrange

SIDE = 400
root=Tk()
cnv= Canvas(root, width=SIDE, height=SIDE, bg='ivory')
cnv.pack()

logo = PhotoImage(file="devsuccess.png")

def show():
    center = (randrange(SIDE), randrange(SIDE))
    cnv.create_image(center, image=logo)

btn = Button(root, text="Nouveau", command=show)
btn.pack()

root.mainloop()