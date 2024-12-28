Got the solution for this issue. Below are the steps to compile and install the net-utils in the CenOS7

# repost
[CentOS7 AMI does not have ec2-net-utils package to configure secondary interface](https://repost.aws/questions/QUBcCFd1z4RNuNZx3k7vADBw/cent-os-7-ami-does-not-have-ec-2-net-utils-package-to-configure-secondary-interface)

If cloud-init directives are installed you can instance with user data. in cloud-config format [aws,User data and cloud-init directives](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/user-data.html)


=== "Tab 1"
    ```sh
    yum groupinstall "Development Tools" -y
    yum install epel-release -y
    yum update -y
    yum -y install git make systemd systemd-units rpm-build systemd-networkd cloud-int
    git clone --branch=1.x --single-branch --depth 1 https://github.com/aws/amazon-ec2-net-utils.git
    cd amazon-ec2-net-utils/
    curl -LO 'https://github.com/aws/amazon-ec2-net-utils/archive/1.7.3.tar.gz'
    rpmbuild --define "_sourcedir $PWD" -bb amazon-ec2-net-utils.spec
    ls ~/rpmbuild/RPMS/noarch/
    yum localinstall ls ~/rpmbuild/RPMS/noarch/amazon-ec2-net-utils-1.5-1.el7.noarch.rpm
    yum localinstall /root/rpmbuild/RPMS/noarch/*.rpm
    ```

=== "shell-to-install packages"

    ``` shell bash
    --8<-- "docs/shell-script/shell-scripts/yum_packages_insta.sh"
    ```


=== "TO backup mysql & pmta & header data push to s3 bucket"

    ``` bash
    --8<-- "docs/shell-script/shell-scripts/backup_pmta_mysql_header_s3.sh"
    ```