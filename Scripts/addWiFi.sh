#!/bin/sh

sudo sh -c 'echo "
network={
	ssid="testing"
	psk="testingPassword"
	key_mgt=WPA-PSK
}" >> /etc/wpa_supplicant/wpa_supplicant.conf'