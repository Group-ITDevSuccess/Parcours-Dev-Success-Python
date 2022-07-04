#-------------------------------------------------------------------------------
# Name:        Le variables dynamique IntVar
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
root.title("Le variables dynamique IntVar")

total = IntVar()
#total = Intvar(value=42)

def incr():
    total.set(total.get()+1)

def decr():
    total.set(total.get()-1)

btn_plus = Button(root, height=5, text="+",command=incr)
btn_plus.pack(padx=5, pady=5)

btn_moins = Button(root, height=5, text="+",command=decr)
btn_moins.pack(padx=5, pady=5)

msg= Label(root, height=5, width=20, textvariable=total)
msg.pack(padx=5,pady=5)

root.mainloop()