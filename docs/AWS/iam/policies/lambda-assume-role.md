<<<<<<< HEAD

# Allow Access To Lambda To Access resources
Master account

lambda-ec2-fleet-management

ec2-start-stop-lambda-role

=======
Add service policy

AmazonEC2FullAccess	
ServiceQuotasFullAccess	



# Trusted Entities
>>>>>>> 1a23421 (Rebase_Edited_Update)
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
<<<<<<< HEAD
                "Service": "lambda.amazonaws.com"
=======
                "AWS": "arn:aws:iam::root-acccount-number:role/ec2-start-stop-lambda-role"
>>>>>>> 1a23421 (Rebase_Edited_Update)
            },
            "Action": "sts:AssumeRole"
        }
    ]
<<<<<<< HEAD
}

AdministratorAccess	
AmazonSNSFullAccess	
AWSMarketplaceFullAccess
Tag 

date
19/06/2023

Project	
Ec2-Fleet-Management

==================================

Slave account

ec2-fleet-management-lambda-assume-role

Description :- Ec2-Fleet-Management By Lambda From Master Account

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::362778997593:role/lambda-ec2-fleet-management"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

permission

AmazonEC2FullAccess
ServiceQuotasFullAccess

Tag 

date
19/06/2023

Project	
Ec2-Fleet-Management
=======
}
>>>>>>> 1a23421 (Rebase_Edited_Update)
