#-------------------------------------------------------------------------------
# Name:        Codes de quelques touches
# Purpose:
#
# Author:      Muriel
#
# Created:     16/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root = Tk()
root.title("Codes de quelques touches")

def f(event):
    print("Ok")

root.bind('<Control-Shift-KeyPress-a>',f)

root.mainloop()