Create a Role


Put 
In Trusted Relationship

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::362778997593:root"
            },
            "Action": "sts:AssumeRole",
            "Condition": {}
        }
    ]
}

Add All These In Permission Block

AdministratorAccess	AWS managed 
Billing	AWS managed 
AWSBillingConductorFullAccess


Allow Access on Belhahf for root account


tag