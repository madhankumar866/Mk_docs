cat <<'EOF' >> /tmp/net.py
ip_list=

i=0
for ip_lst in ip_list:
    i+=1
    content = 'DEVICE=eth0:{}'.format(i)+"\n"+'BOOTPROTO=STATIC'+"\n"+'ONBOOT=yes'+"\n"+'IPADDR={}'.format(ip_lst)+"\n"+'NETMASK=255.255.255.255'
    path='/etc/sysconfig/network-scripts/ifcfg-eth1:{}'.format(i)
    #file_open=open(path,"\"w+\"")
    file_open=open(path,"w+")
    file_open.write(content)
    file_open.close()
    file_open=open(path,"r")
    print(file_open.read())
EOF