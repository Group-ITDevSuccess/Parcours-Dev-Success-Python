# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:09:51 2022

@author: Muriel
"""

from tkinter import *
from random import randrange

WIDTH = 400
HEIGHT = 400
COTE = 20

root = Tk()
root.title("Tag sur un item")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
cnv.pack()

for i in range(40):
    x = randrange(WIDTH)
    y = randrange(HEIGHT)
    if x > WIDTH // 2:
        cnv.create_rectangle(x, y, x+COTE, y+COTE, fill='light blue', outline='', tag='right')
    else:
        cnv.create_rectangle(x, y, x+COTE, y+COTE, fill='pink', outline='', tag='left')

def move():
    cnv.move("right", -WIDTH//2, 0)
    cnv.move("left", WIDTH//2, 0)
cnv.after(1000, move)

root.mainloop()