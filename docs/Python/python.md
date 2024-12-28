# Python2.7 script To wget

!!! py wget
       "Wget python 2.7 Script"

        ```bash py
        import re
        import subprocess 

        filename="nginx.cof"
        url="http://rex.damicosoft.com/nginx_v3.txt"

        wget = "wget -O %s %s" % (filename,url)
        response= subprocess.check_output(wget,stderr=subprocess.STDOUT,shell=True)
        a = "\""+str(response)+"\""
            # print(a)
        pattern=r'200\sOK'
        match=re.search(pattern,a)
        if(match):
            print("match found")
        else:
            print("match not found")
        ```
Python Reference [reference_url](https://docs.python.org/2.7/library/subprocess.html)
        


### Python :

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