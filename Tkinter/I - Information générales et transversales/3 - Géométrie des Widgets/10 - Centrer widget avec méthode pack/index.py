#-------------------------------------------------------------------------------
# Name:        Center widget avec méthode pack
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

app = Tk()
app.title("Center widget avec méthode pack")

cnv = Canvas(app, width=300, height=200, bg="orange")
cnv.pack(side='left')

button =Button(app, text="Bouton")
button.pack(side="left")

app.mainloop()