!!! Notes
-   To generate an SSH key pair for login into a CentOS 7 server, you can follow these steps:

-   Open a terminal on your local machine.

-  Type the following command to generate a new SSH key pair:
  ```bash
   ssh-keygen
  ```

-  This will prompt you for a file name to save the key pair, and a passphrase (which is optional). Press "Enter" to accept the default file name and location, and then enter a passphrase if you want to use one.

-  Once the key pair has been generated, you should see two new files in the location you specified:

   id_rsa (the private key)

   id_rsa.pub (the public key)

-  Copy the public key to your CentOS 7 server by running the following command:"

```bash
ssh-copy-id user@server-ip
```

- Replace user with your username on the CentOS 7 server, and server-ip with the IP address of the server.

- This command will copy the public key to the server and add it to the authorized_keys file, which will allow you to log in using the private key.

- Log in to the CentOS 7 server using the private key:
```bash
ssh user@server-ip -i ~/.ssh/id_rsa
```
- This command will log you in to the server using the private key that you just generated.

- That's it! You should now be able to log in to your CentOS 7 server using the SSH key pair.


================================


- Connect to the server as the root user via SSH.

- Run the following command to generate the SSH key:
```bash
ssh-keygen -t rsa -b 4096 -f /root/.ssh/id_rsa
```
- This command will generate a 4096-bit RSA key and save it in the root user's .ssh directory with the filename id_rsa.

- When prompted, enter a passphrase for the key or leave it blank if you do not want to set one.

- Repeat step 2 to generate a second SSH key with a different name (e.g. id_rsa_second).

- Copy the public key of each SSH key pair (id_rsa.pub and id_rsa_second.pub) to the remote servers or services that you want to connect to using SSH.

- For example, to copy the id_rsa.pub file to a remote server, run the following command:
```bash
ssh-copy-id -i /root/.ssh/id_rsa.pub user@remote-server
```
- Replace user with the username on the remote server and remote-server with the hostname or IP address of the remote server.

- Repeat the command for each public key you want to copy to remote servers.

- Test the SSH connection using each SSH key by running the following command:
```bash
ssh -i /root/.ssh/id_rsa user@remote-server
```
- Replace id_rsa with the name of the SSH key file you want to use and user and remote-server with the appropriate values for the remote server.

- Repeat the command for each SSH key you want to test.

- That's it! You now have two SSH keys for the root user that you can use to securely connect to remote servers and services.