#-------------------------------------------------------------------------------
# Name:        Bord d'un rectangle
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
cnv = Canvas(root, width=480, height=120, bg='ivory' )
cnv.pack()

cnv.create_rectangle(10, 10, 110, 110, fill='light blue')
cnv.create_rectangle(120, 10, 220, 110, fill='light blue', outline='')
cnv.create_rectangle(230, 10, 340, 110, fill='light blue', outline='red')
cnv.create_rectangle(350, 10, 460, 110, fill='light blue', outline='light blue')

root.mainloop()