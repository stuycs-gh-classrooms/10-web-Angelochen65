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
RETURN = """
<body>
  <t1> There seem to be some weird shapes on the wall... and a lock? Figure out the passcode and access the next door. </t1>
    <p>(Insert images of hexagon, star, square, triangle)</p>
    <form action = "page1.py" method = "GET">
    
      <input type = "text" name = "passcode" value = "0000">
      <br>
      <input type = "submit" name = "Submit">
    </form>
    """

passcode = '0000'
if ('passcode' in data):
    passcode = data['passcode'].value

if (passcode == '6543'):
    msg = "<a href= p2.html> Next door </a>"
else:
    msg = "<p> Try Again </p>"

html= HTML_HEADER
html+= RETURN
html+= msg
html+= HTML_FOOTER
print(html)
