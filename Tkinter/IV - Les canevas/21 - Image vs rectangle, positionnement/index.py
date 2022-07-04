#-------------------------------------------------------------------------------
# Name:        Image vs rectangle, positionnement
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

side = 120

root= Tk()
root.title("Image vs rectangle : Positionnement")
cnv= Canvas(root, width=5*side,height=5*side, bg='lavender')
cnv.pack()

a =side
teste = PhotoImage(file="devsuccess.png")
cnv.create_image(a,a,image=teste)

cnv.create_image(a,a,image=teste, anchor=NW)
cnv.create_rectangle(a,a, a+50, a+50, fill="red")

root.mainloop()