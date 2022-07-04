#-------------------------------------------------------------------------------
# Name:        Menu avec Python
# Purpose:
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
import tkinter

#Les fonctions
def show_about():
    about_window = tkinter.Toplevel(app)
    about_window.title("A propos")
    about_window.geometry("200x150")
    lb = tkinter.Label(about_window, text = "Salam Alaikum ....")
    lb.pack()
#Creation et modélisation du widget
app = tkinter.Tk()
app.geometry("460x350")
app.title("Création de ménu avec tkinter")

#widget ...

    #Widget de Menu
mainmenu = tkinter.Menu(app)

first_menu = tkinter.Menu(mainmenu, tearoff = 0)

first_menu.add_command(label = "Nouveau")
first_menu.add_command(label = "Ouvrir")
first_menu.add_separator()
first_menu.add_command(label = "Fermer", command = app.quit)

second_menu = tkinter.Menu(mainmenu, tearoff = 0)

second_menu.add_command(label = "Fait de don")
second_menu.add_command(label = "A Propos de ...", command = show_about)

mainmenu.add_cascade(label = "Fichier", menu = first_menu)
mainmenu.add_cascade(label = "Aide", menu = second_menu)

#Boucle infine d'affichage de widget
app.config(menu = mainmenu)
app.mainloop()