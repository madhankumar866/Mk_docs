# code server

```bash

 sudo yum group install "Development Tools" epel-release -y
 yum install openssl-devel bzip2-devel libffi-devel sqlite-devel wget nginx htop -y 
 cd /home/mk/
 wget http://ftp.openssl.org/source/openssl-1.1.1k.tar.gz
 tar -xvf openssl-1.1.1k.tar.gz 
 cd openssl-1.1.1k
 ./config --prefix=/usr --openssldir=/etc/ssl --libdir=lib no-shared zlib-dynamic
 make
 make install
 touch /etc/profile.d/openssl.sh
 echo "export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/lib64" > /etc/profile.d/openssl.sh
 source /etc/profile.d/openssl.sh
 openssl version
 yum update -y
```

#####
##
* curl -fsSL https://code-server.dev/install.sh | sh

### Port Depend on user ###
```bash
echo " bind-addr: 127.0.0.1:*
auth: password
password: Te@mw0rk
cert: false " > ~/.config/code-server/config.yaml
```

* sudo systemctl enable --now code-server@mk

```bash
echo " server {
    listen 80;
    server_name ansible.damicosoft.com;

    location / {
      proxy_pass http://127.0.0.1:*/;
      proxy_set_header Host $host;
      proxy_set_header Upgrade $http_upgrade;
      proxy_set_header Connection upgrade;
      proxy_set_header Accept-Encoding gzip;
    }

} " > /etc/nginx/conf.d/code.conf
```


===============================================================================

```bash
[root@s97996 ~]# curl -L https://coder.com/install.sh | sh
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100 15986  100 15986    0     0  38083      0 --:--:-- --:--:-- --:--:-- 38083
CentOS Linux 7 (Core)
Installing v0.19.2 of the amd64 rpm package from GitHub.
```

```bash
+ mkdir -p ~/.cache/coder
+ curl -#fL -o ~/.cache/coder/coder_0.19.2_linux_amd64.rpm.incomplete -C - https://github.com/coder/coder/releases/download/v0.19.2/coder_0.19.2_linux_amd64.rpm
######################################################################## 100.0%
+ mv ~/.cache/coder/coder_0.19.2_linux_amd64.rpm.incomplete ~/.cache/coder/coder_0.19.2_linux_amd64.rpm
+ rpm -U ~/.cache/coder/coder_0.19.2_linux_amd64.rpm

rpm package has been installed.
```


### To run a Coder server:

#### Start Coder now and on reboot

```bash
   sudo systemctl enable --now coder
   journalctl -u coder.service -b

```
#### Or just run the server directly
```bash
  $ coder server

  Default URL: http://127.0.0.1:3000
  Configuring Coder: https://coder.com/docs/v2/latest/admin/configure
```

#### To connect to a Coder deployment:
```bash
  $ coder login <deployment url>
```
