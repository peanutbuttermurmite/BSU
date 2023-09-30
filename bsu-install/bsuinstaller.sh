#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
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
    printf "OS not compatible, see wiki for more info"
    exit 1
fi
space=" "
    

PKGS=(
'python3'
'python3-tk'
'python3-pip'
'python3-pil'
'python3-pil.imagetk'
'python3-dotenv'
'whiptail'
)
{
  echo "0"
for PKG in "${PKGS[@]}"; do
    printf "INSTALLING: ${PKG}"
    VAR3="${package_manager}${space}${PKG}"
    $VAR3 > /dev/null 2>&1
done
  echo "28"
pip="pip3 install"
PYTHONDEPS=(
'PySimpleGUI'
'pandas'
'brawlstats'
)
  echo "40"
for PYTHONDEP in "${PYTHONDEPS[@]}"; do
    echo "INSTALLING: ${PYTHONDEP}"
    VAR4="${pip}${space}${PYTHONDEP}"
    $VAR4 > /dev/null 2>&1
done
  echo "52"
cd .. && git pull
  echo "64"
cd bsu-install && chmod u+x bsu && cp -r bsu.desktop ~/.local/share/applications
cd ..
cd ..


mv BSU /opt
ln -s /opt/BSU/bsu-install/bsu /usr/local/bin/bsu
printf "cd /opt/BSU && git pull && cd -" >> ~/.bashrc
sleep 0.1
echo "78"
sleep 0.1 
echo "88"
sleep 0.1
  echo "100"
} |whiptail --title "BSU Install" --gauge "Please wait while installing" 6 60 0
if [ "$?" = -1 ] ; then
        whiptail --title "Installation Failed" --msgbox "The installation has been aborted" $(stty -a | tr \; \\012 |
    grep -E 'rows|columns' | cut '-d ' -f3)
	  exit 0
fi

whiptail --title "Getting Started with BSU" --msgbox "Run BSU by typing 'bsu --run' into your terminal or use the .desktop file.Use 'bsu --help' to show all commands" $(stty -a | tr \; \\012 |
    grep -E 'rows|columns' | cut '-d ' -f3)
