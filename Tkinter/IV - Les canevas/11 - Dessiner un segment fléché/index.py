#-------------------------------------------------------------------------------
# Name:        Dessiner un segment fléché
# Purpose:
#
# Author:      Muriel
#
# Created:     20/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk,Canvas

root = Tk()
root.title("Dessiner un segment fléché")
cnv = Canvas(root, width=200, height=200, bg='ivory')
cnv.pack()

cnv.create_line(40,50,140,50, width=5, arrow='both')

cnv.create_line(50,60,150,60, width=5, arrow='last')

cnv.create_line(60,70,160,70, width=5, arrow='first')


root.mainloop()