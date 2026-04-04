#!/bin/bash

`/bin/sed -i '116 s/DAEMON_OPTIONS*[a-z]*/dnl # &/' /etc/mail/sendmail.mc`
`/usr/bin/m4 /etc/mail/sendmail.mc > /etc/mail/sendmail.cf`
`/usr/bin/makemap hash /etc/mail/virtusertable.db < /etc/mail/virtusertable`

DATE=$(date +"%Y%m%d%H%M");
echo $DATE;
echo y | /bin/cp /etc/aliases /root/aliases_"$DATE"; # Backup /etc/aliases

## Remoev all prior bindings for virtual mailboxes 

`/usr/bin/perl -n -i -e 'print unless /test/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /feedback/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /abuse/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /admin/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /contact/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /info/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /contactus/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /mail/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /support/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /tech/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /webmaster/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /postmaster/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /hostmaster/' /etc/aliases`
`/usr/bin/perl -n -i -e 'print unless /catchallaccount/' /etc/aliases`

## Add all necessary users 

for i in {abuse,feedback,admin,contact,info,contactus,mail,support,tech,webmaster,postmaster,hostmaster,catchallaccount}; do  /usr/sbin/useradd -s /sbin/nologin $i;  done

## Echo all bindings back to /etc/aliases

for i in {abuse,feedback,admin,contact,info,contactus,mail,support,tech,webmaster,postmaster,hostmaster,catchallaccount}; do /bin/sed -i "1i $i: $i" /etc/aliases;done 

## Backup /etc/mail/virtusertable
echo y | /bin/cp /etc/mail/virtusertable /root/virtusertable_"$DATE"; # Backup /etc/mail/virtusertable

## Echo All mailboxes to tempfile
/bin/touch /tmp/newVirtusertable;
/bin/cat /dev/null > /tmp/newVirtusertable;

/bin/cat /dev/null > /etc/mail/local-host-names
/bin/cat /etc/hosts | egrep -v "127.0|Do|::1|localhost|that" | gawk '{ print $2 }' | sort -u >> /etc/mail/local-host-names

## Create all virtual mailboxes
for i in `/bin/cat /etc/hosts | egrep -v "127.0|Do|::1|localhost|that" | gawk '{ print $2 }' | sort -u`; do for j in {abuse,feedback,admin,contact,info,contactus,mail,support,tech,webmaster,postmaster,hostmaster,root}; do echo "$j@$i $j" >> /tmp/newVirtusertable;done; done

## Add catchall account to tempfile
for i in `/bin/cat /etc/hosts | egrep -v "127.0|Do|::1|localhost|that" | gawk '{ print $2 }' | sort -u`; do echo "@${i} catchallaccount" >> /tmp/newVirtusertable; done

## Sort and unique
#sort -ru /tmp/newVirtusertable > /tmp/tempFile

## Copy new virtusertable to destination location
echo y | /bin/cp /tmp/newVirtusertable /etc/mail/virtusertable; 

## Newaliases;
newaliases;
/etc/init.d/sendmail restart; 

## remove temp files
/bin/rm -f /tmp/newVirtusertable
/bin/rm -f /tmp/tempFile
