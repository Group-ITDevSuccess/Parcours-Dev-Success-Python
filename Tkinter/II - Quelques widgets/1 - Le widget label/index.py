#-------------------------------------------------------------------------------
# Name:        Le widget label
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
root.title("Le widget label")
lbl = Label(root, text="Salam Alaikum", font='Arial 30 bold')
lbl.pack(padx=15, pady=15)

root.mainloop()