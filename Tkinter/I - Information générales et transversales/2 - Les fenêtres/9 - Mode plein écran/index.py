#-------------------------------------------------------------------------------
# Name:        Mode plein écran
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

SIDE = 1000

def normalscreen(event):
    master.attributes("-fullscreen", False)

master =Tk()
master.title("Mode plein écran")

master.attributes("-fullscreen",True)

cnv = Canvas(master, width = SIDE, height=(1.3*SIDE), bg='ivory')
cnv.pack()

master.bind("<Escape>",normalscreen)

master.mainloop()