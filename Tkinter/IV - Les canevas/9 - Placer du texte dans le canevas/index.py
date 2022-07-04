#-------------------------------------------------------------------------------
# Name:        Placer du texte dans un canevas
# Purpose:
#
# Author:      Muriel
#
# Created:     19/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

WIDTH = 400
HEIGHT = 300

root = Tk()
root.title("Mon texte dans le canevas")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg="ivory")
cnv.pack(padx=10, pady=10)

C = (WIDTH//2, HEIGHT//2)

cnv.create_text(C, anchor = CENTER, text="Salam Alaikum", fill="blue",
                   font="Arial 30 bold")

root.mainloop()