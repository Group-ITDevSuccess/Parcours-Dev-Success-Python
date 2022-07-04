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
root.title("Mon polygone")
cnv = Canvas(root, width=300, height=200, bg='ivory')
cnv.pack()

A = 50,50
B = 100,120
C = 150,10
D = 40,150

cnv.create_polygon(A,B,C,D, fill='lavender',outline='red')

root.mainloop()
