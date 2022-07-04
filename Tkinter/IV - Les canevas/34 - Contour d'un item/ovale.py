#-------------------------------------------------------------------------------
# Name:        Contour d'un item
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

ellipse = cnv.create_oval(200,250,350,100)

print(cnv.coords(ellipse))

root.mainloop()