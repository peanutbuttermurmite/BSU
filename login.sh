#!/bin/bash
read -p "Enter the name of your file:" usernamebsu
printf "----> Installing .bsu file"
mv $usernamebsu tmpbsu.zip
unzip tmpbsu.zip
rm tmpbsu.zip
printf "----> Successfully Installed!"