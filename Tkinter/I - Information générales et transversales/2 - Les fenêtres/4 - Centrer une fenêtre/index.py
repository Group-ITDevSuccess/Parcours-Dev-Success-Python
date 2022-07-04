#-------------------------------------------------------------------------------
# Name:        Centrer une fenêtre
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

import tkinter as tk

root = tk.Tk() #Create a Tk root Windows
root.title("Centrer une fenêtre")

w = 800 #width for the Tk root
h = 600 #height for the Tk root

ws = root.winfo_screenwidth() #Width of the scree
hs = root.winfo_screenheight() #height of the scree

#Calculate x annd y coordinates for the Tk root windows
x = (ws/2) -(w/2)
y = (hs/2) -(h/2)

#Set the dimensions of the screen and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root.mainloop() #Start the mainloop