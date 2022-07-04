#coding:utf-8
import cgi
import cgitb

#Activer le mode debug:
cgitb.enable()

#Recuperer le donnéer de formulaire
form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8\n")

html = """<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Une page web avec Python et HTML</title>
</head>
<body>
	<h1>PAge de resultat</h1>
	<p>
		Mon page web sans serveur Apache, mais en utilisant du HTML et Python
	</p>

"""
try:
    if form.getvalue("username"):
        username = form.getvalue("username")
        print(f"<p>Salam Alaikum {username} !</p>")
        print("<script> alert('ok) </script>")
    else:
        raise Exception("Pseudo non transmis")
except:
    print("<p>Pseudo non transmis !</p>")

html = """
</body>
</html>
"""
print(html)