# Database Migration System AWS

For DMS TASK	

Provide the Following Aws customer Details To the Magento or Service provider

Aws account number
Region
Vpc
Subnet
Sepcify the port number to be opened by the service provider

Get the "Endpoint" from Adobe or whoever is providing the service & Look out for "Endpoint" under Vpc in aws

Paste the Provided "Endpoint" in "endpoint" in vpc & choose "Find service by name" and paste the endpoint  in same vpc

After Creation use the "DNS names" in endpoint  to connect to appropriate service and port number

Example:-
curl -v telnet://"DNS names":80 -vvv 

curl -v telnet://vpce-007ffnb9qkcnjgult-yfhmywqh.vpce-svc-083cqvm2ta3rxqat5v.us-east-1.vpce.amazonaws.com:80 -vvv 

Create the service or instance in same region,vpc,& subnet's





***Permission should be done In Master Db***

GRANT REPLICATION CLIENT, REPLICATION SLAVE ON Db.* TO 'passwd'@'%';

It should be done by the provider or the root in master




***Permission should be done In SLAVE DB***

GRANT ALTER, CREATE, DROP, INDEX, INSERT, UPDATE, DELETE, SELECT ON *.* TO'passwd'@'%';
GRANT ALL PRIVILEGES ON awsdms_control.* TO ''@'%'; 

CREATE USER 'username'@'%' IDENTIFIED BY 'passwd';

GRANT ALL PRIVILEGES ON * . * TO 'passwd'@'%';

FLUSH PRIVILEGES;

And create the target endpoint for master and slave and test the connection.


