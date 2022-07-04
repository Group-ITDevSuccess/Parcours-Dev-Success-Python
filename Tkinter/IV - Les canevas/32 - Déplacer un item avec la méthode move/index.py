#-------------------------------------------------------------------------------
# Name:        Déplacer un item avec la méthode move
# Purpose:
#
# Author:      Muriel
#
# Created:     21/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#coding:utf-8

from tkinter import Tk, Canvas

root = Tk()
root.title("Déplacer itme avec move")
cnv = Canvas(root, width=600, height=400)
cnv.pack()

xA = 130
yA = 30
xB = 30
yB = 130

rect = cnv.create_rectangle(xA,xB,yA,yB, fill='gray')

v = (xB-xA, yB-yA)

def deplacer(x):
    cnv.move(rect, *x)

cnv.after(1000, deplacer, v)

root.mainloop()