#-------------------------------------------------------------------------------
# Name:        Déplacer un item avec la méthode coords
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
cnv = Canvas(root, width=300, height=200)
cnv.pack()

A = (70,30)
B = (30,160)
C = (150,120)

tr = cnv.create_polygon(A, B, C , fill='gray')

def deplacer(x, y):
    cnv.coords(tr, A[0]+x, A[1]+y, B[0]+x, B[1]+x, C[0]+x, C[1]+y)

cnv.after(1000, deplacer, 150, 50)
root.mainloop()