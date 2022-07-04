#coding:utf-8
import cgi
import http.cookies
import datetime
import os
import sys
import codecs
#Encodage
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

expiration = datetime.datetime.now() + datetime.timedelta(days=365)
expiration = expiration.strftime("%a, %d-%b-%Y %H:%M:%S")

#Format pour créer un Cookie
"""
expires =
path
comment
domain
secure
version
httponly

Sat, jj-mm-yy

"""
#print("Set-Cookie: pref_lang=fr; httponly")
"""
my_cookie = http.cookies.SimpleCookie()
my_cookie["pref_lang"] = "fr"
my_cookie["pref_lang"]["expires"] = expiration
my_cookie["pref_lang"]["httponly"] = True
"""
#Dérnérer le cookier
print(my_cookie.output())

#DU HTML
print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Une page Web</title>
</head>
<body>
	<h1>Cookies avec Python</h1>
"""
print(html)

print("<p>Salam Alaikum ! :) </p>")
try:
    user_lang = http.cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
    print("La langue choisie est :", lauser_lang["pref_lang"].value)
except (http.cookies.CookieError,KeyError):
    print("Non trouver")

"""
if "HTTP_COOKIE" in os.environ:
    print(os.environ["HTTP_COOKIE"])
else:
    print("Cookies n'existe pas")
"""
html = """
</body>
</html>
"""
print(html)