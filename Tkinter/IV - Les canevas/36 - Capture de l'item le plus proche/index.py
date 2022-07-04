# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 20:55:19 2022

@author: Muriel
"""

from tkinter import *

COTE = 30
WIDTH=20*COTE
HEIGHT=20*COTE

root = Tk()
root.title("Cpture de l'item le plus proche !")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
cnv.pack()

n = WIDTH//COTE

for i in range(n):
    for j in range(n):
        cnv.create_line(i*COTE, j*COTE, i*COTE+COTE,j*COTE, fill='red', width=4)
        cnv.create_line(j*COTE, i*COTE, j*COTE,i*COTE+COTE, fill='red', width=4)
    
def suppr(event):
    clic = event.x, event.y
    bord=cnv.find_closest(*clic)
    cnv.delete(bord)

cnv.bind("<Button-1>",suppr)

root.mainloop()