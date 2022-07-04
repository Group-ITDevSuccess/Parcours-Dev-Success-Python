#-------------------------------------------------------------------------------
# Name:        Le widget Frame
# Purpose:
#
# Author:      Muriel
#
# Created:     14/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import *

SIDE = 400
root=Tk()
root.title("Le widget Frame")

frame = Frame(root, bg='lavender')
frame.pack()
cnv = Canvas(frame, width=SIDE, height=SIDE, bg='ivory')
cnv.pack(padx=20,pady=20)

btn = Button(frame,text = "Activer")
btn.pack(pady=20)

root.mainloop()