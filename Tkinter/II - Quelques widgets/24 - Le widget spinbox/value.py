#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     16/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

def f():
    print(sp.get())

root = Tk()

fruits = ["Litchie","Kiwi","Orange","Raisin","Citron","Cerise"]

sp = Spinbox(
   root,
   values = fruits,
   width=8,
   justify=CENTER,
   wrap=True,
   font="times 30",
   state="readonly",
   readonlybackground="white",
   command=  f)
sp.pack(padx=10, pady=10)

root.mainloop()