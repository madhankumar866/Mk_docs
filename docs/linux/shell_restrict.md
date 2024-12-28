To restrict a Linux user to specific commands in bash_profile shell on CentOS 7, you can follow these steps:

1.Open the bash_profile file for the user you want to restrict:
!!! Commands
     sudo nano /home/username/.bash_profile

     Replace "username" with the actual username.

2.Add the following lines to the file:

### Restrict user to specific commands
```bash
if [ "$(id -u)" != "0" ]; then
  alias ls="ls --color=auto"
  alias ll="ls -l --color=auto"
  alias grep="grep --color=auto"
  alias ps="ps aux"
  alias top="top -o %CPU"
  alias df="df -h"
  alias du="du -h"
  alias free="free -h"
  alias ifconfig="ifconfig -a"
  alias netstat="netstat -antup"
  alias ping="ping -c 5"
  alias traceroute="traceroute -n"
  alias ssh="echo 'Access denied'"
  alias sudo="echo 'Access denied'"
  alias su="echo 'Access denied'"
fi
```

- These lines create aliases for some common commands that the user is allowed to use, and block some other commands like ssh, sudo, and su.

3.Save and close the file.

4.Reload the bash_profile file:

- source /home/username/.bash_profile

- Again, replace "username" with the actual username.

