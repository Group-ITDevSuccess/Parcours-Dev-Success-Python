#-------------------------------------------------------------------------------
# Name:        Extrémité, jonction de segment
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

cnv.create_line(20,20,180,20, width=15)
cnv.create_line(180,20,180,180, width=15)

cnv.create_line(380,20,220,20, width=15, capstyle=ROUND)
cnv.create_line(220,20,220,180, width=15, capstyle=ROUND)


root.mainloop()