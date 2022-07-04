#-------------------------------------------------------------------------------
# Name:        Témoin de prise de focus
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas, Button
from random import randrange

W = H = 200
root = Tk()
root.title("Mon fenetre avec focus")

cnv = Canvas(root, width=W, height=H, bg='ivory',
    highlightthickness = 20,
    highlightbackground = 'pink',
    highlightcolor="red",
    takefocus = 1)
cnv.pack(side="left")

Button(root, text = 'Active',
    highlightthickness = 5,
    highlightbackground = 'pink',
    highlightcolor="red").pack()

def dessiner(event):
    a = randrange(W)
    b = randrange(H)
    cnv.create_rectangle(a,b, a + 10, b + 10, fill="blue", outline='')

cnv.bind('<Return>', dessiner)

root.mainloop()