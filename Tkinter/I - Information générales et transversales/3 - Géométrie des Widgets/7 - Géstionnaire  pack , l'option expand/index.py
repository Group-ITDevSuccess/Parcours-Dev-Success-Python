#-------------------------------------------------------------------------------
# Name:        L'option expand
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

root = Tk()
root.title("L'option expand")

Label(root, text = "Label 1", bg="green", height=10).pack(side='left')
Label(root, text = "Label 2", bg="lightblue").pack(fill=Y, expand=True)

root.mainloop()