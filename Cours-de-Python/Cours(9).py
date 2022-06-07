#-------------------------------------------------------------------------------
# Name:        Gestion des erreurs
# Purpose:  Cours 9
#
# Author:      Muriel
#
# Created:     01/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8
"""
Gérer les exceptions : try / except (+else, finally)

Types d'exceptions: ValueError
                    NameError
                    TypeError
                    ZeroDivisionError
                    OSError
                    AssertionError
"""
ageUtisateur = input ("Votre âge : ")

#Gestion des erreurs lors de entrer de utlisateur
try:
    ageUtisateur = int(ageUtisateur)
except:
    print("L'age indiqué est incorrect")
else:
    print("Tu as",ageUtisateur,"ans")
finally:
    print("FIN DU PROGRAMME....")

#Gerer une erreurs de calcule

nombre1 =  150

nombre2 = input("Entrer le nombre pour diviser: ")

try:
    nombre2 = int(nombre2)
    print("Resultat = {}".format(nombre1 / nombre2))
except ZeroDivisionError:
    print("Vous devez entrer un nombre different de Zéro")
except ValueError:
    print("Vous avez saisie de lettre")
except:
    print("Valeur incorrect.")
else:
    print("Bonne Choix")
finally:
    print("Fin de programme...")

#Pour levez un exception
ageNotError = input("Votre Age : ")
ageNotError = int(ageNotError)

if (age < 25):
    raise ZeroDivisionError ("Mon Erreur") #raise poru levez les erreurs
#Gerer une assertion
try:
    ageS = input("Votre age : ")
    ageS = int(ageS)

    assert age >= 18 #Je veux que ageS soit plus grand que 18
except AssertionError:
    print("Vous êtes mineur, reserver au plus de 18 ans")

