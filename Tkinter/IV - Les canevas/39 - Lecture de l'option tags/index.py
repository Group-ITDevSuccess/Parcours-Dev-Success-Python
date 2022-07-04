# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:22:38 2022

@author: Muriel
"""

from tkinter import Tk, Canvas

root = Tk()
root.title("Lecture de l'option")
cnv = Canvas(root, width=200, height=200)
cnv.pack()

rect = cnv.create_rectangle(100, 100, 150, 150, fill='blue', tags=["blue", 42])

options = cnv.itemconfig(rect)

print(*options.items(), sep='\n')


root.mainloop()