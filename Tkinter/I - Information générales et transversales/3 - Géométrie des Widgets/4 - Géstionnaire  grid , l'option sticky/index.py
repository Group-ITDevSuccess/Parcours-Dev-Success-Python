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

from tkinter import *

root= Tk()
root.title("L'option sticky()")

a = Label(root, text = "A", bg='red', width=20,height=2)
a.grid(row=0, column=0)

b = Label(root, text = "B", bg='lightblue', width=10)
b.grid(row=0, column=1, sticky=N)

c = Label(root, text = "C", bg='lime',height=2)
c.grid(row=1, column=0, sticky=E+W)

d = Label(root, text = "D", bg='orange', width=5,height=2)
d.grid(row=1, column=1, sticky=NE)
"""
L’eet de sticky est de coller le widget dans la direction
indiquée, avec un éventuel effetet de remplissage par étirement de la zone
libre de la cellule.
L’option N+E+S+W est de remplir toute la cellule.
"""
root.mainloop()