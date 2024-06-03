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


name = 'Blue'
if ('name' in data):
    name = data['name'].value

html= HTML_HEADER
html+= '<body style="background-color: '
html+= name + ';">'
html+= HTML_FOOTER
print(html)
