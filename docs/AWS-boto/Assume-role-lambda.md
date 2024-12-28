#
##  Configure a Lambda function to assume an IAM role in another AWS account



IAM-Role [Assume role link](https://aws.amazon.com/premiumsupport/knowledge-center/lambda-function-assume-iam-role/#)


Youtube [Video_link](https://youtu.be/UsfdtF-kWzg)



- I need my AWS Lambda function to assume an AWS Identity and Access Management (IAM) role in another AWS account. How do I set that up?

- Short description
   To have your Lambda function assume an IAM role in another AWS account, do the following:

- Configure your Lambda function's execution role to allow the function to assume an IAM role in another AWS account.
- Modify your cross-account IAM role's trust policy to allow your Lambda function to assume the role.
- Add the AWS Security Token Service (AWS STS) AssumeRole API call to your Lambda function's code.
- Note: A Lambda function can assume an IAM role in another AWS account to do either of the following:

- Access resources—For example, accessing an Amazon Simple Storage Service (Amazon S3) bucket.
- Do tasks—For example, starting and stopping instances.
Resolution
Note: The following example procedure references two different types of AWS accounts:

- A home account that hosts the Lambda function ( 111111111111).
- A cross-account that includes the IAM role that the Lambda function assumes (222222222222)
The procedure assumes:

- You have created the IAM role that you want to use in the cross-account (222222222222)
- Configure your Lambda function's execution role to allow the function to assume an IAM role in another AWS account
- Add the following policy statement to your Lambda function's execution role (in account 111111111111) by following the instructions in Adding and removing IAM identity permissions:

Important: Replace 222222222222 with the AWS account ID of the cross-account role that your function is assuming. Replace role-on-source-account with the assumed role's name.
!!! IAM
    === "Role"
    ``` markdown
    {
        "Version": "2012-10-17",
        "Statement": {
            "Effect": "Allow",
            "Action": "sts:AssumeRole",
            "Resource": "arn:aws:iam::222222222222:role/role-on-source-account"
        }
    }
    ```
- Modify your cross-account IAM role's trust policy to allow your Lambda function to assume the role
- Add the following policy statement to your cross-account IAM role's trust policy (in account 222222222222) by following the instructions in Modifying a role trust policy (console):

- Important: Replace 111111111111 with the AWS account ID of the account that your Lambda function is in. Replace my-lambda-execution-role with the name of your function's 
  execution role.

!!! example

    === "Unordered List"
    
        ``` markdown
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": "arn:aws:iam::111111111111:role/my-lambda-execution-role"
                    },
                    "Action": "sts:AssumeRole"
                }
            ]
        }
        ```
- Add the AWS STS AssumeRole API call to your Lambda function's code
- Add the AWS STS AssumeRole API call to your function's code by following the instructions in Configuring Lambda function options.

Note: The AWS STS AssumeRole API call returns credentials that you can use to create a service client. By using this service client, your Lambda function has the permissions granted to it by the assumed role. For more information, see assume_role in the AWS SDK for Python (Boto 3) documentation.

- Python function code example that includes the AWS STS AssumeRole API call

Important: Replace 222222222222 with the AWS account ID of the cross-account role that your function is assuming. Replace role-on-source-account with the assumed role's name.

!!! Python code
    === "Lambda Function"
    ``` markdown
    import boto3

    def lambda_handler(event, context):

        sts_connection = boto3.client('sts')
        acct_b = sts_connection.assume_role(
            RoleArn="arn:aws:iam::222222222222:role/role-on-source-account",
            RoleSessionName="cross_acct_lambda"
        )
        
        ACCESS_KEY = acct_b['Credentials']['AccessKeyId']
        SECRET_KEY = acct_b['Credentials']['SecretAccessKey']
        SESSION_TOKEN = acct_b['Credentials']['SessionToken']

        # create service client using the assumed role credentials, e.g. S3
        client = boto3.client(
            's3',
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY,
            aws_session_token=SESSION_TOKEN,
        )

        return "Hello from Lambda"
    ```

!!!TroubleShoot Error url


   
   IAM-Assume-Role-Error[blog_link](https://aws.amazon.com/premiumsupport/knowledge-center/iam-assume-role-error/)


   Youtube [video_link](https://youtu.be/UdDlSRu8tvE)