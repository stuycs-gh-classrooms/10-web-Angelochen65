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
if ('bgcolor' in data):
    bgcolor = data['bgcolor'].value

html= HTML_HEADER
html+= '<body style="background-color: '
html+= name + ';">'
html+= '<br><a href="hello.html">Try Again</a>'
html+= HTML_FOOTER
print(html)
