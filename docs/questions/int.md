## L1 Int question

## linux
command to show the space
how to add user & want custom path for the user

what are the objects used to create pod, can tell the objects
kubernetes rbac

helm rendered version, which is getting applied.
[Answer Helm Template]

print only the file names
[
ls -lrt | awk '{print $9}'
]

i have multiple file names under a folder write a bash to identify if the folder has to file if yes print it as found 

```bash```
#!/bin/bash

# Set the directory path
DIR_PATH="/path/to/your/folder"

# Set the filenames you want to check for
FILE1="file1.txt"
FILE2="file2.txt"

# Check if both files exist
if [[ -f "$DIR_PATH/$FILE1" && -f "$DIR_PATH/$FILE2" ]]; then
    echo "found"
else
    echo "One or both files not found"
fi


## Terraform
why do we use data block in terraform 

[ Data sources allow Terraform to use information defined outside of Terraform, defined by another separate Terraform configuration, or modified by functions. ]

Local Values

A local value assigns a name to an expression, so you can use the name multiple times within a module instead of repeating the expression.

in terraform plan it shows 10 changes but we have to apply only particular changes
[

    In Terraform, if you only want to apply specific changes and not all the changes shown in a plan, you can achieve this by:

Using Targeted Resource Apply (-target): You can use the -target option to apply changes only to specific resources. For example:

bash
Copy code
terraform apply -target=module.module_name.resource_type.resource_name
This command will only apply the changes for the targeted resource(s) while ignoring other changes in the plan.

Manually Apply Specific Changes: If the change involves editing the resource configuration, you can manually adjust the configuration to include only the changes you want and then run terraform apply as usual.

Selective State Management: If needed, you can use terraform state commands to manage resources selectively. For instance, you can use terraform state rm to remove resources from the state file temporarily, apply changes, and then re-import them using terraform import.

Running Plan and Inspecting Changes: Before applying any changes, run:

bash
Copy code
terraform plan -target=module.module_name.resource_type.resource_name
This will generate a plan specific to your targeted resources.

Each approach allows you to narrow down the scope of your changes while applying only what’s needed.

]
##
Cluster add-ons
[]
liveness and rediness



## jenkins

DSL Concept
how to test different environments

jenkins executor