# Add ports to Public Zone 
```bash
firewall-cmd --get-zones
firewall-cmd --permanent --zone=public --add-port=80/tcp
firewall-cmd --permanent --zone=public --add-port=443/tcp
firewall-cmd --permanent --zone=public --add-port=7904/tcp
firewall-cmd --reload
```