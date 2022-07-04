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

root = Tk()

def animer(i):
    if i < 5:
       print(i)
       L['text'] = "Encore !"
       root.after(500, animer, i+1)
    if i == 5:
       L.configure(text = L['text'] + 'FIN')

L = Label(root, text = "Encore !")
L.pack(padx=50, pady=20)

animer(0)

root.mainloop()