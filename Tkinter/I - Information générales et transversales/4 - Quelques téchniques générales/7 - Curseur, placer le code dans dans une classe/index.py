#-------------------------------------------------------------------------------
# Name:        Curseeur
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

class ScaleDemo:
    def __init__(self,r):
        self.side = side
        self.m = side/2
        root = Tk()
        self.cnv = Canvas(root,width=side, height=side)
        self.cnv.pack()
        self.old = None
        curseur= Scale(root, orient = "horizontal", command= self.rayon, from_=0, to=100)
        curseur.pack()
        root.mainloop()

    def rayon(self,r):
        r = int(r)
        m = self.m
        self.cnv.delete(self.old)
        self.old = self.cnv.create_oval(m-r,m-r,m+r, m+r)

side = 400
ScaleDemo(side)
