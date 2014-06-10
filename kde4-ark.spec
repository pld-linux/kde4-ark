#
%define		_state		stable
%define		orgname		ark
%define		qtver		4.8.1
%define		kdeworkspacever	4.11.0

Summary:	K Desktop Environment - archive manager
Name:		kde4-ark
Version:	4.13.2
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	6a5571a8d656219b7059d18c66ff5744
URL:		http://www.kde.org/
BuildRequires:	bzip2-devel
BuildRequires:	kde4-kdebase-devel >= %{version}
BuildRequires:	libarchive-devel
BuildRequires:	xz-devel
BuildRequires:	zlib-devel
Requires:	kde4-kdebase-workspace >= %{kdeworkspacever}
Requires:	libzip
Obsoletes:	kde4-kdeutils-ark
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ark is a program for managing and quickly extracting archives. It
supports arj, rar, zip, tar, zoo, lha and other formats.

%description -l pl.UTF-8
Ark jest programem służącym do zarządzania i szybkiego rozpakowywania
archiwów. Obsługuje archiwa arj, rar, zip, tar, zoo, lha oraz inne
formaty.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ark
%attr(755,root,root) %{_libdir}/kde4/arkpart.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_clilha.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libarchive.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libgz.so
%attr(755,root,root) %{_libdir}/libkerfuffle.so
%attr(755,root,root) %ghost %{_libdir}/libkerfuffle.so.?
%attr(755,root,root) %{_libdir}/libkerfuffle.so.*.*.*
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_cli7z.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_clirar.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_clizip.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libbz2.so
%attr(755,root,root) %{_libdir}/kde4/kerfuffle_libxz.so
%attr(755,root,root) %{_libdir}/kde4/libextracthere.so
%{_datadir}/apps/ark
%{_datadir}/kde4/servicetypes/kerfufflePlugin.desktop
%{_datadir}/kde4/services/ark_part.desktop
%{_datadir}/kde4/services/kerfuffle_libarchive.desktop
%{_datadir}/kde4/services/kerfuffle_libgz.desktop
%{_datadir}/kde4/services/ark_dndextract.desktop
%{_datadir}/kde4/services/kerfuffle_cli7z.desktop
%{_datadir}/kde4/services/kerfuffle_clilha.desktop
%{_datadir}/kde4/services/kerfuffle_clirar.desktop
%{_datadir}/kde4/services/kerfuffle_clizip.desktop
%{_datadir}/kde4/services/kerfuffle_libarchive_readonly.desktop
%{_datadir}/kde4/services/kerfuffle_libbz2.desktop
%{_datadir}/kde4/services/kerfuffle_libxz.desktop
%{_datadir}/kde4/services/ServiceMenus/ark_addtoservicemenu.desktop
%{_datadir}/kde4/services/ServiceMenus/ark_servicemenu.desktop
%{_datadir}/config.kcfg/ark.kcfg
%{_desktopdir}/kde4/ark.desktop
%{_iconsdir}/hicolor/*/apps/ark.*
%{_mandir}/man1/ark.1.*
