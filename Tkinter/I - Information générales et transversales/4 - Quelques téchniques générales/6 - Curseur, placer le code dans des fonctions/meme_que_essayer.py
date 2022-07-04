#-------------------------------------------------------------------------------
# Name:        module1
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

def make_move(data):
    cnv, side, old = data
    def rayon(r):
        r =int(r)
        m =side/2
        cnv.delete(data[2])
        data[2] = cnv.create_oval(m-r, m-r, m+r, m+r)
    return rayon

def demo(side):
    root = Tk()
    cnv = Canvas(root, width=side, height=side)
    cnv.pack()
    data = [cnv,side,None]
    rayon = make_move(data)

    curseur = Scale(root, orient="horizontal", command= rayon, from_=0, to = 100)
    curseur.pack()

    root.mainloop()

def main(entrer):
    side = entrer
    demo(side)

try:
    X = input("Entrer un nombre :")
    X = int(X)
    main(X)
except:
    print("Saisir un nombre")