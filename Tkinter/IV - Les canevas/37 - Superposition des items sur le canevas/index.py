# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 21:12:03 2022

@author: Muriel
"""

from tkinter import *
from random import randrange, sample

WIDTH=600
HEIGHT=600
COTE =150

root= Tk()
root.title("Superposer de widget entre elle !")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
cnv.pack()
x=y=100

rect1 = cnv.create_rectangle(x, y, x+COTE, y+COTE, fill="red", outline='')
rect2 = cnv.create_rectangle(x+1.25*COTE, y, x+2*COTE, y+2*COTE, fill="gray", outline='')

x=x+COTE/2
y=y+COTE/2
rect3 = cnv.create_rectangle(x, y, x+COTE, y+COTE, fill="green", outline='')

x=x+COTE/2
y=y+COTE/2
rect4 = cnv.create_rectangle(x, y, x+COTE, y+COTE, fill="blue", outline='')

print(cnv.find_all())

def f():
    cnv.tag_raise(rect2,rect4)
    print(cnv.find_all())
    
cnv.after(1000, f)

root.mainloop()