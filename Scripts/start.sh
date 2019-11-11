#!/bin/sh

echo "Checking For Updates . . ."
sh update.sh
echo "Initiating . . ."
cd FireBOX_Sources/ServerAdmin
python3 ServerPickle.py