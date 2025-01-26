# /usr/bin/bash
# ACESSING VARIABLE
# echo "enater name : " 
# # read -a names
# # echo "Names: ${names[0]}, ${names[1]}"

# read 
# echo "Names: $REPLY"

# input passing argument via terminal bash Untitled-1.sh 5 3 9
# echo $1 $2 $3 '>  echo $1 $2 $3'
# #  print all argument passed
# echo $@
# #passing user argument as array
# a=("$@")
# echo =${a[0]} ${a[1]} ${a[2]}

################
# echo -esp "enter the name : "  \c
# read name
# # -e flag to check file exist or not
# # -f flag is for exist if it is regular file or not
# # -s
# if [ -s $name ]
# then
#     echo "$name not empty"
# else
#     echo "$name empty"
# fi
#################

## IF statement
# if statement syntax

# if [ condition ]
# then 
#     statement
# fi

	
# echo $0
# echo "Number of arugment passed" $#
# echo "The first argument is:" $1
# echo "The second argument is:" $2
# echo "Doubled the argument:" $*
# echo "Doubled the argument:" $@
# echo "successfully executed" $?
# echo "The process number of the current shel" $$
# echo "dhd"$!
#############
# using vaariable and loop
# ################
# VAM="ma ad han"
# echo $VAM
# for TOKEN in $VAM
# do
#    echo $TOKEN
# done
###############
# Array
# VAM=("a" "b" "c")
# echo ${VAM[*]}
# echo ${VAM[0]}
# echo ${VAM[1]}

##################

echo "Enter UserName For SFTP Permission?"
# read username
# echo "Hello, $username"

ls -ld /home/$1
chown root:$1 /home/$1
chmod 775 /home/$1

#Operators
vam1=`expr 2 \* 2`
vam2=`expr 2 + 2`
vam3=`expr 2 - 2`
vam4=`expr 2 \* 2`
vam5=`expr 2 / 2`
#modulo
vam6=`expr 2 % 2`
#assignment
vam7=`expr 2 = 2`

echo $vam1 $vam2 $vam3 $vam4 $vam5 $vam6 $vam7 

a=2
b=3
#Equality
if [ $a == $b ]
then
    echo "is equal"
else
    echo "it is not equal"
fi

# Not Equality

if [ $a != $b ]
then   
    echo "it is not equal"
else
    echo "it is equal"
fi
# https://www.tutorialspoint.com/unix/unix-arithmetic-operators.htm
