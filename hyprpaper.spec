Name:           hyprpaper
Version:        0.7.5
Release:        3
Summary:        Blazing fast wayland wallpaper utility with IPC controls
Group:          Hyprland
License:        BSD-3-Clause AND HPND-sell-variant
URL:            https://github.com/hyprwm/hyprpaper
Source0:        https://github.com/hyprwm/hyprpaper/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(glesv2)
BuildRequires:  pkgconfig(hyprlang)
BuildRequires:  pkgconfig(hyprwayland-scanner)
BuildRequires:  pkgconfig(hyprutils)
BuildRequires:  pkgconfig(hyprgraphics)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libmagic)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)

Requires:  hyprlang
Requires:  hyprutils
Requires:  hyprgraphics

%description
Hyprpaper is a blazing fast wallpaper utility for Hyprland with the ability
to dynamically change wallpapers through sockets. It will work on all
wlroots-based compositors, though.

%prep
%autosetup -p1

%build
make protocols
%cmake
%make_build

%install
%make_install -C build

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_userunitdir}/hyprpaper.service
