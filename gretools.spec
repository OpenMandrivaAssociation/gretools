%define localstatedir /var/lib
%define _localstatedir %localstatedir

Name:		gretools
Summary:	Vocabulary building tool for GNOME
Version:	1.2.4
Release:	8
License:	GPL
Group:		Games/Other
Source:		http://theory.cs.iitm.ernet.in/~arvindn/gretools/1.2/%{name}-%{version}.tar.bz2
Patch0:		gretools-1.2.4-fix-desktop-file.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		https://theory.cs.iitm.ernet.in/~arvindn/gretools/
Buildarch:	noarch

Requires: python 
Requires: gnome-python >= 2.0.0
Requires: gnome-python-gconf
Requires: pyorbit 
Requires: pygtk2.0 
Requires: pygtk2.0-libglade 
                                                                                                               
BuildRequires: scrollkeeper 
BuildRequires: automake >= 0:1.6
BuildRequires: autoconf >= 0:2.52

Requires(post):         GConf2
Requires(postun):         GConf2
Requires(post):         /usr/bin/gconftool-2
Requires(postun):         /usr/bin/gconftool-2

BuildRequires:  pygtk2.0-devel 

%description
Gretools consists of a synonym quiz and a word guessing game.
It is very useful for preparing for word tests.

%prep
%setup -q
%patch0 -p0

%build
%configure2_5x
%make 

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

rm -rf $RPM_BUILD_ROOT%{_localstatedir}/scrollkeeper

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc COPYING ChangeLog INSTALL README
%{_bindir}/*
%{_datadir}/gnome/help
%{_datadir}/pixmaps/gretools.png
%{_datadir}/gretools/glade/*.glade
%{_datadir}/gretools/lists/*.wl
%{_datadir}/applications/*.desktop
%{_datadir}/omf/gretools
%{py_puresitedir}/*

%post
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi                                                                                                               
%postun
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q || true ; fi




%changelog
* Fri Nov 12 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 1.2.4-7mdv2011.0
+ Revision: 596952
- rebuild for python 2.7

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 1.2.4-6mdv2010.0
+ Revision: 437814
- rebuild

  + Funda Wang <fwang@mandriva.org>
    - fix desktop file

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 1.2.4-5mdv2009.1
+ Revision: 325578
- fix BR
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Tue Dec 19 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.2.4-3mdv2007.0
+ Revision: 99238
- Fix file list
- Fix menu
- Rebuild against new python
- Fix menu entry
- Remove prereq deprecated macros
- Import gretools

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 1.2.4-2mdk
- Rebuild for new python

* Fri Oct 01 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.4-1mdk
- 1.2.4

* Wed Jun 16 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-2mdk
- rebuild

* Thu Feb 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.2.3-1mdk
- 1.2.3
- from Arvind Narayanan <arvindn users sourceforge net> :
	- Added epoch and some other fedora oriented changes

* Tue Jan 20 2004 Arvind Narayanan <arvindn users sourceforge net>
- Wrote Requires and Buildrequires
- updated %%doc

* Fri Jan 16 2004 Arvind Narayanan <arvindn users sourceforge net>
- Copied spec file from gnome-blog

