#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
	printf "Run this script as root" >&2
	rootless=True
fi
rootless=False
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
if ! command -v whiptail &> /dev/null
then
    echo "Dependency whiptail could not be found"
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
if [[ "$OS" == "$suse" ]]
then 
    export package_manager="zypper install -y"
fi
if [[ "$OS" == "$alpine2" ]]
then 
    export package_manager="apk --update add"
fi
if [[ "$OS" == "$cent" ]]
then 
    export package_manager="yum install -y"
fi
if [[ "$OS" == "$redhat" ]]
then 
    export package_manager="dnf install -y"
fi
if [[ "$OS" == "$pacman" ]]
then
    export package_manager="pacman -Sy"
fi
if [[ "$OS" == "$deb" ]]
then 
    export package_manager="apt install -y"
fi
if (( IS_UNKNOWN==1 ))
then
    exit 1
fi
space=" "
if (whiptail --title "BSU Installation" --yesno "Would you like to install offline capabilities?" $(stty -a | tr \; \\012 |
    egrep 'rows|columns' | cut '-d ' -f3)); then
    printf "Offline capabilities will be installed"
    offlinemode=True
else
    printf "Offline capabilities will not be installed"
    offlinemode=False
fi   

PKGS=(
'python3'
'python3-tk'
'python3-pip'
'python3-pil'
'python3-pil.imagetk'
'python3-dotenv'
'fontconfig'
)
{
  echo "0"
for PKG in "${PKGS[@]}"; do
    printf "INSTALLING: ${PKG}"
    VAR3="${package_manager}${space}${PKG}"
    $VAR3  > /dev/null 2>&1
done
  echo "28"
pip="pip3 install"
PYTHONDEPS=(
'PySimpleGUI'
'pandas'
'brawlstats'
)
  echo "46"
for PYTHONDEP in "${PYTHONDEPS[@]}"; do
    echo "INSTALLING: ${PYTHONDEP}"
    VAR4="${pip}${space}${PYTHONDEP}"
    $VAR4 > /dev/null 2>&1
done
  echo "75"
cd .. 
git pull
cd .. 
cd BSU/bsu-install
chmod ugo+rwx bsu 
cp -r bsu.desktop ~/.local/share/applications
cd .. 
cd ..
mv BSU /opt
ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
printf "cd /opt/BSU && git pull && cd -" >> ~/.bashrc
  echo "100"
} |whiptail --title "BSU Install" --gauge "Please wait while installing" 6 60 0
if [ "$?" = -1 ] ; then
        whiptail --title "Installation Failed" --msgbox "The installation has been aborted" $(stty -a | tr \; \\012 |
    egrep 'rows|columns' | cut '-d ' -f3)
	  exit 0
fi

whiptail --title "Getting Started with BSU" --msgbox "Run BSU by typing 'bsu --run' into your terminal or use the .desktop file.Use 'bsu --help' to show all commands" $(stty -a | tr \; \\012 |
    egrep 'rows|columns' | cut '-d ' -f3)
