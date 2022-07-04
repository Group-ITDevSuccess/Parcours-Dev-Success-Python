#-------------------------------------------------------------------------------
# Name:        module1
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

root = Tk()
root.title("Mon curseur(Slider)")

cnv= Canvas(root, width =400, height=400)
cnv.pack()

old = None

def rayon(r):
    global old
    r=int(r)
    cnv.delete(old)
    old = cnv.create_oval(200-r,200-r,200+r,200+r)

curseur = Scale(root, orient="horizontal",command=rayon, from_=0, to=200)
#curseur = Scale(root, command=tirer, from_=0, to=180, length=200)
curseur.pack()

root.mainloop()
