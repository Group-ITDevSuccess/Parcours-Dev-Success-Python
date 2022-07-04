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
	<h1>Page de récupération</h1>
	<p>
		Mon page web sans serveur Apache, mais en utilisant du HTML et Python
	</p>
	code sur CMD:
	<form method="post" action="result.py">
		<p>
			<input type="texte" name="username">
			<input type="submit" value="Envoyer">
		</p>
	</form>

</body>
</html>
"""
print(html)