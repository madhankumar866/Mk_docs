# Squid installation & config file

yum install squid httpd-tools
sudo cp /etc/squid/squid.conf /etc/squid/squid.conf.default

htpasswd -cb /etc/squid/passwd proxytunnel VtB35VJ5pnm31NwL9G
cat /dev/null > /etc/squid/conf.d/ipconfig.conf
service squid restart


## Put below in config location
## Config

    

```bash
acl manager proto cache_object
#acl localhost src 136.232.211.158/32  14.98.54.90/32 202.83.25.120/32

acl localhost src 127.0.0.0/8 
acl to_localhost dst 127.0.0.0/8 0.0.0.0/32 ::1
acl localnet src 0.0.0.0/8
include /etc/squid/conf.d/*.conf 

##########

##########

acl Safe_ports port 4377         #squid
acl SSL_ports port 443
acl Safe_ports port 80          # http
acl Safe_ports port 21          # ftp
acl Safe_ports port 443         # https
acl Safe_ports port 70          # gopher
acl Safe_ports port 210         # wais
acl Safe_ports port 1025-65535  # unregistered ports
acl Safe_ports port 280         # http-mgmt
acl Safe_ports port 488         # gss-http
acl Safe_ports port 591         # filemaker
acl Safe_ports port 777         # multiling http
acl CONNECT method CONNECT

auth_param basic program /usr/lib64/squid/basic_ncsa_auth /etc/squid/passwd
auth_param basic children 5
auth_param basic realm Squid proxy-caching web server
auth_param basic credentialsttl 2 hours
auth_param basic casesensitive off


acl ncsa_users proxy_auth REQUIRED
http_access allow ncsa_users


http_access allow manager localhost
http_access deny manager

http_access deny !Safe_ports

http_access deny CONNECT !SSL_ports



http_access allow localnet
http_access allow localhost

http_access deny all

http_port 4377

hierarchy_stoplist cgi-bin ?

#cache_dir ufs /var/spool/squid 500 26 556

forwarded_for delete

coredump_dir /var/spool/squid

refresh_pattern ^ftp:           1440    20%     10080
refresh_pattern ^gopher:        1440    0%      1440
refresh_pattern -i (/cgi-bin/|\?) 0     0%      0
refresh_pattern .               0       20%     4320


```