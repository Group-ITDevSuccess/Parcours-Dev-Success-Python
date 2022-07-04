#-------------------------------------------------------------------------------
# Name:         Image sur un bouton
# Purpose:
#
# Author:      Muriel
#
# Created:     13/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()
logo = PhotoImage(file="halal_sign_60px.png")
btnA = Button(root, image = logo, bg='yellow')
btnA.pack(padx=10,pady=10)
btnB = Button(root, width=50, height=50, image = logo,bg='lightgreen')
btnB.pack(padx=10,pady=10)

root.mainloop()