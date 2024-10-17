%define	name	OilWar
%define	version	1.2.1
%define	rel	10
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
URL:		https://www.2ndpoint.fi/projektit/oilwar.html
BuildRequires:	SDL_image-devel SDL_mixer-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc ChangeLog README AUTHORS
%attr(2755,root,games) %{_gamesbindir}/*
%{_gamesdatadir}/oilwar
%attr(664,root,games) %{_localstatedir}/lib/games/*.scores
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
%{_datadir}/applications/mandriva-%{name}.desktop


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-10mdv2011.0
+ Revision: 616417
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.2.1-9mdv2010.0
+ Revision: 430198
- rebuild

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 1.2.1-8mdv2009.0
+ Revision: 218434
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
- adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.2.1-8mdv2008.1
+ Revision: 148302
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon May 07 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.2.1-8mdv2008.0
+ Revision: 23944
- fix wrong path in menu item (fixes #30669)
- Import OilWar



* Fri Aug 25 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.1-7mdv2007.0
- add xdg menu

* Tue Jun 20 2006 Lenny Cartier <lenny@mandriva.com> 1.2.1-6mdv2007.0
- rebuild

* Wed May 04 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.2.1-5mdk
- rebuild
- %%mkrel

* Wed Sep 01 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.1-4mdk
- rebuild for new menu (fixes #11024)

* Tue Jun 15 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.1-3mdk
- rebuild

* Thu May 20 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.2.1-2mdk
- change summary macro to avoid possible conflicts if we were to build debug package
- don't bzip2 icons in src.rpm

* Sat Apr 12 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.2.1-1mdk
- initial mdk release
