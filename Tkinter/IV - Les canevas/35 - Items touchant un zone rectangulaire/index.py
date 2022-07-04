# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:39:56 2022

@author: Muriel
"""

from tkinter import *

WIDTH=400
HEIGHT=400

root= Tk()
root.title("Items touchant une zone rectangulaire")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
cnv.pack()

#Rectangle de référence
a, b = U = (200, 120)
c, d = V = (350, 350)
cnv.create_rectangle(U, V)

COTE = 50

#Carré bleu
x=y=40
cnv.create_rectangle(x, y, x+COTE, y+COTE, fill="blue", outline='')

#Carré vert
x=180
y=80
cnv.create_rectangle(x, y, x+COTE, y+COTE, fill="green", outline='')

#◘Crré rouge
x = 240
y = 260
cnv.create_rectangle(x, y, x+COTE, y+COTE, fill="red", outline='')

print(cnv.find_all())
print(cnv.find_overlapping(a+1, b+1, c-1, d-1))

root.mainloop()