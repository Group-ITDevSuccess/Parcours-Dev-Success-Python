#coding:utf-8

import cgi

print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Une page web avec Python et HTML</title>
</head>
<body>
	<h1>Salam Alaikum</h1>
	<p>
		Mon page web sans serveur Apache, mais en utilisant du HTML et Python
	</p>
	code sur CMD:
	<p>
		cd D:\PREPARATION_PISCINE_INTEGRATION\Cours_de_Python\VingNeuf\ python .\http-serveur.py
	</p>

</body>
</html>
"""
print(html)