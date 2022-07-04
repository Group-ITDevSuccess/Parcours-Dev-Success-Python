#-------------------------------------------------------------------------------
# Name:        Cacher, montrer des itmes sur le canevas
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

def hide_my_rect():
    cnv.itemconfigure(rect, state="hidden")

def show_my_rect():
    cnv.itemconfigure(rect, state="normal")

root = Tk()
root.title("Cacher, montrer des itmes sur le canevas")
cnv = Canvas(root, width=350, height=350, bg='ivory')
cnv.pack(padx=10,pady=10)

rect = cnv.create_rectangle(30,30,270,270,fill="red")

cnv.after(1500, hide_my_rect)
cnv.after(3000, show_my_rect)

root.mainloop()