#!/bin/bash
packages=("httpd" "mysql-server" "php")

#Loop through packages and install
for package in "${packages[@]}"
do
if ! rpm -qa | grep -qw $package; then
echo "Installing $package"
yum install -y $package
else
echo "$package is already installed"
fi
done

#Check if packages are installed
for package in "${packages[@]}"
do
if ! rpm -qa | grep -qw $package; then
echo "$package installation failed"
fi
done

echo "Package installation complete."