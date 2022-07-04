#-------------------------------------------------------------------------------
# Name:        Le widget spinbox
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
root=Tk()
root.title("Mon spinbox pour les années")

sp = Spinbox(root, from_=2000, to = 2022)
sp.pack(padx=10, pady=10)

root.mainloop()