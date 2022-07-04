#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     21/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

SIDE = 400
item = None

root = Tk()
cnv = Canvas(root, width=SIDE, height=SIDE, bg='ivory')
cnv.pack()

item = cnv.create_text(SIDE/2, SIDE/2, text="2024", font="Arial 100 bold")

print(cnv.bbox(item))

root.mainloop()