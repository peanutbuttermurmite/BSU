#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
	printf "Run this script as root" >&2
	exit 1
fi
if ! command -v which &> /dev/null
then
    printf "Dependency which could not be found"
    exit 1
fi
if ! command -v git &> /dev/null
then
    echo "Dependency git could not be found"
    exit 1
fi
if [[ $(which yum) ]]; then
   OS="CentOS"
elif [[ $(which apt) ]]; then
   OS="Debian"
elif [[ $(which apk) ]]; then
   OS="Alpine"
elif [[ $(which zypper) ]]; then
   OS="OpenSuse"
elif [[ $(which pacman) ]]; then
   OS="Arch"
elif [[ $(which dnf) ]]; then
   OS="Fedora"

else
   IS_UNKNOWN=1
fi
if (( IS_UNKNOWN == 1 ))
then 
   printf "OS not found, install a supported package manager"
fi
suse="OpenSuse"
alpine2="Alpine"
cent="CentOS"
redhat="Fedora"
deb="Debian"
pacman="Arch"
if [[ "$OS"=="suse" ]]
then 
    export package_manager="zypper install -y"
elif [[ "$OS" == "alpine2" ]]
then 
    export package_manager="apk --update add"
elif [[ "$OS" == "cent" ]]
then 
    export package_manager="yum install -y"
elif [[ "$OS"=="redhat" ]]
then 
    export package_manager="dnf install -y"
elif [[ "$OS" == "pacman" ]]
then
    export package_manager="pacman -Sy"
elif [[ "$OS" == "deb" ]]
then 
    export package_manager="apt install -y"
else
    if (( IS_UNKNOWN==1 ))
then
    exit 1
fi
space=" "
cleanoutput=" &>/dev/null"
yadtext="yad"
installyad=$package_manager$space$yadtext
$installyad
(
# =================================================================
echo "# Installing dependencies" ; sleep 2
PKGS=(
'python3'
'python3-tk'
'python3-pip'
'python3-pil'
'python3-pil.imagetk'
)

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    VAR3="${package_manager}${space}${PKG}${cleanoutput}"
    $VAR3
done
# =================================================================
echo "33"
echo "# Installing python packages" ; sleep 2
pip="pip3 install"
PYTHONDEPS=(
'enquiries'
'selenium'
'PySimpleGUI'
'pandas'
'brawlstats'
'pythondotenv'
)
for PYTHONDEP in "${PYTHONDEPS[@]}"; do
    echo "INSTALLING: ${PYTHONDEP}"
    VAR4="${pip}${space}${PYTHONDEP}${cleanoutput}"
    $VAR4
done
# =================================================================
echo "66"
echo "# Setting Up..." ; sleep 2
cd .. || exit
git pull
cd .. || exit
cd BSU/bsu-install || exit
chmod ugo+rwx bsu 
cd .. || exit
cd .. || exit
mv BSU /opt
ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
cp -r bsu.desktop ~/.local/share
printf "cd /opt/BSU && git pull && cd ~" >> ~/.bashrc
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
if [ "$?" = -1 ] ; then
        yad --error \
          --text="BSU install canceled."
	  exit 0
fi

yad --text "Run BSU by typing "bsu --run" into your terminal or use the .desktop file.Use bsu --help to show all commands (WARNING:Use root for all commands)"
