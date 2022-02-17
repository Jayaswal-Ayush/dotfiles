#POPOS THEME
sudo dnf install sassc meson glib2-devel -y
sudo dnf install inkscape optipng -y
sudo dnf remove pop-gtk-theme -y
sudo rm -rf /usr/share/themes/Pop* 
rm -rf ~/.local/share/themes/Pop*
rm -rf ~/.themes/Pop*
mkdir tmp
cd tmp
git clone https://github.com/pop-os/gtk-theme.git
cd gtk-theme
meson build && cd build
ninja
ninja install