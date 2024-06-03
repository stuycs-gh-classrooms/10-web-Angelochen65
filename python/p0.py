#!/usr/bin/python
print('Content-type: text/html\n')

import cgi
data = cgi.FieldStorage()

HTML_HEADER = """
<!DOCTYPE html>
<html lang="en">

<head>
<meta charset="utf-8">
<title>Hello</title>
</head>
"""

HTML_FOOTER = """
</body>
</html>
"""


name = 'Rwar'
if ('name' in data):
    name = data['name'].value

html= HTML_HEADER
html+= '<p> Hello there ' + name + "! Sadly I think that you're stuck here. There's a weird looking door thing if you want to try to go through it. (I'm kind of forcing you to go, or else we'll be stuck here for a while) </p>"
html+= '<br> <a href = "p1.html">' +  "Let's go I guess.. </a>"
html+= HTML_FOOTER
print(html)
