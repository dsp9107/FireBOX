#!/bin/sh

sudo apt-get update
sudo apt-get upgrade
wget https://download.teamviewer.com/download/linux/teamviewer-host_armhf.deb
sudo dpkg -i teamviewer-host_armhf.deb
sudo apt --fix-broken install
echo "Use sudo teamviewer passwd <password> To Set Password"
echo "Then, Use teamviewer info To Retrieve The TeamViewer ID"
