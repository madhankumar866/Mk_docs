#

!!! Mysql

        ```
        [mysqld]
        port                            = 3306
        datadir=/var/lib/mysql
        socket=/var/lib/mysql/mysql.sock
        tmpdir                          = /var/lib/mysql/mysql_temp  
        slave-skip-errors=1062,1146,1053,1064,1032,1677
        slow_query_log                  = ON
        long_query_time                 = 10
        slow_query_log_file             = /var/log/mysqld/slow.log
        read_buffer_size                = 8M 
        sort_buffer_size                = 8M 
        ```


###  Disabling symbolic-links is recommended to prevent assorted security risks
symbolic-links=0

user=mysql

### INNODB 
!!! Note
        innodb-buffer-pool-size        = 24M 

        innodb-f lush-method            = O_DIRECT

        innodb-flush-log-at-trx-commit = 2

        innodb_buffer_pool_instances   = 8

        innodb_log_file_size           = 50M

        innodb_log_buffer_size         = 32M

        innodb_thread_concurrency      = 8



## CACHES AND LIMITS #

!!! Note 

            #tmp-table-size                 = 32M

            max-heap-table-size             = 32M

            query_cache_type                = 1

            query_cache_size                = 800M

            max_connections                 = 1700
 
            wait_timeout                    = 800

            thread_cache_size               = 512

            open-files-limit                = 65535

            table-definition-cache          = 1024

            table-open-cache                = 2048

### TUNING #
!!! Note 

            max-allowed-packet             = 1G

            max-connect-errors             = 1000

### Binlog ###
!!! Note

            log-bin                        = /var/lib/mysql/mysql-bin

            expire-logs-days               = 14

            sync-binlog                    = 1

###
###

- [mysqld_safe]

- log-error=/var/log/mysqld.log

- pid-file=/var/run/mysqld/mysqld.pid
```
[client]

port                    = 3306

socket                  = /var/lib/mysql/mysql.sock
```


### Tuining mysql 
```

read_buffer_size                = 62M

sort_buffer_size                = 62M

innodb_buffer_pool_size         = 24M

read_buffer_size                = 62M --- 1MB for every 1GB of RAM

sort_buffer_size                = 62M --- 1MB for every 1GB of RAM

innodb_buffer_pool_size         = 24M
```