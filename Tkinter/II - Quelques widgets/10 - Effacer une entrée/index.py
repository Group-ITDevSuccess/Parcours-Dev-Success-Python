#-------------------------------------------------------------------------------
# Name:        Effacer une entrée
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import *
from random import randrange

WIDTH = 200
HEIGHT = 200

COTE = 20

root =Tk()
root.title("Effacer une entrée")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg='ivory')
cnv.pack()

def dessiner(event):
    n = int(my_entry.get())
    color = "#%s%s%s" % (randrange(10), randrange(10), randrange(10))
    for i in range(n):
        x = randrange(WIDTH)
        y = randrange(HEIGHT)
        cnv.create_rectangle(x,y, x + COTE, y + COTE, fill=color, outline='')
    my_entry.delete(0, END)

my_entry = Entry(root)
my_entry.pack()
my_entry.bind('<Return>', dessiner)

root.mainloop()