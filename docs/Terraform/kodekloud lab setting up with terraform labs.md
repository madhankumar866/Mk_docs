# KodeKloud Lab: Setting Up Terraform

This page contains lab questions and solutions for setting up Terraform with AWS.

## Lab Exercises

=== "Exercise 1: S3 Backend Creation"
    **Question:**
    Create an `S3 bucket` for remote state storage.
    Name the bucket `my-terraform-state-[your-name-or-unique-string]`, ensuring it's a globally unique name. 
    
    Replace `[your-name-or-unique-string]` with your name or a unique string. Enable versioning on the S3 bucket and configure it to block all public access, keeping it private.

    ---
    **Solution:**
    Create a `main.tf` file in the **terraform-projects** folder:

    ```hcl
    resource "aws_s3_bucket" "terraform_state" {
      bucket = "my-terraform-state-johndoe123"
    }

    resource "aws_s3_bucket_versioning" "versioning" {
      bucket = aws_s3_bucket.terraform_state.id

      versioning_configuration {
        status = "Enabled"
      }
    }

    resource "aws_s3_bucket_public_access_block" "block_public_access" {
      bucket = aws_s3_bucket.terraform_state.id

      block_public_acls       = true
      ignore_public_acls      = true
      block_public_policy     = true
      restrict_public_buckets = true
    }
    ```

=== "Exercise 2: Configure S3 Backend"
    **Question:**
    Configure terraform to use the `S3 bucket` for state management. Add the required block in a new file called `backend.tf`.
    For key, add `terraform-state-file`.

    !!! note
        Do not apply the file yet.

    ---
    **Solution:**
    Create the following file titled `backend.tf`:

    ```hcl
    terraform {
      backend "s3" {
        bucket = "my-terraform-state-johndoe123"  # Replace with your unique bucket name
        key    = "terraform-state-file"
        region = "us-east-1"
      }
    }
    ```

=== "Exercise 3: AWS Secrets Manager"
    **Question:**
    Store sensitive information securely using **AWS Secrets Manager** by creating a new `secret`.
    Name the secret `my-database-password-<randomString>` and store a value `"YourSecurePassword"`.

    !!! warning
        Create this secret using the AWS CLI and ensure that the name is unique.

    ---
    **Solution:**
    Create a secret in **AWS Secrets Manager** named `my-database-password` using the command:

    ```bash
    aws secretsmanager create-secret --name my-database-password-johndoe --secret-string "YourSecurePassword"
    ```

=== "Exercise 4: RDS with Secrets Manager"
    **Question:**
    Using terraform, create an RDS database resource called `my_secret_db` with the following specs:

    - **identifier:** `rds-db-instance`
    - **allocated_storage:** `20`
    - **storage_type:** `gp2`
    - **engine:** `mysql`
    - **engine_version:** `8.0.43`
    - **instance_class:** `db.t3.micro`
    - **username:** `admin`

    Utilize the data source `aws_secretsmanager_secret_version` to retrieve the secret prefixed `my-database-password-` and use it in the resource as **password**.

    Initialize the repository, generate an execution plan and apply the configuration.

    ---
    **Solution:**
    Append the following content to the `main.tf` file:

    ```hcl
    data "aws_secretsmanager_secret_version" "database_password" {
      secret_id = "my-database-password-johndoe"
    }

    resource "aws_db_instance" "my_secret_db" {
      identifier        = "rds-db-instance"
      allocated_storage = 20
      storage_type      = "gp2"
      engine            = "mysql"
      engine_version    = "8.0.43"
      instance_class    = "db.t3.micro"
      username          = "admin"
      password          = data.aws_secretsmanager_secret_version.database_password.secret_string
    }
    ```

    Run:
    ```bash
    terraform init
    terraform plan
    terraform apply
    ```
