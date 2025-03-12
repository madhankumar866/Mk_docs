# Q 

!!! q

==""
s3 is multi region  how to sync s3 to s3

rename git commit message

docker built commands

---

config maps
list process
how to configure ssh public & private key
how to mount docker in docker
docker logs
command to expose port using docker command
how you deployed eks



    === "Common q"

        ``` markdown
        * day to day acttivity
        * list services which u use
        * ways to block ip address in aws
        * create a architech
        * current working environment
        * how you deploy your application
        * how to
        
        ```

    === "git hub"

        ``` markdown
        * commit,push,merge,detached head, rebase
        To Commit
                "git add -A"
                "git commit -m "update""
                "git push origin main"
        To merge
            
        ```

    === "kubernetes"

        ``` markdown
        1.how to get pods command
            "kubectl help"
            "kubectl pods --help"
            
        To get the pods which are place on nodes            
            kubectl get pods -o wide
            
        2.docker build vs docker compose

            "Docker build  is used to create a image where we bundle our packages and files into particular required image"
            "Docker compose:-  Tool for Defining & running multi-container Docker applications \
                                we use Docker yaml file to create & start all services from configuration"

            Docker compose url 
            [https://www.freecodecamp.org/news/run-multiple-containers-with-docker-compose]
            [https://github.com/shenanigan/super-app-docker]                                

        3.pod log, container log
            refer difference between pod and container [https://medium.com/google-cloud/kubernetes-101-pods-nodes-containers-and-clusters-c1509e409e16]
        ! What is pod
        " pod is a collection of one or multiple containers. An application will be running in one container, while other containers will run in the pod for the purpose of a service mesh, logging, monitoring, etc. "
        
            To See Pod We use Label and selector to see the pods log ( Which contain multiple container's)
         ```
         kubectl logs pod/podname  --tail=100
         kubectl logs container name
         ```
        
        4.Difference between image and container 

         [https://phoenixnap.com/kb/docker-image-vs-container]
        EKS selenium grid
        ```
    === "linux"

        ``` markdown
        1.netsat , chmod,chown,restart,lshell,yum packages installation,
        apache,mysql,confgiure,tunning,problem identify.
        2. Apache or nginx error code like 404,402,403,401,200,301,302,500, and mk you have done nginx config in zabbix server  = { return 444; }

        ```
    === "Python"
        ``` markdown
        1.python skeliton
        ```
                    # Import necessary modules
            import sys

            # Define the main function
            def main():
                # Read input or initialize variables
                # ...

                # Call the core logic function
                result = core_logic_function(input_data)

                # Print or return the result
                print(result)

            # Define the core logic function
            def core_logic_function(input_data):
                # Implement the core logic here
                # ...

            # Call the main function
            if __name__ == "__main__":
                main()
        ```

        2.get alpabet from string
        ```
                def extract_alphabets(input_string):
            alphabets = ""
            for char in input_string:
                if char.isalpha():
                        ( Or Use below if you dont want isalpha method)
                if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):

                    alphabets += char
            return alphabets

        input_string = "Hello123World"
        alphabets_only = extract_alphabets(input_string)
        print(alphabets_only)
        ```

        3.get 7th element from a given string
        
        ```
        input_string = "This is a sample string."
        seventh_element = input_string[6]

        print(seventh_element)
        ```

        4.find number of reapeated word or number in given string
        5.read content's of file and print one one in net line
        
        ```
        file_path = "path_to_your_file.txt"  # Replace with the actual path of your file

        # Open the file for reading
        with open(file_path, "r") as file:
            # Read lines one by one and print them
            for line in file:
                print(line.strip())  # Strip newline characters and print each line        
        ```

        6.create a ec2 instance, rds and snapshot of both service. using boto3 and add it to crontab make it run at monday 5 am.

        ```
        import boto3

        # Create EC2 instance
        ec2_client = boto3.client('ec2')
        ec2_instance = ec2_client.run_instances(
            ImageId='ami-12345678',  # Replace with your desired AMI ID
            InstanceType='t2.micro',
            MinCount=1,
            MaxCount=1,
            KeyName='your-key-name',
            SecurityGroupIds=['sg-12345678'],  # Replace with your security group ID
            SubnetId='subnet-12345678'  # Replace with your subnet ID
        )

        # Create RDS DB instance
        rds_client = boto3.client('rds')
        db_instance = rds_client.create_db_instance(
            DBInstanceIdentifier='mydbinstance',
            AllocatedStorage=20,
            DBInstanceClass='db.t2.micro',
            Engine='mysql',
            MasterUsername='admin',
            MasterUserPassword='your-password',
            VpcSecurityGroupIds=['sg-12345678'],  # Replace with your security group ID
            DBSubnetGroupName='your-subnet-group-name'
        )

        ```


    === "Ansible"
        ``` markdown
        1.Create a Sample Ansible Playbook & With custom host
        
        ```
          - name: Update web servers
            hosts: webservers
            remote_user: root

            tasks:
            - name: Ensure apache is at the latest version
                ansible.builtin.yum:
                name: httpd
                state: latest
        ```
    
        
        3.Ansible Version

        To Run ansible Playbook
        
            " ansible-playbook playbook.yml " 
        
        To Verify yml file

        " ansible-lint verify-apache.yml "


        1. What is inventory file used for and default inventory host location?

        2. What is ansible configuration file used for and its default path?

        3. Do you write your inventory file?

        4. How many types of variables and precedence?

        5. Write the command to find the python version on nodes?

        6. What is the file structure of ansible roles?

        7. What happen when one node or instance is unreachable?

        8. What happen when one task is failed in playbook?

        9. I have 20 servers , I want to install one package in 5 servers and other package in next 5 servers..like that How to write in ansible script for that…Explain?

        10. What is the architecture of ansible?

        11. How do I supply variables while executing the playbook in ansible?

        12. Explain about the tags in ansible?

        13. How to execute failure playbook again?

        14. How is ansible diffrent than any other configuration management tool?

        15. Ansible playbooks are written in what format?


!!! q

    === "Common q"

        ``` markdown
        * Automating Routine Tasks, Migrating existing Monlithic setups to clouds, Works Towars Realtime problem along with developers to fix issues,(web server, app server,db servers, work in all kind of configuration & tuining perfomance issuse), Moreover my 85 percent of my on automating & managing services in cloud, other 15 percent i will be handling ticket like server,service,domain down, permission issuse,payment issuse, subnet reconfigure, work with wrong configuration to fix.


    === "Tools"
        Argocd
        percona
        grafana promethus





To mount a local directory into a Docker container

docker run -v <host_directory>:<container_directory> <image>


Docker login

docker exec -it mycontainer sh


