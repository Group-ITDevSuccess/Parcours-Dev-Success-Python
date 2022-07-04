#-------------------------------------------------------------------------------
# Name:        Clavier et focus
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *
from random import randrange

WIDTH = 400
HEIGHT = 300

root = Tk()
root.title("Clavier et focus")
cnv = Canvas(root, width=WIDTH, height= HEIGHT, bg='ivory')
cnv.pack()

COTE = 20
cnv.focus_get()

def f(event):
    a = randrange(WIDTH)
    b = randrange(HEIGHT)
    color = "#%s%s%s" %(randrange(10), randrange(10), randrange(10))
    cnv.create_rectangle(a,b,a + COTE, b + COTE, fill=color)

# l’appui sur la touche ENTRÉE (si le canevas a le focus) déclenche l’exécution de la fonction f.
cnv.bind('<Return>',f)

root.mainloop()