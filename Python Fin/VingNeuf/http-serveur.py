#-------------------------------------------------------------------------------
# Name:        Le Serveur HTTP et page web
# Purpose:  Cours 29
#
# Author:      Muriel
#
# Created:     11/06/2022
# Copyright:   (c) Muriel 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#coding:utf-8

#Sans interface script CGI
"""
import http.server
import socketserver

#Initialiser le port:
port = 80
address = ("",port)

#Metre en place un gestionnaire:

handler = http.server.SimpleHTTPRequestHandler

#Metre en place le httpd oula connexion:
httpd = socketserver.TCPServer(address, handler)

print(f"Serveur démarré sur le PORT {port}")

#Mètre en boucle l'affichage de page:
httpd.serve_forever()
"""
import http.server

port = 80
address = ("",port)

server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
#Répertoire de fichier
handler.cgi_directories = ["/"]

httpd = server(address, handler)

print(f"Serveur démarré sur le PORT {port}")

httpd.serve_forever()
