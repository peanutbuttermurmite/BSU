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
for f in "${!osInfo[@]}"
do
    if [[ -f $f ]];then
        package_manager=${osInfo[$f]}
    fi
done
(
# =================================================================
echo "# Installing dependencies" ; sleep 2
cleanoutput=">/dev/null"
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
    VAR3="$package_manager$space$PKG$space$cleanoutput"
    $VAR3
done
# =================================================================
echo "33"
echo "# Running Second Task." ; sleep 2
pip="pip3 install"
PYTHONDEPS=(
'enquiries'
'selenium'
'PySimpleGUI'
)
for PYTHONDEP in "${PYTHONDEPS[@]}"; do
    echo "INSTALLING: ${PYTHONDEP}"
    VAR4="$pip$space$PYTHONDEP$space$cleanoutput"
    $VAR4
done
# =================================================================
echo "66"
echo "# Setting Up..." ; sleep 2
(cd .. || exit) 
(cd ..)
(git pull || exit)
(cd BSU/bsu-install || exit)
chmod ugo+rwx bsu 

mv BSU /opt
ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
cp -r bsu.desktop ~/.local/share
# =================================================================
echo "# All finished." ; sleep 2
echo "100"
) |
yad --progress \
  --title="BSU Installer" \
  --text="Installing BSU" \
  --percentage=0 \
  --auto-close \
  --auto-kill

(( $? != 0 )) && zenity --error --text="Error in zenity command."

yad --text "Run BSU by typing "bsu --run" into your terminal or use the .desktop file.Use bsu --help to show all commands (WARNING:Use root for all commands)"
