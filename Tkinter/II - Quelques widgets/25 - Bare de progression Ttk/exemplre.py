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

from tkinter import Tk, ttk, StringVar, Label

root = Tk()

progress = ttk.Progressbar(root, length=400, maximum=300)
progress.pack(pady=30)

progress.start(10)

message = StringVar()

w = Label(root, textvariable = message, font='Arial 30 bold')
w.pack()

seconds = 0
delay = 1000

def anim(ms):
    message.set(str(ms//1000))
    root.after(delay, anim,ms + delay)

anim(0)

root.mainloop()