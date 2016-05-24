#!/usr/bin/env python
# coding=utf-8
from os import system

cmd = system

max = int(raw_input(':'))
x = 1
while True:
    if x < 10:
        cmd('mv 0%d.jpg 0%d.png' % (x, x))
    else:
        cmd('mv %d.jpg %d.png' % (x, x))
    x += 1
    if x == max:
        break
