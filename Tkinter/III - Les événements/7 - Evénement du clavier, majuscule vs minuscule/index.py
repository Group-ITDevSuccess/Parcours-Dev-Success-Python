#-------------------------------------------------------------------------------
# Name:        Evénement du clavier, majuscule vs minuscule
# Purpose:
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

from tkinter import Tk, Canvas

root= Tk()
root.title("Majuscule vs Minuscule")
cnv= Canvas(root, width=400, height=100, bg="ivory")
cnv.pack(padx=10,pady=10)
cnv.focus_set()
x = 0

def texte(event):
    global x
    cnv.create_text(x, 40, text=event.keysym, font="Arial 50 bold")
    x+=30

cnv.bind('<Key-a>', texte)
cnv.bind('<Key-B>', texte)

root.mainloop()