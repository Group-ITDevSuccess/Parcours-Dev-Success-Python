#-------------------------------------------------------------------------------
# Name:        Bord, intérieur et dimensions exactes d'un rectangle
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
cnv = Canvas(root, width=130, height=250, bg='ivory' )
cnv.pack()

cnv.create_rectangle(10, 10, 110, 110, fill='light blue')
cnv.create_rectangle(10, 113, 110, 223, fill='light blue', outline='')

root.mainloop()