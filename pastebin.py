#!/usr/bin/env python
# coding=utf-8
import requests as re


url = 'http://pastebin.com/raw/cRYvK4jb'
rep = re.get(url)
print rep.content
