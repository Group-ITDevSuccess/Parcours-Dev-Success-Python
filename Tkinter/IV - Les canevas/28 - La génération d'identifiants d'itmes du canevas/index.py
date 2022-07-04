#-------------------------------------------------------------------------------
# Name:        La génération d'identifiants d'itmes du canevas
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
from random import randrange,sample

COLORS = ["orange","pink","green","yellow","lavender","lightblue"]
NCOLORS = len(COLORS)

WIDHT = 600
HEIGHT = 600
COTE = 20

root = Tk()
root.title("La génération d'identifiants d'itmes du canevas")
cnv = Canvas(root, width=WIDHT, height=HEIGHT, bg="ivory")
cnv.pack(padx=10,pady=10)

N = 100
items_ids = []

for i in range(N):
    x = randrange(WIDHT)
    y = randrange(HEIGHT)
    color = COLORS[randrange(NCOLORS)]
    rect = cnv.create_rectangle(x, y, x+COTE, y+COTE, fill=color, outline='')
    items_ids.append(rect)

print(items_ids == list(range(1, N + 1)))

M = sample(items_ids, N//2)

for m in M:
    cnv.delete(m)

new_itmes_ids = []

for i in range(N):
    x = randrange(WIDHT)
    y = randrange(HEIGHT)
    color = COLORS[randrange(NCOLORS)]
    rect = cnv.create_rectangle(x, y, x+COTE, y+COTE, fill=color, outline='')
    new_itmes_ids.append(rect)

print(new_itmes_ids == list(range(N+1, 2*N+1)))

root.mainloop()