#
## Snowflake ODBC
```
wget https://sfc-repo.snowflakecomputing.com/snowsql/bootstrap/1.2/linux_x86_64/snowflake-snowsql-1.2.23-1.x86_64.rpm
```

```bash
echo "
[snowflake-odbc]
name=snowflake-odbc
baseurl=https://sfc-repo.snowflakecomputing.com/odbc/linux/2.22.1/
gpgkey=https://sfc-repo.snowflakecomputing.com/odbc/Snowkey-630D9F3CAB551AF3-gpg " >> /etc/yum.repos.d/snowflake-odbc.repo
```
```
yum install libiodbc snowflake-odbc snowflake-snowsql-1.2.23-1.x86_64.rpm -y
```
```bash
echo "
[ODBC Drivers]
SnowflakeDSIIDriver=Installed

[SnowflakeDSIIDriver]
APILevel=1
ConnectFunctions=YYY
Description=Snowflake DSII
Driver=/<path>/lib/libSnowflake.so
DriverODBCVer=03.52
SQLLevel=1" >> /etc/odbcinst.ini


echo "

" >> /etc/odbc.ini
```

Test with

^^iodbctest "DSN=testodbc2;UID=mary;PWD=password"^^


DSN on linux CentOS [ODBC](https://community.snowflake.com/s/article/How-to-create-Snowflake-ODBC-DSN-On-Linux-CentOS)