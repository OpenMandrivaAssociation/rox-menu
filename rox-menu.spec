%define name rox-menu
%define version 1.0.2
%define release %mkrel 6
%define oname ROX-Menu
%define _appsdir	%{_libdir}/apps

Summary: Menu for the panel of the ROX filer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.skepticats.com/rox/dist/%oname-%version.tar.bz2
License: GPL
Group: Graphical desktop/Other
URL: http://www.skepticats.com/rox/rox-menu.html
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: librox-c-devel >= 2.1.3
Requires: rox

%description
ROX-Menu is a simple panel applet for ROX-Filer and the ROX desktop that
pops up a menu that you can use to start your favorite application 
directories.  It serves the same purpose as the KDE "K" menu or the 
Windows "Start" menu.

%prep
%setup -q -n %oname
#gw that version is lib64-aware
cp -f %_libdir/ROX-CLib/Linux-*/bin/rox_run .
chmod 755 Help . Help/*.sh

%build
./AppRun --compile

%install
rm -rf $RPM_BUILD_ROOT
mkdir  -p %buildroot%_appsdir
cp -r ../%oname %buildroot%_appsdir
rm -rf %buildroot%_appsdir/%oname/src
rm -f %buildroot%_appsdir/%oname/makedist.sh
#install a default menu
mkdir -p %buildroot%_datadir/Choices/%oname
ln -s %_appsdir %buildroot%_datadir/Choices/%oname/Menu_Root
chmod 755 %buildroot%_libdir/apps/ROX-Menu/Help/Icons
chmod 644 %buildroot%_libdir/apps/ROX-Menu/Help/Icons/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc %_appsdir/%oname/Help
%dir %_appsdir/%oname
%_appsdir/%oname/.DirIcon
%_appsdir/%oname/App*
%_appsdir/%oname/rox_run
%_appsdir/%oname/Options.xml
%_appsdir/%oname/Linux-*
%_datadir/Choices/%oname


