#-------------------------------------------------------------------------------
# Name:        Les ancres
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#coding:utf-8

#Il y a 9 ances possibles :
"""
NW  N   NE  W   CENTER  E   SW  S   SE

"""
from tkinter import *

root = Tk()
root.title("Les ancres")

lbl1 = Label(root, text="Rose", font='Arial 30 bold', anchor=NW, width=20)
lbl2 = Label(root, text="begonia", font='Arial 30 bold',width=20)
lbl3 = Label(root, text="Kiwi", font='Arial 30 bold',anchor = 'se',width=20)

lbl1.pack()
lbl2.pack()
lbl3.pack()

root.mainloop()