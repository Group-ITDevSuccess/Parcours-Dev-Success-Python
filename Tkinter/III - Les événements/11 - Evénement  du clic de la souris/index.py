#-------------------------------------------------------------------------------
# Name:        Evénement  du clic de la souris
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

root = Tk()
root.title("Evénement  du clic de la souris")
cnv = Canvas(root, width=300, height=300, bg="ivory")
cnv.pack(pady=10, padx=10)
cnv.focus_set()

def clic(event):
    x, y = event.x, event.y
    print(x, y)
    cnv.create_oval(x-3, y-3, x+3, y+3, fill='red', outline='')

cnv.bind("<Button-1>", clic)

root.mainloop()