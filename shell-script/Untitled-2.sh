
# echo "your ui ${UID}"
# files=`id -un`  # old way to store command output to variable
# # files="$(ls)" # use openparanthes() to capture output of command.
# files="$(id -un)"

# echo "$files"


if [[ "${UID}" -eq 0 ]]
then
    echo "your are root"
else 
    echo "yoou are not root"
fi