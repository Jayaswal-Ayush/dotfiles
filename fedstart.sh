#RPMFUSION
sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm -y
sudo dnf install https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm -y
sudo dnf group update core -y
#FLATPAKS
sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo 
#MULTIMEDIA CODECS
sudo dnf install gstreamer1-plugins-{bad-\*,good-\*,base} gstreamer1-plugin-openh264 gstreamer1-libav --exclude=gstreamer1-plugins-bad-free-devel -y
sudo dnf install lame* --exclude=lame-devel -y
sudo dnf group upgrade --with-optional Multimedia -y
sudo dnf install ffmpeg -y
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
#VIMPLUG
curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
