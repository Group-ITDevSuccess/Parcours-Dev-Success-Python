#-------------------------------------------------------------------------------
# Name:        Modifier dynamiquement la géométrie de la fenêtre
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root = Tk()
root.title("Modifier dynamiquement la géométrie de la fenêtre")
cnv = Canvas(root, width=400, height= 400)
cnv.pack()

def printgeom():
    root.geometry("600x600+200+50")
    print(root.geometry())

print(root.geometry())
#Au bout de 2,5 s, la géométrie de la fenêtre est modiée
cnv.after(2500, printgeom)

root.mainloop()