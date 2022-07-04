#-------------------------------------------------------------------------------
# Name:        Bord d'un canevas
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
root.title("Bord d'un canevas")

#Largeur du canevas
W= 300

#Hauteur du canevas
H = 200

#Largeur du bord
B = 50

#Largeur de la zone de focus
F =10

cnv = Canvas(root, width=W, height=H, bg="ivory",
    bd=B, highlightthickness = F,
    highlightbackground="green")
cnv.pack(side="left", pady=20, padx=20)

#Partie active du canevas
z = B + F
w = W - 1
h = H - 1

cnv.create_rectangle(z, z, z + w, z + h, fill ="orange")

root.mainloop()