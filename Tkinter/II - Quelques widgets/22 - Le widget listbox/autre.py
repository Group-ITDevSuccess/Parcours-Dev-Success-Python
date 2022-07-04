#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     15/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

fruits = ["Litchie","Kiwi","Orange","Raisin","Citron","Cerise"]
n =len(fruits)

master = Tk()

lbox = Listbox(master,
     width=8,
     height=n,
     font="Verdana 20 bold",
     selectbackground="lightgreen")
lbox.pack(padx=20, pady=20)

for item in fruits:
    lbox.insert(END, item)

lbox.focus_set()
lbox.select_set(2)

for i in range(0, len(fruits), 2):
    lbox.itemconfigure(i, bg='#f0f0f0')

for i in range(1, len(fruits), 2):
    lbox.itemconfigure(i, bg='#fff')

master.mainloop()