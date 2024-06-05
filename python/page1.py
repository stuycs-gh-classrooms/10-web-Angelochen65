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


passcode = '0000'
if ('passcode' in data):
    passcode = data['passcode'].value

if (passcode == '6543'):
    msg = "<a href= p2.html> Next door </a>"
else:
    msg = "<p> Try Again </p>"

html= HTML_HEADER
html+= msg
html+= HTML_FOOTER
print(html)
