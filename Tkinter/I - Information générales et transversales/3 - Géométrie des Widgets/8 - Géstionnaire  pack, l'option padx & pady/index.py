#-------------------------------------------------------------------------------
# Name:        Les options padx et pady
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root=Tk()
root.title("Les options padx et pady")

cnv= Canvas(root, width=300, height=200, bg="yellow")
cnv.pack(padx=150, pady=100)

root.mainloop()