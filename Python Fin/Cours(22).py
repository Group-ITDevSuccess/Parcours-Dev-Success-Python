#-------------------------------------------------------------------------------
# Name:        Les widgets avancés
# Purpose:  Cours 22
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
import tkinter
from tkinter import messagebox

app = tkinter.Tk()
"""
check_widget = tkinter.Checkbutton(app, text= "Valider", offvalue=2, onvalue=1)

radio_widget1 = tkinter.Radiobutton(app, text="Home", value = 1)
radio_widget2 = tkinter.Radiobutton(app, text="Fermer", value = 2)

scale_w = tkinter.Scale(app, from_=10, to=100) #tickinterval = 25
spain_w = tkinter.Spinbox(app, from_=1, to=10)

lb = tkinter.Listbox(app)

lb.insert(1, "Windows")
lb.insert(2, "GNU/Linux")
lb.insert(3, "MacOS")
lb.insert(4, "Android")

check_widget.pack()
radio_widget1.pack()
radio_widget2.pack()
scale_w.pack()
spain_w.pack()
lb.pack()
"""

#Créer un fentre modal
"""
showerror
showinfo
showwarning
askquestion
askretrycancel
askokcancel
askyesnocancel
askyesno
"""
def show_modal_window():
    messagebox.askokcancel("ERREUR","Une problème est survenu")

btn = tkinter.Button(app, text= "Decencher une erreur", command=show_modal_window)

btn.pack()
app.mainloop()

