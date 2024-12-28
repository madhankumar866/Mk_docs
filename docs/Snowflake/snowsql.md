#

## Installing  Snowsql
**********************************************************************
Installing SnowSQL on Linux Using the RPM Package

Downloading the SnowSQL RPM Package
            `https://developers.snowflake.com/snowsql/` - Download url.
**********************************************************************
1. Open a new terminal window.

       `Get the account name from your snowflake login url`
       
        `example: https://wca45935.us-east-1.snowflakecomputing.com/`
2. Execute the following command to test your connection:

      `snowsql -a <account_name> -u <login_name>`

      Enter your password when prompted. Enter !quit to quit the connection.

3. Add your connection information to the Config File `file-Location`

       `~/.snowsql/config` 

       `accountname = <account_name>`
          `username = <login_name>`
             `password = <password>`

4. Execute the following command to connect to Snowflake:

      snowsql