#-------------------------------------------------------------------------------
# Name:        Mon essaye de code tkinter dans un fonction
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas, Scale

def rayon(r):
    cnv, side, old = data
    r = int(r)
    m = side/2
    cnv.delete(old)
    data[2] = cnv.create_oval(m-r, m+r, m+r)

def demo(side):
    global data
    root = Tk()
    root.title("Mon essaye de code tkinter dans un fonction")
    cnv = Canvas(root, width=side, height=side)
    cnv.pack()

    old = None

    curseur = Scale(root, orient="horizontal", command=rayon, from_=0, to=100)
    curseur.pack()

    date = [cnv, side, old]

    root.mainloop()

side = 400
demo(side)