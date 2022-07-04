#-------------------------------------------------------------------------------
# Name:        Dessiner  une segment
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
root.title("Mon segment")
cnv = Canvas(root, width=200, height=200, bg='ivory')
cnv.pack()

A = (50,60)
B = (150,100)
C = (30,140)
D = (150,180)

cnv.create_line(A, B)

cnv.create_line(60,70,160,70, width=8, fill = "red")

cnv.create_line(A,B,C,D, width=5, fill = "green")

root.mainloop()