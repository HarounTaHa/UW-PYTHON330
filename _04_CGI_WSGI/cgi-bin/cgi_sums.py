#!/usr/bin/env python
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/plain")
print()
form = cgi.FieldStorage()
operands = form.getlist('operand')
try:
    total = sum(map(int, operands))
    body = 'Your Total is : {}'.format(total)
except (ValueError, TypeError):
    body = 'Unable to calculate a sum: please provide integer operands'

print(body)
