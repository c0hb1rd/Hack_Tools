#!/bin/sh
python -c "print(('[*] The md5 value: ' + __import__('md5').md5(str(raw_input('[*] Input the source: '))).hexdigest()))"
