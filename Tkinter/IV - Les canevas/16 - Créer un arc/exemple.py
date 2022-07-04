#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     20/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

WIDTH=400
HEIGHT=300

root=Tk()
root.title("Mon arc !")
cnv = Canvas(root, width=WIDTH, height=HEIGHT, bg='ivory')
cnv.pack()
x = 30
y = 20
COTEx = 100
COTEy = 180

cnv.create_arc(x,y,x+COTEx,y+COTEy, extent=210,start=-20, width=2)

x+=20+COTEx
cnv.create_arc(x,y,x+COTEx,y+COTEy, extent=210,start=-20, width=2, style=ARC)

x+=20+COTEx
cnv.create_arc(x,y,x+COTEx,y+COTEy, extent=210,start=-20, width=2, style=CHORD)


root.mainloop()