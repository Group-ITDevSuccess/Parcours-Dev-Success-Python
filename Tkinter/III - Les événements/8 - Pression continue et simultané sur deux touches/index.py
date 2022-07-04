#-------------------------------------------------------------------------------
# Name:        Pression continue et simultané sur deux touches
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
from time import time

root=Tk()
root.title("Pression continue et simultané sur deux touches")

def press(event):
    print("press", event.keysym, time())

def release(event):
    print("release", event.keysym, time())

for key in ["a","z"]:
    root.bind('<KeyPress-%s>' %key, press)
    root.bind('<KeyRelease-%s>' %key, press)

root.mainloop()