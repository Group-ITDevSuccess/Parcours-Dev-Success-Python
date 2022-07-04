#-------------------------------------------------------------------------------
# Name:        Lire les options d'un itme du canevas
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

WIDHT = 300
HEIGHT = 200

root = Tk()
root.title("La génération d'identifiants d'itmes du canevas")
cnv = Canvas(root, width=WIDHT, height=HEIGHT, bg="ivory")
cnv.pack(padx=10,pady=10)

rect = cnv.create_rectangle(30,30,130,130, fill="red", outline="green")

options = cnv.itemconfigure(rect)
print(*options.items(), sep='\n')


root.mainloop()