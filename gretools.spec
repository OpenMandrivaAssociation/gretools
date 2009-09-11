%define name gretools
%define version 1.2.4
%define release %mkrel 6

%define localstatedir /var/lib
%define _localstatedir %localstatedir

Name:		%name
Summary:	Vocabulary building tool for GNOME
Version:	%version
Release:	%release
License:	GPL
Group:		Games/Other
Source:		http://theory.cs.iitm.ernet.in/~arvindn/gretools/1.2/%{name}-%{version}.tar.bz2
Patch0:		gretools-1.2.4-fix-desktop-file.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://theory.cs.iitm.ernet.in/~arvindn/gretools/
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


