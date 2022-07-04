#-------------------------------------------------------------------------------
# Name:        Audio sour Tkinter avec Winsound
# Purpose:
#
# Author:      Muriel
#
# Created:     12/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

#A rétenir avec winsound
"""
Seul le format wav est pris en charge, en particulier le format mp3 n’est pas
utilisable avec winsound
"""

from tkinter import *
import winsound

def lancer():
    #Jouer le son:
    winsound.PlaySound('coran.mp3', winsound.SND_LOOP | winsound.SND_ASYNC)
    """
    Pour jouer un fichier .wav, on utilise le fonction PlaySound  qui on
    transmet le nom du fichhier et en deuxieme argument, on place des flags , ici
    un flag pour jouer en boucle et un flag pour que le flux audio ne bloque pas
    le programme principal.
    """

def couper():
    #Couper le son :
    winsound.PlaySound(None, winsound.SND_PURGE)
    """
    Pour couper(provisoirement) le son, on utlise encore le fonction Playsound
    mais avec un argument valant None
    """

def close_sound():
    couper()
    app.destroy()

app= Tk()
app.title("Audio sour Tkinter avec Winsound")

app.protocol("WM_DELETE_WINDOW",close_sound)

Button(app, text="Activer", command=lancer, width=40).pack(pady=20)
Button(app, text="Désactiver", command=couper, width=40).pack(pady=20)

app.mainloop()
