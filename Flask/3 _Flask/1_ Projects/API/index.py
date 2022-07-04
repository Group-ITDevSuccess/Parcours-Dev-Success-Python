# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 23:43:52 2022

@author: Muriel
"""
import flask 

#Crée l'objet application Flask
"""
Il contient les données de l'application et les méthodes correspondant au action susceptible d'être effectuées sur l'objet.'
"""
app = flask.Flask(__name__)

#Lancer le débugueur:
"""
Ce qui permet d'afficher un message autre que 'Bad Gateway' s'il y a une erreur dans l'applicaton'
"""
app.config["DEBUG"] = True

#Le route:
@app.route('/', methods=['GET'])

def home():
    return " <h1>Mon Page avec flask</h1>"

#Instruction app.run() est une exmple d'utilisation de méthode. (permert d'exécuter l'application) 
app.run()
