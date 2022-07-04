#-------------------------------------------------------------------------------
# Name:        Le widget bouton
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

WIDTH = 300
HEIGHT = 200

COTE = 20

root = Tk()
root.title("Mon bouton")
cnv = Canvas(root, width=WIDTH, height=HEIGHT,bg='ivory')
cnv.pack()

def dessiner():
    color = "#%s%s%s" %(randrange(10), randrange(10), randrange(10))
    x = randrange(WIDTH)
    y = randrange(HEIGHT)
    cnv.create_rectangle(x, y, x + COTE, y + COTE, fill = color, outline='')

btn = Button(root, text = "Carré\nAléatoire", command=dessiner)
btn.pack()

root.mainloop()