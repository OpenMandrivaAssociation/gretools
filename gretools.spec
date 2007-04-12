%define name gretools
%define version 1.2.4
%define release %mkrel 3 

%define localstatedir /var/lib
%define _localstatedir %localstatedir

Name:		%name
Summary:	Vocabulary building tool for GNOME
Version:	%version
Release:	%release
License:	GPL
Group:		Games/Other
Source:		http://theory.cs.iitm.ernet.in/~arvindn/gretools/1.2/%{name}-%{version}.tar.bz2
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
BuildRequires: rpm >= 0:4.1
BuildRequires: desktop-file-utils >= 0:0.2.92

Requires(post):         GConf2
Requires(postun):         GConf2
Requires(post):         /usr/bin/gconftool-2
Requires(postun):         /usr/bin/gconftool-2

BuildRequires:  pygtk2.0-devel >= %{gnome_python2_version}

%description
Gretools consists of a synonym quiz and a word guessing game.
It is very useful for preparing for word tests.

%prep
%setup -q

%build

%configure

%make 

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

# Menu
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-MoreApplications-Education" \
  --add-category="Education" \
  --add-category="GNOME" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

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


