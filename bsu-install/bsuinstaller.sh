#!/bin/bash
printf -- "---> Installing Packages"
echo -ne '>>>>>>>>                       [25%]\r'
sudo apt-get install python3 python3-tk python3-pip python3-pil python3-pil.imagetk
printf -- "---> Downloading BSU + Python dependencies"
git clone https://github.com/peanutbuttermurmite/BSU.git
pip3 install enquiries selenium PySimpleGUI
echo -ne '>>>>>>>>>>>>>>>                [50%]\r'
cd BSU/bsu-install
chmod a+x bsu
cd ..
cd ..
sudo mv BSU /opt
echo -ne '>>>>>>>>>>>>>>>>>>>>>>>        [75%]\r'
printf -- "---> Installing BSU + updaterbsu"
sudo ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
sudo cp -r bsu.desktop ~/.local/share/applications
echo -ne '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>[100%]\r'
printf -- "Installed Successfully"
printf -- "Run BSU by typing "bsu --run" into your terminal or use the .desktop file"
