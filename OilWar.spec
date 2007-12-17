%define	name	OilWar
%define	version	1.2.1
%define	rel	8
%define	release	%mkrel %{rel}
%define	Summary	Very simple mouse shooting game

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Arcade
Source0:	http://www.2ndpoint.fi/projektit/filut/%{name}-%{version}.tar.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch0:		%{name}-fix-scoredir.patch.bz2
URL:		http://www.2ndpoint.fi/projektit/oilwar.html
BuildRequires:	SDL_image-devel SDL_mixer-devel

%description
OilWar is a simple game where you shoot enemy soldiers and tanks with
your mouse. The evil army is attacking your land and tries to steal
your oil. Your mission: waste the invaders, protect the oil, protect
the mother land...

%prep
%setup -q
%patch0 -p0

%build
%configure	--bindir=%{_gamesbindir}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_menudir}
cat <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/oilwar" \
		icon=%{name}.png \
		needs="x11" \
		section="More Applications/Games/Arcade" \
		title="%{name}"\
		longtitle="%{Summary}" \
		xdg="true"
EOF

install -d %{buildroot}%{_datadir}/applications
cat <<EOF > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{_gamesbindir}/oilwar
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ArcadeGame;X-MandrivaLinux-MoreApplications-Games-Arcade;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(2755,root,games) %{_gamesbindir}/*
%{_gamesdatadir}/oilwar
%attr(664,root,games) %{_localstatedir}/games/*.scores
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_menudir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop
