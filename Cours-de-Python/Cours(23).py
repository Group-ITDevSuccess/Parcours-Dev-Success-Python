#-------------------------------------------------------------------------------
# Name:        Les variables de contrôle
# Purpose:  Cours 23
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
import tkinter
"""
StringVar():    chaines de caractères [str]
IntVar():       nombre entier [int]
DoubleVar():    nombre flottant [float]
BoolVar():      booléen [bool]
"""
#Création de observeur (Observateur)
def update_label(*args):
    #print(f"Sexe : {var_gender.get()}")
    if var_gender.get():
        print("C'est un Homme")
        var_label_gender.set("C'est un Homme")
    else:
        print("C'est une Femme")
        var_label_gender.set("C'est une Femme")

    #var_label.set(var_entry.get())

#Création et paramétrage de la fenètre
app = tkinter.Tk()
app.geometry("400x300")
app.title("Les Variables tkinter")

#Widgets....
    #Saisie en tant reel
"""
var_entry = tkinter.StringVar()

var_entry.trace("w", update_label)

entry = tkinter.Entry(app, textvariable = var_entry)

var_label = tkinter.StringVar()
label = tkinter.Label(app, textvariable = var_label)

#var_label.set("La label...")

    #Affectation

var_label.set("Salam Alaikum")

    #Affichage

print("Label : ",var_label.get())


entry.pack()
label.pack()
"""

var_gender = tkinter.IntVar()
var_gender.trace("w", update_label)

radio1 = tkinter.Radiobutton(app, text = "Homme",value = 1, variable=var_gender)
radio2 = tkinter.Radiobutton(app, text = "Femme",value = 0, variable=var_gender)

var_label_gender = tkinter.StringVar()
label_gender =  tkinter.Label(app, textvariable = var_label_gender)

radio1.pack()
radio2.pack()
label_gender.pack()
#Boucle principal#
app.mainloop()