#-------------------------------------------------------------------------------
# Name:        Image dans un label
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

root = Tk()
root.title("Mon label avec un image")

logo = PhotoImage(file="devsuccess.png") #ne prend pas en charge les .ico

#Si l’option image est utilisée, l’option text sera sans effet
Label(root, image = logo).pack(padx=15, pady=15)

root.mainloop()