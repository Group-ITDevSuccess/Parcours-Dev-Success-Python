# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:43:22 2022

@author: Muriel
"""

from tkinter import *

WIDTH = 400
HEIGHT = 200
COTE = 40

root = Tk()
root.title("Evénement associé à un tag")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
cnv.pack()

milieu = HEIGHT/2-COTE/2
debut = 10
fin = WIDTH-debut

cnv.create_rectangle(debut, milieu, debut+COTE, milieu+COTE, fill="blue", outline='', tag="mobile")

def animate(v):
    a, b, c, d = cnv.coords("mobile")
    if a < debut or c > fin:
        v = -v
        cnv.move("mobile", v, 0)
        cnv.after(25, animate, v)

def change_couleur(event):
    print("click !")
    color = cnv.itemconfig("mobile", "fill")[-1]
    if color == "red":
        color = "blue"
    else:
        color = "red"
    cnv.itemconfig("mobile", fill=color)

cnv.tag_bind("mobile","<Button-1>", change_couleur)

animate(v = 3)

root.mainloop()