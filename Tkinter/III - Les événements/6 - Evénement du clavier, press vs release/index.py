#-------------------------------------------------------------------------------
# Name:        Evénement du clavier, press vs release
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

root = Tk()
root.title("Press vs Release")

def press(event):
    print("press", event.keysym)
def release(event):
    print("release", event.keysym)

root.bind('<KeyPress>', press)
root.bind('<KeyRelease>', release)

root.mainloop()