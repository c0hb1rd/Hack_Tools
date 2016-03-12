#!/bin/bash
mysql -h121.42.32.213 -uroot -p417811... -Dmyspace -e"DROP TABLE useduser"
mysql -h121.42.32.213 -uroot -p417811... -Dmyspace -e"CREATE TABLE useduser(id smallint primary key auto_increment, name varchar(30))"
