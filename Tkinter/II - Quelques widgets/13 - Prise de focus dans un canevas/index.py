#-------------------------------------------------------------------------------
# Name:        Prise de focus dans un canevas
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas
from random import randrange

SIDE = 200

root = Tk()
root.title("Mon focus")
cnv = Canvas(root, width=SIDE, height=SIDE, bg='ivory')
cnv.pack(padx=10, pady=10)
cnv.focus_set()

def dessiner(event):
    a =randrange(SIDE)
    b =randrange(SIDE)
    cnv.create_rectangle(a,b,a + 20, b + 20, fill ="red")

cnv.bind('<Key>', dessiner)

root.mainloop()
