## Nginx and PHP Tuning:

```bash
wget -q -O- "http://rex.damicosoft.com/nginx_v3.txt" >  /etc/nginx/nginx.conf  
wget -q -O-  "http://rex.damicosoft.com/www.txt"  >  /etc/php-fpm.d/www.conf
wget -O  '/root/fpm_up.php'  'http://rex.damicosoft.com/fpm_up.txt';
php /root/fpm_up.php && rm -rf /root/fpm_up.php  && service nginx restart;service php-fpm restart;
wget -q -O-  "http://rex.damicosoft.com/www.txt"  >   /opt/remi/php56/root/etc/php-fpm.d/www.conf
```
####
* updatedb
#####
* locate php-fpm