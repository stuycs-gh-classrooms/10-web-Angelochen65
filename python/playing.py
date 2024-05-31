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

name = "Blue"
if ('name' in data):
    name = data['name'].value
bgcolor = 'Blue'
if ('bgcolor' in data):
    bgcolor = data['bgcolor'].value
print(data)
