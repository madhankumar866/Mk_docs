#


Install and Configure VNC Server in CentOS 7 and RHEL 7 [vncserver](https://www.linuxtechi.com/install-configure-vnc-server-centos-7-rhel-7/).

Install VNC server on CentOS 6.5  [CentOS 6.5 ](https://www.howtoforge.com/vnc-server-installation-centos-6.5)


- In my case I have a fresh installed CentOS6.5 Server on which I will be installing the VNC-server so that I can access the CentOS server with GUI. You can follow the guid\e for the basic installation of the CentOS server till Chapter 7. Please don't install the Development Tools. All of the cases are same as per the guide. My details are as follows:
```bash
IP address 192.168.0.100
Gateway 192.168.0.1
DNS     8.8.8.8    8.8.4.4
Hostname server1.example.com
```
- VNC-server benefits
- Remote GUI administration makes work easy & convenient.
- Clipboard sharing between host CentOS server & VNC-client machine.
- GUI tools can be installed on the host CentOS server to make the administration more powerful
- Host CentOS server can be administered through any OS having the VNC-client installed.
- More reliable over ssh graphics.
- More reliable over RDP connections.
- 2 Installation

I am logged in my system with root, & now I will be installing the VNC-server.
```bash
yum groupinstall Desktop
Further install
 yum install gnome-core xfce4 firefox
 yum install tigervnc-server
Now make the service on after every reboot
chkconfig vncserver on
```

3 Adding VNC user

In my case I am using user=srijan it will differ in your case. You can use any username for the same.
```bash
useradd srijan
```
Now I will assign the vncpassword for the user with the user I just created before as:
```bash
su - srijan
vncpasswd

[root@server1 ~]# su - srijan
[srijan@server1 ~]$ vncpasswd 
Password:<--yourvncpassword
Verify:<--yourvncpassword
[srijan@server1 ~]$
```

- Now I will make the configuration file for the vncserver  by creating file as follows:
```bash
vi /etc/sysconfig/vncservers
Give the entries like this.
[...]
VNCSERVERS="1:srijan"
VNCSERVERARGS[1]="-geometry 1024x768"

   Here your port comes to be 5901 & 1024x768 resolution for the VNC client, you can choose resolution of your own choice.
   Now I will restart the VNC server service as root user:

service vncserver restart
[root@server1 ~]# service vncserver restart
Shutting down VNC server:                                  [  OK  ]
Starting VNC server: 1:srijan xauth:  creating new authority file /home/srijan/.Xauthority

New 'server1.example.com:1 (srijan)' desktop is server1.example.com:1

Creating default startup script /home/srijan/.vnc/xstartup
Starting applications specified in /home/srijan/.vnc/xstartup
Log file is /home/srijan/.vnc/server1.example.com:1.log

                                                           [  OK  ]
[root@server1 ~]# 
Now to make the changes affective I will kill VNC & do some more configurations as follows:
pkill vnc
Open the file comment the line #twm & & add the line exec gnome-session as follows:
vi /home/srijan/.vnc/xstartup
#!/bin/sh

[ -r /etc/sysconfig/i18n ] && . /etc/sysconfig/i18n
export LANG
export SYSFONT
vncconfig -iconic &
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS
OS=`uname -s`
if [ $OS = 'Linux' ]; then
  case "$WINDOWMANAGER" in
    *gnome*)
      if [ -e /etc/SuSE-release ]; then
        PATH=$PATH:/opt/gnome/bin
        export PATH
      fi
      ;;
  esac
fi
if [ -x /etc/X11/xinit/xinitrc ]; then
  exec /etc/X11/xinit/xinitrc
fi
if [ -f /etc/X11/xinit/xinitrc ]; then
  exec sh /etc/X11/xinit/xinitrc
fi
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey
xterm -geometry 80x24+10+10 -ls -title "$VNCDESKTOP Desktop" &
#twm &
exec gnome-session &

& Finally reboot the machine.
reboot
```
4 VNC Client

- At client end my OS is Ubuntu14.04 with vino installed on my client machine. Otherwise you can install any VNC-client of your choice. In case other OS say windows-7 you can install Realvnc-client or any other of your choice.
- Again start the vncservice with the user srijan:
```bash
su - srijan
vncserver
[root@server1 ~]# su - srijan
[srijan@server1 ~]$ vncserver
New 'server1.example.com:1 (srijan)' desktop is server1.example.com:1
Starting applications specified in /home/srijan/.vnc/xstartup
Log file is /home/srijan/.vnc/server1.example.com:1.log
[srijan@server1 ~]$
```
- Now I am going to connect with the VNC server through my VNC-client

- It will prompt for the password as follows:

- Put yourvncpassword the same which you gave at the time of adding the user srijan.



- Now you are connected with the CentOS6.5 Server. In case you want to add more users to access the vnc-console you need to add the user, assign the vncpassword for the new-user as mentioned above & append the entry in the file as:
```bash
vi /etc/sysconfig/vncservers
```
For instance I am using user kishore, entries will be like this


!!! Note
  - [..]
  - VNCSERVERS="2:kishore"
  - VNCSERVERARGS[2]="-geometry 1024x768"



- This will enable user kishore to get the access to the VNC-server with the port 5902. In the same way you can add the root user also.