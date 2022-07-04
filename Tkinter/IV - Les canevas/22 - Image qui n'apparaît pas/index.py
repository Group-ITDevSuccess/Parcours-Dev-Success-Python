#-------------------------------------------------------------------------------
# Name:        Image qui n'apparaît pas
# Purpose:
#
# Author:      Muriel
#
# Created:     20/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
from tkinter import *

def run():
    root = Tk()
    cnv = Canvas(root, width=200, height=200)
    cnv.pack()
    photo(cnv)
    root.mainloop()

def photo(cnv):
    test =PhotoImage(file="devsuccess.png")
    cnv.create_image(100, 100, image=test)
    cnv.create_rectangle(100, 100, 150,150,fill="orange")

run()
