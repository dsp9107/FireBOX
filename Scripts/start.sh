#!/bin/sh

echo -e "\e[93mChecking For Updates . . .\e[39m"
sleep 1
sh update.sh
cd FireBOX_Sources/ServerAdmin
sleep 2
echo -e "\e[93mSetting Up Firewall . . .\e[39m"
python3 ReConfigureFirewall.py
echo -e "\e[93m"Waking Up chigfy To Obscure Traffic\e[39m"
nohup python3 TrendGetter.py >/dev/null 2>&1 &
sleep 2
echo -e "\e[93mAds-Delivery Services Are Unreachable\e[39m"
sleep 1
echo -e "\e[93mchigfy Is Ensuring Clients' Privacy\e[39m"
sleep 2
echo -e "\e[93mInitiating Authentication Server . . .\e[39m"
sleep 1
python3 ServerPickle.py