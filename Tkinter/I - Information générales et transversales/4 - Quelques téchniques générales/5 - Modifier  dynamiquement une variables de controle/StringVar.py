#-------------------------------------------------------------------------------
# Name:        Le variables dynamique StringVar
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

root = Tk()
root.title("Le variables dynamique StringVar")

msg= StringVar()

entree = Entry(root, textvariable=msg)
entree.pack(padx=20, pady=10)

lbl=Label(root, textvariable=msg, bg="#812",width=10)
lbl.pack(padx=20, pady=10)

root.mainloop()