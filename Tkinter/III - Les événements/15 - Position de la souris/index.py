#-------------------------------------------------------------------------------
# Name:        Position de la souris
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

def clic(event):
    x = event.x
    y = event.y
    print("Position :", x, y)

root = Tk()
root.title("Position de la souris !")

root.bind("<Button-1>",clic)

root.mainloop()
