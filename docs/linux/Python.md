
#  Python 
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


####python####
```bash
wget http://www.python.org/ftp/python/3.11.0/Python-3.11.0.tgz
tar -xvf Python-3.11.0.tgz 
cd Python-3.11.0

./configure --enable-loadable-sqlite-extensions --enable-optimizations --with-openssl=/usr/
 (or)
sudo ./configure --with-system-ffi --with-computed-gotos --enable-loadable-sqlite-extensions --with-openssl=/usr/

make
 (or)
make -j ${nproc} 

make install
 (or)
make altinstall 

ln -sf /usr/local/bin/python3.11 /usr/bin/python
 (or)
ln -sf /usr/local/bin/python3.11 /usr/local/bin/python
```

#############

* curl -fsSL https://code-server.dev/install.sh | sh

### Port Depend on user ###
```bash
echo " bind-addr: 127.0.0.1:*
auth: password
password: Te@mw0rk
cert: false " > ~/.config/code-server/config.yaml


sudo systemctl enable --now code-server@mk




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

[Python Environment](https://docs.python.org/3/library/venv.html)

[Serverless-Lambda-DynamoDB](https://www.serverless.com/blog/flask-python-rest-api-serverless-lambda-dynamodb/)