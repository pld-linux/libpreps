Summary:	libPRepS is the PRepS client/server library
Summary(pl):	libPRepS to biblioteka dla klienta/serwera PRepS
Name:		libpreps
Version:	1.6.5
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://webpages.charter.net/stuffle/linux/preps/%{name}-%{version}.tar.gz
Patch0:		%{name}-postgresql_include_path.patch
Patch1:		%{name}-nostatic.patch
Patch2:		%{name}-plpgsql_include_path.patch
Patch3:		%{name}-scripts_ac.patch
Patch4:		%{name}-shell.patch
Patch5:		%{name}-postgres-server.patch
URL:		http://webpages.charter.net/stuffle/linux/preps/preps.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1.2.0
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel >= 7.0
BuildRequires:	postgresql-module-plpgsql
BuildRequires:	tetex-dvips
# Requires:	postgresql-clients
Requires:	postgresql-module-plpgsql >= 7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RepS is a simple Problem Reporting System. PRepS is designed around
the bug tracking needs of small to medium sized software projects.
However, PRepS may be flexible enough to be used for other types of
problem or status tracking. For example, PRepS could be setup to track
things that need fixing around the house. Be creative.

The libPRepS package contains the server side scripts used to create
and update PRepS databases. It also contains libpreps. libpreps is a
library that contains routines used by the server, as well as some
routines common to the user interface. For that reason, it is needed
for both the server and the client.

%description -l pl
PRepS s³u¿y do kontroli i zarz±dzania b³êdami. PRepS zosta³
zaprojektowany do ma³ych i ¶rednich projektów. Mimo to jest na tyle
elestyczny, ¿e mo¿e byæ u¿ywany przy innych rodzajach problemów
wymagaj±cych kontroli postepu prac. Mo¿e byæ na przyk³ad u¿yty w domu
do nadzoru rzeczy wymagaj±cych naprawy.

Pakiet libPRepS zawiera skrypty umo¿liwiaj±ce tworzenie i aktualizacjê
baz danych dla serwera. Zawiera te¿ bibliotekê libpreps, zawieraj±c±
procedury wykorzystywane przez serwer oraz niektóre procedury wspólne
z interfejsem u¿ytkownika. Z tego powodu jest ona wymagana zarówno
przez serwer, jak i przez klientów.

%package devel
Summary:	Header files for libPRepS
Summary(pl):	Pliki nag³ówkowe dla libPRepS
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
This package is necessary to compile programs which use libPRepS, eg.
PRepS client/server.

%description devel -l pl
Pakiet ten jest niezbêdny podczas kompilacji programów korzystaj±cych
z biblioteki libPRepS, w szególno¶ci klienta/serwera PRepS.

%package static
Summary:	Static library
Summary(pl):	Biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libPRepS static version.

%description static -l pl
Statyczna wersja biblioteki libPRepS.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f --foreign
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog INSTALL NEWS README

rm -f doc/html/Makefile*
mv -f doc/html doc/programmer

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%doc doc/C/prepsdb-admin-manual
%doc doc/C/preps-FAQ
%doc doc/programmer
%doc doc/*.fig
%attr(755,root,root) %{_libdir}/*.so*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}/*.sql
%{_datadir}/%{name}/*.in
%{_datadir}/%{name}/*.msg
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
