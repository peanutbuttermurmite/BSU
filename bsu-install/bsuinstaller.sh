#!/bin/bash
echo "---> Installing Packages"
sudo apt-get install python3 python3-tk python3-pip -y
echo "---> Downloading BSU + Python dependencies"
git clone https://github.com/peanutbuttermurmite/BSU.git
pip3 install enquiries selenium PySimpleGUI
cd BSU/bsu-install
chmod a+x bsu
cd ..
cd ..
mv BSU /opt
"---> Installing BSU + updaterbsu"
sudo ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
cp -r bsu.desktop ~/.local/share/applications
echo "Installed Successfully"
echo "Run BSU by typing "bsu --run" into your terminal or use the .desktop file"
