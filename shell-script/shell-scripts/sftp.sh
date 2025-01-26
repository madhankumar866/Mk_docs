

echo "Enter Group Name To Create for sftp user"

# read sftpgroup
# sftpgroup=""
sftpgroup="sftpgroup_resticted"
groupadd $sftpgroup

echo "Entered User names" 
echo $@
a=("$@")

echo "Permission Updated for respective User's"

for names in "${!a[@]}"
do
     Username=${a[$names]}
    #  echo "$nam"
     ls -ld /home/$Username
    chown root:$TOKEN /home/$Username
    chmod 775 /home/$Username
    sudo usermod -a -G $sftpgroup $Username
done

echo "Updating SSh config file for sftp users"

cat <<EOF >> /5
Match Group sftpuser
    ChrootDirectory /home/%u
    ForceCommand internal-sftp
    X11Forwarding no
    AllowTcpForwarding no
EOF

service sshd restart

b="$?"
echo "$b"
if [ $b == 0 ]
then   
    echo "Update Done"
else
    echo "Update not done"
fi
