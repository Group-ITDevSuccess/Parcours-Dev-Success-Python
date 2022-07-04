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

WIDTH = 400
HEIGHT = 300

root = Tk()
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg='ivory')
cnv.pack()

triangle = cnv.create_polygon(50,50,300,250,390,10)

print(cnv.coords(triangle))

root.mainloop()