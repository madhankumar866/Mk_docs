# AMAZON LINUX

use locate command to find the files  for starting ""service php56-php-fpm status""


## Install PHP5.6 in AMAZON LINUX
cat /etc/os-release
<<<<<<< HEAD
<<<<<<< HEAD
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
=======
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpmyum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
>>>>>>> 1a23421 (Rebase_Edited_Update)
=======
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
>>>>>>> 33a4921 (AWS)
yum install http://rpms.remirepo.net/enterprise/remi-release-7.rpm -y
yum install yum-utils -y
yum-config-manager --enable remi-php56 
yum install php56 php56-mcrypt php56-cli php56-gd php56-curl php56-mysql php56-ldap php56-zip php56-fileinfo php56-php-fpm install php56-php-pecl-mysqlnd-ms php56-php-pdo -y
cd /usr/bin
ln -sf php56 php

ln -sf php56 php
php -v


## Install mysql5.5.55

wget https://cdn.mysql.com/archives/mysql-5.5/MySQL-5.5.55-1.el7.x86_64.rpm-bundle.tar
tar -xvf MySQL-5.5.*
rm -rf *.tar
yum install *
cat /etc/my.conf



Check my.cnf and set correct access log
PLEASE REMEMBER TO SET A PASSWORD FOR THE MySQL root USER !
To do so, start the server, then issue the following commands:
    /usr/bin/mysqladmin -u root password '*****'
    /usr/bin/mysqladmin -u root -h ip-172-31-92-146.ec2.internal password '*****'

    Alternatively you can run:
    /usr/bin/mysql_secure_installation



sudo service mysql stop
sudo nano /etc/mysql/my.cnf

add it in my.cof
user=mysql

sudo chown -R mysql:mysql /var/lib/mysql/
sudo service mysql start
