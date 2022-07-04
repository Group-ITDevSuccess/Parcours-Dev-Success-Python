#-------------------------------------------------------------------------------
# Name:        La liste de tous les itmes du canevas
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

WIDHT = 200
HEIGHT = 200
COTE = 20

root = Tk()
root.title("La liste de tous les itmes du canevas")
cnv = Canvas(root, width=WIDHT, height=HEIGHT, bg="ivory")
cnv.pack()

N = randrange(10)
print(N)

for _ in range(N):
    x = randrange(WIDHT)
    y = randrange(HEIGHT)
    cnv.create_rectangle(x, y, x+COTE, y+COTE, fill="purple")

print(cnv.find_all())

root.mainloop()