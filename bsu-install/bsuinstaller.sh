#!/bin/bash
echo "---> Installing Packages"
echo -ne '>>>>>>>>                       [25%]\r'
sudo apt-get install python3 python3-tk python3-pip -y
echo "---> Downloading BSU + Python dependencies"
git clone https://github.com/peanutbuttermurmite/BSU.git
pip3 install enquiries selenium PySimpleGUI
echo -ne '>>>>>>>>>>>>>>>                [50%]\r'
cd BSU/bsu-install
chmod a+x bsu
cd ..
cd ..
sudo mv BSU /opt
echo -ne '>>>>>>>>>>>>>>>>>>>>>>>        [75%]\r'
"---> Installing BSU + updaterbsu"
sudo ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
sudo cp -r bsu.desktop ~/.local/share/applications
echo -ne '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[100%]\r'
echo "Installed Successfully"
echo "Run BSU by typing "bsu --run" into your terminal or use the .desktop file"
