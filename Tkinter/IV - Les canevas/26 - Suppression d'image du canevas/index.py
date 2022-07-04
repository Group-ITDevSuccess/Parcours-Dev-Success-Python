#-------------------------------------------------------------------------------
# Name:        Suppression d'image du canevas
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

NB_IMG = 8
SIDE = 100
WIDTH=SIDE*NB_IMG
XO = YO = SIDE // 2

root = Tk()
root.title("Suppression d'image du canevas")

logo = PhotoImage(file="halal.png")

cnv = Canvas(root, width=WIDTH, height=SIDE, bg='ivory')
cnv.pack(pady=100)

ids = []
for k in range(NB_IMG):
    id_image = cnv.create_image(XO+k*SIDE, YO, image=logo)
    ids.append(id_image)

j =randrange(NB_IMG)
print(j)
mon_id = ids[j]

cnv.delete(mon_id)

root.mainloop()