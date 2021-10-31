#!/bin/bash
declare -A osInfo;
osInfo[/etc/debian_version]="apt install -y"
osInfo[/etc/alpine-release]="apk --update add"
osInfo[/etc/centos-release]="yum install -y"
osInfo[/etc/fedora-release]="dnf install -y"
for f in ${!osInfo[@]}
do
    if [[ -f $f ]];then
        package_manager=${osInfo[$f]}
    fi
done
package1="python3 > /dev/null"
package2="python3-tk > /dev/null"
package3="yad > /dev/null"
package4="python3-pip > /dev/null"
package5="python3-pil > /dev/null"
package6="python3-pil.imagetk > /dev/null"
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
sudo mv BSU /opt
sudo ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
sudo cp -r bsu.desktop ~/.local/share
yad --progress \
  --title="BSU has been set up" \
  --text="Installation Complete" \
  --percentage=100
  --autoclose
yad --text "Run BSU by typing "bsu --run" into your terminal or use the .desktop file.Use bsu --help to show all commands (WARNING:use sudo before commands)"
