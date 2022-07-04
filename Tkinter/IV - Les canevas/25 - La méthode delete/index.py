#-------------------------------------------------------------------------------
# Name:        La méthode deleteLa méthode delete
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
SIDE = 180
root= Tk()
root.title("La méthode delete")
cnv = Canvas(root, width=SIDE, height=SIDE)
cnv.pack()

rect1 = cnv.create_rectangle(20,20,80,80, fill="red",outline='')
rect2 = cnv.create_rectangle(100,20,160,80, fill="red",outline='')
rect3 = cnv.create_rectangle(70,40,100,90, fill="red",outline='')

def effacer(ident):
    cnv.delete(ident)

cnv.after(2000, effacer, rect1)

#Effacer tout
cnv.after(4000, effacer, 'all')

root.mainloop()