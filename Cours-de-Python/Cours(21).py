#-------------------------------------------------------------------------------
# Name:        Prémier widgets
# Purpose:  Cours 21
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
"""
<nom_variable> = <nom_widget>(<widget_parent>, <params>,...)

"""
import tkinter

def hello():
    print("Salam Alaikum Muriel")
app = tkinter.Tk()

message = "Salam Alaikum !"
#label_welcome = tkinter.Label(app, text = message)
#Afficher le contetnue dans le widget
"""
print(label_welcome["text"])
#Ou
print(label_welcome.cget("text"))
"""
#Modifier le contenue de widget
"""
label_welcome["text"] = "Bonjour a tous"
#Ou
label_welcome.configure(text="Salam Alaikum Muriel")
"""
#label_welcome.pack()
"""
message_welcome = tkinter.Message(app, text = message)
message_welcome.pack()
"""
#Saisir
"""
entry_name = tkinter.Entry(app) #Entry(app, width = 45, show="*")
entry_name.pack()
"""
#Bouton


button_quit = tkinter.Button(app, text="Ok", command=hello)
button_quit.pack()


app.mainloop()