
# Manage Docker as a non-root user🔗
https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user

sudo usermod -aG docker $USER


# Add docker to firewlld.
## Please substitute the appropriate zone and docker interface
firewall-cmd --zone=trusted --remove-interface=docker0 --permanent
firewall-cmd --reload

https://docs.docker.com/network/packet-filtering-firewalls/