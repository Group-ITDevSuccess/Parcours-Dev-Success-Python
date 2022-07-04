#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from tkinter import font as tkfont, Tk, Canvas

root = Tk()

canvas = Canvas(root, width=500, height=500, bg="ivory")
canvas.pack()

my_font = tkfont.Font(family="cmsy10")

lettre = "Portez ce vieux whisky au juge blond qui fume"

text=canvas.create_text(420,100,fill="black", font = my_font,text=lettre)

root.mainloop()