#-------------------------------------------------------------------------------
# Name:        Introduction au tkinter
# Purpose:  Cours 20
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#coding:utf-8

"""
mainapp.quit() #Quiter la fenetre

"""
import tkinter
#from tkinter import *

"""
Créer un fenetre


#Propriéte sur le fenetre

#mainapp.minsize(640,480)
#mainapp.maxsize(750,580)
#mainapp.geometry("800x600")
#mainapp.positionfrom("user")
#mainapp.sizefrom("user")
#mainapp.resizable(width = False, height = True)

#Geometry("XxY+0+0")
#mainapp.geometry("400x300+50+100")
#Centrer une fenetre
"""
"""
position_X = (largeur_ecran // 2) - (largeur_fenetre //2)
position_Y = (hauteur_ecran // 2) - (hauetr_fenetre //2)
"""

mainapp = tkinter.Tk()
mainapp.title("Mon prémier programme")

screen_x = int(mainapp.winfo_screenwidth())
screen_y = int(mainapp.winfo_screenheight())
window_x = 500
window_y = 400

pos_X = (screen_x // 2) - (window_x // 2)
pos_Y = (screen_y // 2) - (window_y // 2)

geo = "{}x{}+{}+{}".format(window_x,window_y,pos_X, pos_Y)
mainapp.geometry(geo)

#Faire un boucle infinie pour affichier la fenetre
mainapp.mainloop()
