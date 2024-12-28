

## code commit policy 
Allow only Specific user to access branch

[AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-conditional-branch.html)

=== "Policy"

    ```
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "codecommit:*",
                "Resource": "{==repoarn==}",
                "Condition": {
                    "StringEqualsIfExists": {
                        "codecommit:References": [
                            "refs/heads/{==Branch-name==}"
                        ]
                    }
                }
            }
        ]
    }
    
    ```




    * ` Git command to clone`

    git clone --single-branch -b {==Branch-name==} {==repo-url==}

https://medium.com/@it.melnichenko/invoke-a-lambda-across-multiple-aws-accounts-8c094b2e70be



=== "Limiting restrict user from accessing repo"

    ``` 
    --8<-- "docs/AWS/iam/policies/code-commit-restrictions"
    ```