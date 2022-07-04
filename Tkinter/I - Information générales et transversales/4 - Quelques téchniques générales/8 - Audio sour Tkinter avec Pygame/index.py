#-------------------------------------------------------------------------------
# Name:        Audio sous Tkinter avec Pygame
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

#On importe Pygame
import pygame

#Pré-initialisation
pygame.mixer.pre_init(44100, -16, 1, 512)
"""
Les valeurs ci-dessous ont été retranscrises d’une réponse sur StackOverFlow.
"""

#On initialise le module mixer de Pygame (le module qui gère le son)
pygame.mixer.init()

#On charge le fichier dont on veut écouter le flux audio en indiquant l’adresse du fichier
monAudio=pygame.mixer.Sound("coran.mp3")

def lancer():
#Le volume du son
"""
La méthode set_volume accepte en un argument un nombre fottant entre 0 (aucun son) et 1
(son d’intensité maximale), donc 0.5 correspond à une intensité médiane
"""
     monAudio.set_volume(1)

#Jouer le son
"""
Le son est joué (fonction play). L’argument -1 a pour effer que le flux audio est joué
en boucle, indéfiniment si on ne l’interrompt pas. Le volume par défaut est maximal.
"""
    monAudio.play()

def couper():
#Interruption du ux audio
    monAudio.stop()

#on quittera Pygame avec la fonction dédiée quit
def quitter():
    pygame.quit()
    app.destroy()

app = Tk()
app.title("Audio sous Tkinter avec Pygame")

Button(app, text="Lancer", command=lancer, width=40).pack(pady=20)
Button(app, text="Couper", command=couper, width=40).pack(pady=20)

#Couper  le son en même temp que la fermetur de interface
app.protocol("WM_DELETE_WINDOW", quitter)
"""
Cette ligne détecte une tentative de fermeture de la fenêtre en cliquant sur la croix.
Fermer la fenêtre est l’événement "WM_DELETE_WINDOW". Lorsque cet événement est détecté
par Tkinter, la fonction quitter sera automatiquement appelée.
"""

app.mainloop()