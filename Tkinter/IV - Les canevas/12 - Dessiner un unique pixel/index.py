#-------------------------------------------------------------------------------
# Name:        module1
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

root = Tk()
root.title("Mon pixel")
cnv = Canvas(root, width=250, height=250, bg='ivory')
cnv.pack()

cnv.create_rectangle(100,100,100,100, fill='orange', outline='')

root.mainloop()