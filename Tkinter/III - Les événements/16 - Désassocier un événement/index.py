#-------------------------------------------------------------------------------
# Name:        Désassocier un événement
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from random import randrange
from tkinter import *

root = Tk()
root.title("Désassocier un événement")
cnv = Canvas(width=400, height=400, bg="lightgreen")
cnv.pack(side="left")
lbl= Label(text='', width=10, font="Arial 20 bold")
lbl.pack(side="right")

MESSAGE = ["Bien \n joué !", "Nice", "Super !", "Bravo !", "Champion !", "OK !"]

def f(event):
    x, y = event.x, event.y
    if 100 < x < 300 and 100 < y < 300:
       lbl['text'] = "Perdu !"
       #Si le joueyr clique dans la zone en rouge
       """
       On lui annonce qu'il a perdu et le clic gauche dans la fenêtre ne réagira
       plus (à cause de unbind)
       """
       root.unbind("<Button-1>")
    else:
         lbl['text'] = MESSAGE[randrange(len(MESSAGE))]

A = (100,100)
B = (300,300)
cnv.create_rectangle(A, B, fill='red', outline='')

root.bind("<Button-1>", f)



root.mainloop()