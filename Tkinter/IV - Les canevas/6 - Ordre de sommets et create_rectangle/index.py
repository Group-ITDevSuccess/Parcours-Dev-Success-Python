#-------------------------------------------------------------------------------
# Name:        Ordre de sommets et create_rectangle
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
root.title("Mon rectangle")
cnv = Canvas(root, width=400, height=400, bg='ivory')
cnv.pack()


cnv.create_rectangle((50,50),(150,100), fill='orange', outline='')
cnv.create_rectangle((250,150),(350,50), fill='green')

cnv.create_rectangle((150,300),(50,250), fill='orange')
cnv.create_rectangle((350,250),(250,350), fill='brown', outline='')

root.mainloop()