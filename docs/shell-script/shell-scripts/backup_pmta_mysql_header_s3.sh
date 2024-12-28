<< com
Installing Aws cli


wget "http://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip"
unzip awscli-exe-linux-x86_64.zip
sudo ./aws/install



# aws configure and auto insert access key and secret key

echo -e "*\n*\n\n" | aws configure

<< com
# file will not be created at first installation initilize with "aws configure" command
cat <<EOF >> /root/.aws/credentials
[default]
aws_access_key_id = *
aws_secret_access_key = *
EOF
com


# get server Name From the file | server alias line and get the value | trimer whitespaces
a=$(cat /var/www/cgi-bin/server_config.txt | awk -F 'server alias: ' '{print $2}' | tr -d '[:space:]' )

servername=${a^^} # Smaller To Caps
echo "$servername"

sudo mkdir /home/"$servername"_old_centos6_backup

#Mysql dump 
mysqldump -u root -p'cubesphpmyadmin'  maildynamix  > /home/"$servername"_old_centos6_backup/db_backup.sql

#tar 
tar -cvf /home/"$servername"_old_centos6_backup/"$servername".pmta_backup.tar /etc/pmta

# using aws cli
aws s3 sync /home/"$servername"_old_centos6_backup/ s3://headerv2/header_data/"$servername"/"$servername"_old_centos6_backup/

aws s3 sync /var/www/Maildynamix/Headers/ s3://headerv2/header_data/"$servername"/"$servername"_old_centos6_backup/Headers

#confirming wether the script is finished or not


if [[ "${?}" == 0 ]]  # checking  previously executed command is successful or not by using "$?"
then   
    echo "Update Done"
else
    echo "Update not done"
fi