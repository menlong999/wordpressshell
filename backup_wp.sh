#!/bin/bash

dbuser=root
dbpwd=
dbname=wordpress

today=`date '+%Y%m%d'`
bakdir=wordpress-$today

mkdir /root/$bakdir
mkdir /root/$bakdir/site
mkdir /root/$bakdir/mysql

bakfile=/root/wordpress-${today}.tar.gz
[ -f $bakfile ] && rm -rf $bakfile

cp -rf /usr/share/nginx/html/wordpress /root/$bakdir/site/
cp -rf /var/lib/mysql/wordpress /root/$bakdir/mysql/
cp /etc/nginx/nginx.conf /root/$bakdir/
cp /etc/php-fpm.conf /root/$bakdir/
mysqldump -u${dbuser} -p${dbpwd} ${dbname} > /root/$bakdir/wordpress_db.sql
tar zcvfP ${bakfile} /root/$bakdir >/dev/null
rm -rf /root/$bakdir

