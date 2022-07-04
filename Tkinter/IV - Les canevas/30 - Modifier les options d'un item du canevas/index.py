#-------------------------------------------------------------------------------
# Name:        Modifier les options d'un item du canevas
# Purpose:
#
# Author:      Muriel
#
# Created:     20/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
from tkinter import Tk, Canvas

def action():
    cnv.itemconfigure(rect, fill="lavender")

root = Tk()
root.title("Modifier les options d'un item du canevas")
cnv = Canvas(root, width=500, height=500, bg='ivory')
cnv.pack(padx=10,pady=10)

rect = cnv.create_rectangle(30,30,430,430, fill="pink", outline="green")

cnv.after(1000, action)

root.mainloop()