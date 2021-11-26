#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
	echo "run this script as root" >&2
	exit 1
fi
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
PKGS=(
'python3'
'python3-tk'
'yad'
'python3-pip'
'python3-pil'
'python3-pil.imagetk'
)
space=" "

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    VAR3="$package_manager$space$PKG"
    $VAR3
done
yad --progress \
  --title="Dependency Install" \
  --text="All dependencies installed" \
  --pulsate \
  --percentage=33 \
  --auto-close
 
git clone https://github.com/peanutbuttermurmite/BSU.git
pip3 install enquiries selenium PySimpleGUI
yad --progress \
  --title="Python packages " \
  --text="Setting up..." \
  --pulsate \
  --percentage=66 \
  --auto-close
cd BSU/bsu-install
chmod ugo+rwx bsu
cd ..
cd ..
mv BSU /opt
ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
cp -r bsu.desktop ~/.local/share
yad --progress \
  --title="BSU has been set up" \
  --text="Installation Complete" \
  --pulsate \
  --percentage=100 \
  --auto-close
yad --text "Run BSU by typing "bsu --run" into your terminal or use the .desktop file.Use bsu --help to show all commands (WARNING:Use root for all commands)"
