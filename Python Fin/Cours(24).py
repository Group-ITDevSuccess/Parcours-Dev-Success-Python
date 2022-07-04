#-------------------------------------------------------------------------------
# Name:        Positionnement des widgets
# Purpose:  Cours 24
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
import tkinter

#Création et parametrage de la fenetre
app = tkinter.Tk()
app.geometry("640x480")
app.title("Positionnement des widgets")

#Widgets...

#Cadre
"""
mainframe = tkinter.Frame(app,width = 300, height = 200, borderwidth=1)
#mainframe = tkinter.LabelFrame(app,text="Titre", width = 300, height = 200, borderwidth=1)
mainframe.pack()

btn = tkinter.Button(mainframe, text = "Envoyer")
btn.pack()
"""

label = tkinter.Label(app, text = "Un Label")
entry = tkinter.Entry(app)
btn = tkinter.Button(app, text = "Envoyer")

label.place(x = 100, y = 10)
entry.place(x = 100, y = 55)
btn.place(x = 100, y = 95)

    #"Avec Grid(...)":
"""
label.grid()
entry.grid()
btn.grid()

    row = ..., column= ...
    padx = ..., pady = ..
    ipadx = ..., ipady = ...
    columnspan = ...
    rowspan = ...
    sticky =" n ou s ou e ou w"
        exmple : grid(sticky = "ne")

"""
    #"Avec Pack(...)":
"""
label.pack()
entry.pack()
btn.pack(padx = 100, pady = 10)

    side = "top",... Ou expend = 1
    fill = "y ou x ou both", padx = ..., pady = ..
    ipadx = ..., ipady = ...
    Boucle infinie
"""
app.mainloop()