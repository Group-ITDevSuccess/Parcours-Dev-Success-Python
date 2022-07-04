#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root= Tk()

#Largeur du canevas
W= 300

#Hauteur du canevas
H = 200

#Largeur du bord
B = 0

#Largeur de la zone de focus
F = 0

cnv = Canvas(root, width=W, height=H, bg='ivory', bd=B, highlightthickness = F)
cnv.pack(side="left", padx=20, pady=200)

#Partie active du canevas
z = B + F
w = W - 1
h = H - 1

cnv.create_rectangle(z, z, z + w, z + h, fill ="orange")

root.mainloop()