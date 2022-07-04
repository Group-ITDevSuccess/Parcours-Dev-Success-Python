#-------------------------------------------------------------------------------
# Name:        Les fontes avec Python
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

#Les deux Syntaxes pour definir une fonte:
"""
font = "Times 12 bold"
font = ("Times", 12, "bold")

NB: La 2e est utile si le nom de la police contient des espaces
"""
from tkinter import *

root=Tk()
root.title("Les fontes avec Python")

lettre = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
nombre = "0123456789"
Label(root, text=lettre, font=('Arial',12)).pack(side=TOP, anchor="w")
Label(root, text=nombre, font=('Arial',12)).pack(side=TOP, anchor="w")

Label(root, text=lettre, font=('Times New roman',12)).pack(side=TOP, anchor="w")
Label(root, text=nombre, font=('Times New roman',12)).pack(side=TOP, anchor="w")

Label(root, text=lettre, font=('Courier',18)).pack(side=TOP, anchor="w")
Label(root, text=nombre, font=('Courier',18)).pack(side=TOP, anchor="w")

root.mainloop()