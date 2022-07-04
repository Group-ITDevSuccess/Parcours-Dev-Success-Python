#-------------------------------------------------------------------------------
# Name:        L'option side
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
root.title("L'option side")

Label(bg="red",width=30, height=2, text="1", font="arial 30").pack(side=BOTTOM)
Label(bg="purple",width=20, height=2, text="2", font="arial 30").pack()
Label(bg="green",width=40, height=2, text="3", font="arial 30").pack()
Label(bg="pink",width=15, height=2, text="4", font="arial 30").pack(side=RIGHT)
Label(bg="orange",width=25, height=2, text="5", font="arial 30").pack(side=LEFT)
Label(bg="lightblue",width=25, height=2, text="6", font="arial 30").pack()
Label(bg="lavender",width=5, height=2, text="7", font="arial 30").pack(side=RIGHT)



root.mainloop()