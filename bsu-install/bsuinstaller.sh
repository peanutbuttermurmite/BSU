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
package1="python3"
package2="python3-tk"
package3="yad"
package4="python3-pip"
package5="python3-pil"
package6="python3-pil.imagetk"
${package_manager} ${package1} >/dev/null
${package_manager} ${package2} >/dev/null
${package_manager} ${package3} >/dev/null
${package_manager} ${package4} >/dev/null
${package_manager} ${package5} >/dev/null
${package_manager} ${package6} >/dev/null
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
