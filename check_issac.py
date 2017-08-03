#!/usr/bin/env python3
# encoding: utf-8
import sys

from isafk.dbconnector import BaseDB



dbconn = BaseDB('root', 'root,./123', 'issac_db')


def select_items(key, table):
    sql = 'SELECT * FROM ' + table + ' WHERE f_name LIKE %(key)s'
    ret = dbconn.select(sql, {'table': table, 'key': '%' + key + '%'})
    if ret.Suc:
        for line in ret.Result:
            for k, v in line.items():
                print(k + ':', v)
            print()


select_items(sys.argv[1], sys.argv[2])

