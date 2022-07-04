#-------------------------------------------------------------------------------
# Name:        PLacer des grille avec pack
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

root = Tk()
root.title("PLacer des grille avec pack")

Scrollbar(root, orient="vertical",command=None).pack(side=RIGHT,fill=Y)
Canvas(root, bg="ivory").pack()
Scrollbar(root, orient="horizontal",command=None).pack(fill=X)


root.mainloop()