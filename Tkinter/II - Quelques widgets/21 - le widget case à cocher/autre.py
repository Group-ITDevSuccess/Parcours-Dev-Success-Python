#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
from tkinter import *

root = Tk()

def update(*args):
    s = sum(check["text"]*v.get() for (check,v) in checks)
    lbl["text"] = "Somme : %s" %s

checks =[]

for i in range(3):
    v =IntVar()
    check = Checkbutton(root, text = i +2,font='Arial 30', variable=v)
    check.grid(row=i)

    #L’argument "w" de trace signie write (modication en écriture de v).
    v.trace("w",update)
    checks.append((check,v))

lbl = Label(root, text ="Somme : 0",font='Arial 30')
lbl.grid(row = 1,column = 1,padx=100)

root.mainloop()

