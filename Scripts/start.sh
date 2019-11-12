#!/bin/sh

echo "Checking For Updates . . ."
sleep 1
sh update.sh
cd FireBOX_Sources/ServerAdmin
sleep 3
echo "Setting Up Firewall . . ."
python3 ReConfigureFirewall.py
echo "Waking Up chigfy To Obscure Traffic"
nohup python3 TrendGetter.py &
sleep 3
echo "Ads-Delivery Services Are Unreachable"
sleep 2
echo "chigfy Is Ensuring Clients' Privacy"
sleep 3
echo "Initiating Authentication Server . . ."
sleep 1
python3 ServerPickle.py