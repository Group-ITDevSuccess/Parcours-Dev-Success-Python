#-------------------------------------------------------------------------------
# Name:        Le widget entrée
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *
from random import randrange

COTE = 200
SIDE = 20

root=Tk()
cnv=Canvas(width=COTE, height=COTE, bg='ivory')
cnv.pack()
"""
La fonction appelée lorsque l’entrée est validée. Cette fonction reçoit un évé-
nement event. Cet événement correspond à l’appui sur la touche ENTRÉE mais n’est pas
véritablement utilisé par la fonction dessiner
"""
def dessiner(event):
    n =int(my_entry.get())
    color = "#%s%s%s" %(randrange(10),randrange(10), randrange(10))
    for i in range(n):
        x =randrange(COTE)
        y =randrange(COTE)
        cnv.create_rectangle(x, y, x + SIDE, y + SIDE, fill=color, outline='')

my_entry = Entry(root)
my_entry.pack()
"""
si on appuie sur une certaine touche indiquée comme premier argument de bind (dans
notre exemple la touche ENTRÉE référencée par <Return>), une fonction de commande est
exécutée (ici la fonction dessiner)
"""
my_entry.bind('<space>', dessiner)

root.mainloop()