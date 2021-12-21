#!/bin/bash
echo "----> Installing .bsu file"
echo $1
mv $1 tmpbsu.zip
unzip tmpbsu.zip
rm tmpbsu.zip
echo "----> Successfully Installed!"