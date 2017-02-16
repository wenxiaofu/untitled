import re
import urllib
from urllib import request
urlstr="http://200.200.107.38/m/James/order/pp15_1_-_%E5%BA%94%E7%94%A8_-_%E9%94%80%E5%94%AE%E8%AE%A2%E5%8D%95_-_%E8%AE%A2%E5%8D%95%E5%88%97%E8%A1%A8.html"

fp=urllib.request.urlopen(urlstr)

html2str=fp.read().decode("utf8")
fp.close()

tr=[(r'\<span\>\&\#149\;.*?span\>'),
    (r'\<span\>.*?span\>'),]
tkr='|'.join('%s' % pair for pair in tr)
print(tkr)
li=re.findall(tkr,html2str)
#print(li)
li=re.match(tkr,html2str)
print(li.group())
statements = '''
    IF quantity THEN
        total := total + price * quantity;
        tax := price * 0.05;
    ENDIF;
'''

token_specification = [
        ('NUMBER',  r'\d+(\.\d*)?'),  # Integer or decimal number
        ('ASSIGN',  r':='),           # Assignment operator
        ('END',     r';'),            # Statement terminator
        ('ID',      r'[A-Za-z]+'),    # Identifiers
        ('OP',      r'[+\-*/]'),      # Arithmetic operators
        ('NEWLINE', r'\n'),           # Line endings
        ('SKIP',    r'[ \t]+'),       # Skip over spaces and tabs
        ('MISMATCH',r'.'),            # Any other character
    ]
tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
print(tok_regex)
li=re.findall(tok_regex,statements)
#print(li)

iter1=re.match(tok_regex,statements)
print(iter1.group())

iter2=re.finditer(tok_regex,statements)
print(iter2)