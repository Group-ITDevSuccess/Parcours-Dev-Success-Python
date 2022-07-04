# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 23:34:44 2022

@author: Muriel
"""
import sqlite3


try:
    connexion = sqlite3.connect("data.db")
    curseur = connexion.cursor()
    curseur.execute('''CREATE TABLE IF NOT EXIST scores(id INTGER PRIMARY KEY AUTOINCREMENT UNIQUE, pseudo TEXT, valeur INTEGER)''')
    
    connexion.commit()
    
except:
    print("Connexion echouer  !")
finally:
    connexion.close()
