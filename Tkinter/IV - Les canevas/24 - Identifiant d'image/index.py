#-------------------------------------------------------------------------------
# Name:        Identifiant d'image
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
from random import randrange

SIDE = 400
root= Tk()
root.title("Identifiant d'items du canevas")
cnv = Canvas(root, width=SIDE, height=SIDE)
cnv.pack()

logo = PhotoImage(file="devsuccess.png")

for i in range(5):
    x, y = randrange(SIDE), randrange(SIDE)
    id_image = cnv.create_image(x, y, image=logo)
    print(id_image)

root.mainloop()