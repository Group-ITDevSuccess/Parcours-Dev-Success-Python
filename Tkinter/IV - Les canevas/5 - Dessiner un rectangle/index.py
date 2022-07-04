#-------------------------------------------------------------------------------
# Name:        Dessiner un rectangle
# Purpose:
#
# Author:      Muriel
#
# Created:     19/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root = Tk()
root.title("Mon rectangle")
cnv = Canvas(root, width=500, height=250, bg='ivory')
cnv.pack()

cnv.create_rectangle(30,70,190,170)

cnv.create_rectangle((280,40),(400,200), fill='orange', outline='blue',width=8)

root.mainloop()