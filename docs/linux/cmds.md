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

        ## Immutable Files (chattr)

        Use the `chattr` command to make files immutable, preventing them from being deleted or modified, even by the root user.

        !!! example

        === "Make file immutable"

        ```bash
        # To make a file immutable
        sudo chattr +i filename
        ```

        === "Remove immutability"

        ```bash
        # To remove the immutable attribute
        sudo chattr -i filename
        ```

        === "Check attributes"

        ```bash
        # To see the attributes of a file
        lsattr filename
        ```