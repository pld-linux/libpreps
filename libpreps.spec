Summary:	libPRepS is the PRepS client/server library
Summary(pl.UTF-8):	libPRepS to biblioteka dla klienta/serwera PRepS
Name:		libpreps
Version:	1.9.0
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://webpages.charter.net/stuffle/linux/preps/%{name}-%{version}.tar.gz
# Source0-md5:	a23d6fb06a4bb09eca4f8f7da3e139ae
Patch0:		%{name}-nostatic.patch
Patch1:		%{name}-plpgsql_include_path.patch
Patch2:		%{name}-shell.patch
Patch3:		%{name}-postgres-server.patch
Patch4:		%{name}-glibc.patch
URL:		http://webpages.charter.net/stuffle/linux/preps/preps.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	postgresql-backend-devel >= 7.2
BuildRequires:	postgresql-devel >= 7.2
BuildRequires:	tetex-dvips
# Requires:	postgresql-clients
Requires:	postgresql-module-plpgsql >= 7.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RepS is a simple Problem Reporting System. PRepS is designed around
the bug tracking needs of small to medium sized software projects.
However, PRepS may be flexible enough to be used for other types of
problem or status tracking. For example, PRepS could be setup to track
things that need fixing around the house. Be creative.

The libPRepS package contains the server side scripts used to create
and update PRepS databases. It also contains libpreps. libpreps is a
library that contains routines used by the server.

%description -l pl.UTF-8
PRepS służy do kontroli i zarządzania błędami. PRepS został
zaprojektowany do małych i średnich projektów. Mimo to jest na tyle
elastyczny, że może być używany przy innych rodzajach problemów
wymagających kontroli postępu prac. Może być na przykład użyty w domu
do nadzoru rzeczy wymagających naprawy.

Pakiet libPRepS zawiera skrypty umożliwiające tworzenie i aktualizację
baz danych dla serwera. Zawiera też bibliotekę libpreps, zawierającą
procedury wykorzystywane przez serwer.

%package devel
Summary:	Header files for libPRepS
Summary(pl.UTF-8):	Pliki nagłówkowe dla libPRepS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
This package is necessary to compile programs which use libPRepS, eg.
PRepS server.

%description devel -l pl.UTF-8
Pakiet ten jest niezbędny podczas kompilacji programów korzystających
z biblioteki libPRepS, w szczególności serwera PRepS.

%package static
Summary:	Static libPRepS library
Summary(pl.UTF-8):	Biblioteka statyczna libPRepS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libPRepS library.

%description static -l pl.UTF-8
Statyczna wersja biblioteki libPRepS.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f doc/html/Makefile*
mv -f doc/html doc/programmer

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README doc/*.fig
%doc doc/C/{prepsdb-admin-manual,preps-FAQ}
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_datadir}/libpreps
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/programmer
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/preps

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
