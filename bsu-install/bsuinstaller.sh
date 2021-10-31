#!/bin/bash
sudo ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
sudo cp -r bsu.desktop ~/.local/share
sudo apt install python3 python3-tk python3-pip python3-pil python3-pil.imagetk yad -y > /dev/null 
yad --progress \
  --title="Dependency Install" \
  --text="All dependencies installed" \
  --percentage=33
  --autoclose
git clone https://github.com/peanutbuttermurmite/BSU.git
pip3 install enquiries selenium PySimpleGUI
yad --progress \
  --title="Python packages " \
  --text="Setting up..." \
  --percentage=66
  --autoclose
cd BSU/bsu-install
chmod ugo+rwx bsu
cd ..
cd ..
sudo mv BSU /opt/applications
yad --progress \
  --title="BSU has no been set up" \
  --text="Installation Complete" \
  --percentage=100
  --autoclose
yad --text "Run BSU by typing "bsu --run" into your terminal or use the .desktop file.Use bsu --help to show all commands (WARNING:use sudo before commands)"
