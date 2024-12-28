
#

##

[sftp Refer Link](https://www.alibabacloud.com/blog/how-to-configure-chroot-environments-for-sftp-access-on-ubuntu-16-04_594118#:~:text=In%20Linux%20chroot%20stands%20for,a%20server%20over%20a%20network.)


## Commands to change permission
- vi /etc/ssh/sshd_config
# Set Permission for Main Root folder to access
- ls -ld /home/root_dir   
- chown root:root /home/root_dir
- chmod 755 -R /home/root_dir

# Set subfolder access to their respective folder
- mkdir /home/root_dir/user_folder
- chown username:username /home/root_dir/user_folder
- chmod 700 user_folder

## Add these lines inside sshd_config file    
=== "sshd_config"    
    ``` bash
    Match User {== user or group===}
    ChrootDirectory /home/ (or) {== add %u or %h==}
    ForceCommand internal-sftp
    X11Forwarding no
    AllowTcpForwarding no
    ```

!!! Notes

    === "points"

        ``` markdown
        %u - username
        %h - host
        ```

!!! Notes

    === "sftp-sshd_config"

        ``` bash
        --8<-- "docs/shell-script/shell-scripts/sftp.sh"
        ```

    === "README"

    ``` bash
    --8<-- "docs/shell-script/Readme/sftp.readme"
    ```

## Folder access structure
Main root folder will be handle by sftp tp to restrict user login,
and subfolder for the appropriate user will be created to give access for user's by mapping user name in sshd_config

``` mermaid
stateDiagram-v2
  state fork_state <<fork>>
    Root_Folder --> fork_state
    fork_state --> sub1
    fork_state --> sub2

    state join_state <<join>>
    sub1 --> join_state
    sub2 --> join_state
    join_state --> SFTP
    SFTP --> [*]
```




