#-------------------------------------------------------------------------------
# Name:        Evénement du clavier
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

def touche(event):
    t = event.keysym
    print("Touche %s pressée ! " %t)

root = Tk()
root.title("Evenement du clavier")

root.bind('<Key>', touche)

root.mainloop()