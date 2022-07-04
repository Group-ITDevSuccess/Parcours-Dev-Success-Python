# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 21:48:40 2022

@author: Muriel
"""

import sqlite3

#Connexion à la base de données:
connexion = sqlite3.connect("base.db")

#Création d'un curseur d'échange:
curseur = connexion.cursor()

#Mise à jour (INSTER, UPDATE, DELETE):
curseur.execute("INSERT INTO users(user_id, name, lastname) VALUES(2,'Fatima','FANOMEZANTSOA')")

#Validation de la modifiaction:
connexion.commit()

#Interrogation de la DB (SELECT):
curseur.execute("SELECT * FROM users;")

#Traitement du résultat:
resultat = curseur.fetchall()

curseur.close()
connexion.close()
