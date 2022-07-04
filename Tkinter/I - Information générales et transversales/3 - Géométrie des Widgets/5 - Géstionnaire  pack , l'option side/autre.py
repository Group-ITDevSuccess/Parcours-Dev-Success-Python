#-------------------------------------------------------------------------------
# Name:        Se placer de gauche à droite
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
root.title("Se placer de gauche à droite")

Label(bg="white", width=5, height=2, text="1", font="arial 30").pack(side=LEFT)
Label(bg="red", width=5, height=2, text="2", font="arial 30").pack(side=LEFT)
Label(bg="green", width=5, height=2, text="3", font="arial 30").pack(side=LEFT)

root.mainloop()