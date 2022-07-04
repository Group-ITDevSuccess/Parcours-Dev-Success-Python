#-------------------------------------------------------------------------------
# Name:        L'optin fill
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

#L’option ll permet d’étendre le widget dans sa zone de placement.
"""
On donne l’option sous la fome fill=v ou v vaut :

— X pour une expansion dans le sens horizontal,
— Y dans le sens vertical
— NONE pour une absence d’expansion (valeur par défaut)
— BOTH pour une expansion dans toutes les directions
"""

from tkinter import *

root = Tk()
root.title("L'optin fill")

cnv = Canvas(root, width=400, height=400, background="ivory")
lbl1 = Label(root, text="Orange", bg="orange", width=15)
lbl2 = Label(root, text="Rouge", bg="red", width=15)

cnv.pack()
lbl1.pack(fill=X)
lbl2.pack()

root.mainloop()