# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 15:29:27 2022

@author: Muriel
"""


from tkinter import Tk, Canvas

root = Tk()
root.title("Récupérer les tags d'un item")
cnv = Canvas(root, width=200, height=200)
cnv.pack()

rect1 = cnv.create_rectangle(10, 10, 50, 50, fill="red", tags=("red", 24))

rect2 = cnv.create_rectangle(100, 100, 150, 150, fill="blue", tags=["blue", 42])

print(cnv.gettags(rect2))

root.mainloop()