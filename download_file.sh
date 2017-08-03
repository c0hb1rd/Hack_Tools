#!/bin/bash

download_file() {
    echo '[*]Start download file:' $1
    scp root@tz.umisen.net:/var/www/$1 $1
    echo '[*]Download finish'
}

download_file $1
