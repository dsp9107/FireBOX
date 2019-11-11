#!/bin/sh

echo "Updating . . ."
sudo rm FireBOX_Sources -rf
echo "Deleted Old Files"
git clone https://github.com/dsp9107/FireBOX_Sources.git
echo "Downloaded Latest Files"