#-------------------------------------------------------------------------------
# Name:        Introduction au Tkinter
# Purpose:
#
# Author:      Muriel
#
# Created:     11/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *
from random import randrange

def tracer():
    cnv.delete("all")
    u, v = randrange(SIDE), randrange(SIDE)
    R = SIDE//4
    cnv.create_oval(u-R, v-R, u+R, v+R, fill = 'orange')

def msg():
    lbl["text"] = "Occupé !"

def calcul():
    z = 10**6000000
    lbl["text"] = "Libre !"
SIDE = 400

root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE, background="ivory")
cnv.pack(side=LEFT)

button = Button(root, text ="Tracer", command=tracer)
button.pack()

lbl = Label(root, text = "Libre !", font="Times 12 bold")
lbl.pack(pady=30)

root.after(4990,msg)
root.after(5000,calcul)

root.mainloop()
print("Salam Alaikum")