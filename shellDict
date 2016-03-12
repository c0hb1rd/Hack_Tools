#!/usr/bin/env python
# coding=utf8
import re
import requests
import sys


value = ""
if len(sys.argv) > 1:
    value = sys.argv[1]
else:
    value = str(raw_input('[*]Input a word which you wanna search: '))
url = r'http://dict.youdao.com/search?q=%s&keyfrom=dict.index' % value
response = requests.get(url)
content = response.text

REGX = r'li>(\w.*)</li>'
result = re.findall(REGX, content)

ls = []
for value2 in set(result):
    ls.append(value2)

ls = sorted(ls)
for value in ls:
    print '[*]' + value
