#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

root= Tk()

def play():
    b['text'] ='ABCDEFGHIJKLM'

b = Button(root, text = "Play", command=play, width=5)
b.pack(padx=50, pady=20)

root.mainloop()