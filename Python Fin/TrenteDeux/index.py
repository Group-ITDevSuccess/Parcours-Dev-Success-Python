# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        Base de donnée
# Purpose: Cours 32
#
# Author:      Muriel
#
# Created:     18/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import sqlite3

#CRUD : Create, Read, Update, Delete
try:
    connection = sqlite3.connect("base.db")
    cursor = connection.cursor()
    rep = cursor.execute('SELECT * FROM py_users') 

    for row in rep.fetchall():
        print(row[1])

except Exception as e:
    print("[ERREUR]",e)
    connection.rollback()
finally: 
    connection.close()
# =============================================================================
# new_user = (cursor.lastrowid,"Jason",15)
# cursor.execute('INSERT INTO py_users VALUES(?,?,?)', new_user)
# print("Nouveau utlisateur ajouter")
# connection.commit()
# =============================================================================


# =============================================================================
# cursor.execute('SELECT * FROM py_users WHERE user_name = ?', my_username)
# 
# result = cursor.fetchone()[1]
# print(f"Le nom de l'utlisateur est : {result}")
# =============================================================================

