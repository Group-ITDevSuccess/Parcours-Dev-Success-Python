#-------------------------------------------------------------------------------
# Name: introduction au python, coder un premier programme, les variables
# Purpose:      Cours de Video 1 , 2 et 3
#
# Author:      Muriel
#
# Created:     01/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding: utf-8
"""
Nommer une variable :   doit commencer par une lettre ou une underscore
                        ne pas contenir de caractères spéciaux
                        ne pas contenir d'espace
                        utiliser des underscore (_)

Type standars des variables :   entier numérique (int)
                                nombre flottant (float)
                                chaine de caractères (str)
                                booléen (bool)
                                autres (listes, dictionnaires, tuple, etc.)

Fonction vues : print()         -> afficher à l'écran
                input()         -> lire au clavier
                type()          -> retourne le type d'une donnée, variables, etc
                str.format()    -> formater une chaine
                int(), float(), str(), bool() -> "caster" une donnée, la convertir


"""
valeur_Booleen = False
nom = input("Entrer votre nom: ")
agePersonne = input("Et votre age : ")

enterArgent = input("Entrer votre argent en fmg: ")

argent = int(enterArgent) / 5

texte = "Salam Alaikum {} et votre age est {}"

print(int(valeur_Booleen))
print(texte.format(nom,agePersonne))

print("Votre argent de Pôche est", argent,"fmg")


