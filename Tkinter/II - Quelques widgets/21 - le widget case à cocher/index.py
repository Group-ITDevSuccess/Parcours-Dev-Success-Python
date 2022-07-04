#-------------------------------------------------------------------------------
# Name:        Le case ра cocher
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# coding:utf-8

from tkinter import *

root = Tk()
root.title("Le case ├а cocher")

def f(i):
    def g():
        s = sum(check["text"] * v.get() for (check, v) in checks)
        lbl["text"] = "Somme : %s" %s
    return g

checks =[]

for i in range(3):
    v = IntVar()
    check = Checkbutton(
          root, text = i + 2,
          font='Arial 30',
          command = f(i),
          variable=v)
    check.grid(row=i)
    checks.append((check, v))

lbl = Label(root, text="Somme : 0", font='Arial 30')
lbl.grid(row=1,column=1,padx=100)

root.mainloop()