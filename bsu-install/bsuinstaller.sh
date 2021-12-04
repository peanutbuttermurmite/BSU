#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
	echo "run this script as root" >&2
	exit 1
fi
if ! command -v awk &> /dev/null
then
    exit 1
fi

os=$(awk '/^ID=/' /etc/*-release | awk -F'=' '{ print tolower($2) }')
ubu="ubuntu"
suse="opensuse"
alpine2="alpine"
cent="centos"
redhat="fedora"
deb="debian"
pacman="arch"

if (( $os==$ubu )) 
then
    package_manager="apt install -y"
fi 
if (( $os==$suse ))
then 
    package_manager="zypper install -y"
fi
if (( $os==$alpine2 ))
then 
    package_manager="apk --update add"
fi
if (( $os==$cent ))
then 
    package_manager="yum install -y"
fi
if (( $os==$redhat ))
then 
    package_manager="dnf install -y"
fi
if (( $os==$deb ))
then 
    package_manager="apt install -y"
fi
if (( $os==$pacman ))
then
    package_manager="pacman -Sy"
fi
space=" "
yad="yad"
installyad=$package_manager$space$yad
$installyad
(
# =================================================================
echo "# Installing dependencies" ; sleep 2
cleanoutput=">/dev/null"
PKGS=(
'python3'
'python3-tk'
'python3-pip'
'python3-pil'
'python3-pil.imagetk'
)

for PKG in "${PKGS[@]}"; do
    echo "INSTALLING: ${PKG}"
    VAR3="$package_manager$space$PKG$space$cleanoutput"
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
    VAR4="$pip$space$PYTHONDEP$space$cleanoutput"
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
