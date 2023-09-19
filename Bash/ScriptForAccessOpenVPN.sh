#!/bin/bash

echo "Depois de virar root, pressione Ctrl+d para entrar no openvpn"
sudo su 
"yourpassword" 2>/dev/null
sudo su -c "openvpn youruser.ovpn"
