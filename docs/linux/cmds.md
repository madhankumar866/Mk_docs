# Commands 

* `Commands`

!!! example

    === "sefacl"

        ``` markdown
        * setfacl -m user:vs:rwx /home/site 
        ```

## Command to get private ip from aws server and save it to file using grep
* `awk command`
!!! example


    === "grep"

        ``` markdown
        ip a | egrep -v '127.0.0.1|::1|inet6 |grep inet  | awk -F"/" '{print $1}' | awk '{print $2}' > /var/www/cgi-bin/set_ip.txt
        chmod 777 /var/www/cgi-bin/set_ip.txt
        cat /var/www/cgi-bin/set_ip.txt
        ```