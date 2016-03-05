#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys


result = ''
def help():
    print 'Description: Xsstoascii is a tool which can transcoding native encode to ASCII encode.'
    print 'Usag: xsstoascii [-cx|v] \'source_string\''
    print ''
    print ' -x                            - Transcoding by hexadecimal ASCII'
    print ' -c                            - Use ";" as a delimiter.'
    print ' -cx                           - Transcoding by hexadecimal ASCII'
    print '                                 Use ";" as a delimiter.'
    print ' -v                            - Print current version.'
    print ''
    print ' --help                        - Print this help information.'

def usag():
    print 'xsstoascii: missing arguments'
    print 'Try "xsstoascii --help" for more information',

if len(sys.argv) > 1:
    if len(sys.argv) == 2:
        if sys.argv[1] ==  '--help':
            help()
        elif sys.argv[1] == '-v':
            print 'Version 0.0.1',
        elif sys.argv[1][0] != '-':
            for char in sys.argv[1]:
                result += '&#' + str(ord(char))
        else:
            usag()
    if len(sys.argv) == 3:
        if sys.argv[1] == '-c':
            for char in sys.argv[2]:
                result += '&#' + str(ord(char)) + ';'
        elif sys.argv[1] == '-x':
            for char in sys.argv[2]:
                result += '&#' + str(hex(ord(char)))[1:]
        elif sys.argv[1] == '-cx':
            for char in sys.argv[2]:
                result += '&#' + str(hex(ord(char)))[1:] + ';'
        else:
            usag()
else:
    usag()

print result,
