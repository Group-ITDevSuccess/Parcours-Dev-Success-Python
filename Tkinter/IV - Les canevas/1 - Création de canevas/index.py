#-------------------------------------------------------------------------------
# Name:        Création de canevas
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

root= Tk()
root.title("Création de canevas")
cnv= Canvas(root,width=600, height=400, bg='ivory')
cnv.pack(padx=10,pady=10)

root.mainloop()