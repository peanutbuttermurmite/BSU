
sudo ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
sudo cp -r bsu.desktop ~/.local/share#!/bin/bash
sudo apt install python3 python3-tk python3-pip python3-pil python3-pil.imagetk yad -y > /dev/null 
yad --progress \
  --title="Dependency Install" \
  --text="All dependencies installed" \
  --percentage=33
git clone https://github.com/peanutbuttermurmite/BSU.git
pip3 install enquiries selenium PySimpleGUI
yad --progress \
  --title="Python packages " \
  --text="Setting up..." \
  --percentage=66
cd BSU/bsu-install
chmod a+x bsu
cd ..
cd ..
sudo mv BSU /opt/applications
yad --progress \
  --title="BSU has no been set up" \
  --text="Installation Complete" \
  --percentage=100
printf -- "Installed Successfully"
printf -- "Run BSU by typing "bsu --run" into your terminal or use the .desktop file"
printf -- "Use bsu --help to show all commands (WARNING:use sudo before commands)"
