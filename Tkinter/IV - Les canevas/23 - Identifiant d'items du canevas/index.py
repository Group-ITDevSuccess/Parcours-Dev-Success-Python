#-------------------------------------------------------------------------------
# Name:        Identifiant d'items du canevas
# Purpose:
#
# Author:      Muriel
#
# Created:     20/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
from tkinter import *
from random import randrange

SIDE = 400
root= Tk()
root.title("Identifiant d'items du canevas")
cnv = Canvas(root, width=SIDE, height=SIDE)
cnv.pack()

t =SIDE//2

xA, yA = A = (randrange(t), randrange(t))
xB, yB = B = (randrange(t), randrange(t))
xC, yC = C = (randrange(t), randrange(t))

rect1 = cnv.create_rectangle(A, (xA+t, yA+t), fill='ivory')
rect2 = cnv.create_rectangle(B, (xB+t, yB+t), fill='red')
rect3 = cnv.create_rectangle(C, (xC+t, yC+t), fill='green')

print(rect3)
print(rect2)
print(rect1)

root.mainloop()