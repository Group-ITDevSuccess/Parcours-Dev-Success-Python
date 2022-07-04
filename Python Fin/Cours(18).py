#-------------------------------------------------------------------------------
# Name:        Les dictionnaires
# Purpose:  Cours 18
#
# Author:      Muriel
#
# Created:     06/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

"""
Création de dictionnaire:
    dico = {}    #Vide
    dico = {<cle1>:<valeur>, <cle2><valeur>}
(!) La clé d'un dictionnaire peut être un tuple
    dico[(2,3)] = "ok"
Accès à une valeur :
    dico[<clé>]

Ajout et modification :
    dico[<clé>] = <valeur>

Suppression :
    * Par méthode:
        dico.pop(<clé>)
    * Utliser del
        del dico[<clé>]

Parcourir un dictionnaire :
    *pour le clé:
        for truc in dico.key():
            print(truc)
    *pour le valeur :
        for truc in dico.values():
            print(truc)
    *les deux :
        for key, valeur in dico.items():
    print("Clé : {} - Valeur : {} ".format(key,valeur))

Copy de dictionnaire :
    dico2 = dico.copy()
Fonction avec de parametre nommée:
    **  : parametre nommé
    *   : parametre variable
"""

dico = {"chat":"C'est un félin", "chien":"C'est un animal"}

def maFonction(**parametres): # Parametre nommée
    print(parametres)

maFonction(age = 14, nom ="Muriel")