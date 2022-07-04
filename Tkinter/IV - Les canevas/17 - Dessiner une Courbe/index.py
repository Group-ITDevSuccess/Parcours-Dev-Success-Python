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

from tkinter import Canvas, Tk
#from tkinter import * # For Python 3.2.3 and higher.
root = Tk()
root.title('Une courbe')

cw = 250 # canvas width
ch = 200 # canvas height
canvas_1 = Canvas(root, width=cw, height=ch, background="pink")
canvas_1.grid(row=0, column=1)

x1 = 50
y1 = 10
x2 = 50
y2 = 180
x3 = 180
y3 = 180

canvas_1.create_line(x1,y1, x2,y2, x3,y3, smooth="true", width= 2)

root.mainloop()