#!/bin/bash
if [ "$(id -u)" -ne 0 ]; then
	echo "run this script as root" >&2
	exit 1
fi
if [ -f /etc/os-release ]; then
    # freedesktop.org and systemd
    . /etc/os-release
    OS=$NAME
    VER=$VERSION_ID
elif type lsb_release >/dev/null 2>&1; then
    # linuxbase.org
    OS=$(lsb_release -si)
    VER=$(lsb_release -sr)
elif [ -f /etc/lsb-release ]; then
    # For some versions of Debian/Ubuntu without lsb_release command
    . /etc/lsb-release
    OS=$DISTRIB_ID
    VER=$DISTRIB_RELEASE
elif [ -f /etc/debian_version ]; then
    # Older Debian/Ubuntu/etc.
    OS=Debian
    VER=$(cat /etc/debian_version)
elif [ -f /etc/SuSe-release ]; then
    # Older SuSE/etc.
    ...
elif [ -f /etc/redhat-release ]; then
    # Older Red Hat, CentOS, etc.
    ...
else
    # Fall back to uname, e.g. "Linux <version>", also works for BSD, etc.
    OS=$(uname -s)
    VER=$(uname -r)
fi
ubu="Ubuntu"
suse="OpenSuse"
alpine2="Alpine"
cent="CentOS"
redhat="Fedora"
deb="Debian"
pacman="Arch"

if (( OS==ubu )) 
then
    package_manager="apt install -y"
fi 
if (( OS==suse ))
then 
    package_manager="zypper install -y"
fi
if (( OS==alpine2 ))
then 
    package_manager="apk --update add"
fi
if (( OS==cent ))
then 
    package_manager="yum install -y"
fi
if (( OS==redhat ))
then 
    package_manager="dnf install -y"
fi
if (( OS==deb ))
then 
    package_manager="apt install -y"
fi
if (( OS==pacman ))
then
    package_manager="pacman -Sy"
fi
space=" "
yadtext="yad"
installyad=$package_manager$space$yadtext
$installyad
(
# =================================================================
echo "# Installing dependencies" ; sleep 2
cleanoutput="> /dev/null 2> /dev/null"
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
