#
##  Create Database:

!!! Note
    create or replace database sf_tuts;

    select current_database(), current_schema(), current_warehouse();


`elect from table;`

 select * from EMP_BASIC ;	

`use warehouse`

 use WAREHOUSE SENT_MTM;

```
create or replace table emp_basic (
  em_id string ,
  email string ,
  trackid string ,
  stats_id string ,
  offer_id string ,
  jobisp string
  );
```

### Put file
```
put file:///td-agent/csv4.log @SF_TUTS.PUBLIC.%emp_basic;
```

```
copy into emp_basic
  from @%emp_basic 
  file_format = (type = csv field_optionally_enclosed_by='"')
  pattern = '.*csv4.log.gz'
  on_error = 'skip_file';
```

Sql copy into table.HTML [Reference](https://docs.snowflake.net/manuals/sql-reference/sql/copy-into-table.html)

```
create stage files;

    `create stage csv;`

 list staged files;

     `list @csv;`
```
### To remove stage files:

- Remove @sf_tuts.public.%emp_basic pattern='.*.csv.gz'; 

[ TO Check error before Loading data into the tables; ]

	COPY INTO emp_basic
	  FROM @%emp_basic
	    validation_mode=return_all_errors;


### copy into tables stage files

 copy into EMP_BASIC
     from @csv
     pattern = 't9.csv.gz'
     on_error = 'skip_file';

desc table  emp_basic;



For loading from s3 AMAZON [S3.html](https://docs.snowflake.net/manuals/user-guide/data-load-s3.html)

Option 3: Configuring AWS IAM User Credentials
```
#staged from s3
CREATE OR REPLACE STAGE my_t3_stage
URL='s3://b1pk2az26c/tsty_snt_dt_120220_fn*'
CREDENTIALS=(AWS_KEY_ID='**************' AWS_SECRET_KEY='***********************');                     
                                                    

COPY INTO SENTDATA       
FROM @my_t3_stage
FILE_FORMAT = (type = csv NULL_IF = ('0000-00-00 00:00:00') SKIP_HEADER = 1 field_optionally_enclosed_by='"')
PATTERN = '.*tsty_snt_dt_120220_fna[a-z]'
ON_ERROR = 'skip_file';        
```