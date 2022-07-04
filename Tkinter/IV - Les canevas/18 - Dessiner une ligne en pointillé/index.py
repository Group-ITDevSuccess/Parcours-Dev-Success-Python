#-------------------------------------------------------------------------------
# Name:        Dessiner une ligne en pointillé
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
root.title("Dessiner une ligne en pointillé")
cnv = Canvas(root, width=200, height=200, bg='ivory')
cnv.pack()

cnv.create_line(0,100,200,0, fill="red",dash=(4,4))

root.mainloop()