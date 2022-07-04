#-------------------------------------------------------------------------------
# Name:        Créer un arc
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

WIDTH=400
HEIGHT=300

root=Tk()
root.title("Mon arc !")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg='ivory')
cnv.pack()
A = (50, 50)
B = (250, 250)

cnv.create_oval(A,B)
#Pour ligne 28 :
"""
* option extent : la totalité de l'angle (OA, OB), end dégrés
* option start : l'angle en degrés (u, OA) où représente un demi-droite horizontale
dirigée vers l'Est et A le point de départ sur l'ellipse.

"""
cnv.create_arc(A,B, outline="red",extent=210,start=-120, fill="light blue",width=4)


root.mainloop()