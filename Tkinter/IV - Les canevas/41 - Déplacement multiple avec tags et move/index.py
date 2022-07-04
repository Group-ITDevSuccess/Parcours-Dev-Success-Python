# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:34:30 2022

@author: Muriel
"""

from tkinter import Tk, Canvas

root = Tk()
root.title("Récupérer les tags d'un item")
cnv = Canvas(root, width=300, height=300)
cnv.pack()

cnv.create_rectangle(30, 30, 130, 130, fill="gray", tags=("A", "rect"))
cnv.create_rectangle(30, 30+150, 130,130+150, fill="gray", tags=("rect", "B"))
cnv.create_rectangle(140, 30, 170, 130, fill="orange", tags=("small rect",))

def deplacer(x):
    cnv.move("rect", x, 0)

cnv.after(1000, deplacer, 150)

root.mainloop()
