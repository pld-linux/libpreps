Summary:	libPRepS is the PRepS client/server library
Summary(pl):	libPRepS to biblioteka dla klienta/serwera PRepS
Name:		libpreps
Version:	1.6.5
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	http://webpages.charter.net/stuffle/linux/preps/%{name}-%{version}.tar.gz
Patch0:		%{name}-postgresql_include_path.patch
Patch1:		%{name}-nostatic.patch
Patch2:		%{name}-plpgsql_include_path.patch
Patch3:		%{name}-scripts_ac.patch
Patch4:		%{name}-shell.patch
URL:		http://webpages.charter.net/stuffle/linux/preps/preps.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:  glib-devel >= 1.2.0
BuildRequires:	postgresql-backend-devel
BuildRequires:	postgresql-devel >= 7.0
BuildRequires:	postgresql-module-plpgsql
BuildRequires:  tetex-dvips
# Requires:	postgresql-clients
Requires:       postgresql-module-plpgsql >= 7.0
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
PRepS s≥uøy do kontroli i zarz±dzania b≥Ídami. PRepS zosta≥
zaprojektowany do ma≥ych i ∂rednich projektÛw. Mimo to jest na tyle
elestyczny, øe moøe byÊ uøywany przy innych rodzajach problemÛw
wymagaj±cych kontroli postepu prac. Moøe byÊ na przyk≥ad uøyty w domu
do nadzoru rzeczy wymagaj±cych naprawy.

Pakiet libPRepS zawiera skrypty umoøliwiaj±ce tworzenie i aktualizacjÍ
baz danych dla serwera. Zawiera teø bibliotekÍ libpreps, zawieraj±c±
procedury wykorzystywane przez serwer oraz niektÛre procedury wspÛlne
z interfejsem uøytkownika. Z tego powodu jest ona wymagana zarÛwno
przez serwer, jak i przez klientÛw.

%package devel
Summary:        Header files for libPRepS
Summary(pl):    Pliki nag≥Ûwkowe dla libPRepS
Group:          Development/Libraries
Group(de):      Entwicklung/Libraries
Group(es):      Desarrollo/Bibliotecas
Group(fr):      Development/Librairies
Group(pl):      Programowanie/Biblioteki
Group(pt_BR):   Desenvolvimento/Bibliotecas
Group(ru):      Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):      Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:       %{name} = %{version}

%description devel
This package is necessary to compile programs which use libPRepS,
eg. PRepS client/server.

%description devel -l pl
Pakiet ten jest niezbÍdny podczas kompilacji programÛw korzystaj±cych
z biblioteki libPRepS, w szegÛlno∂ci klienta/serwera PRepS.

%package static
Summary:        Static library
Summary(pl):    Biblioteka statyczna
Group:          Development/Libraries
Group(de):      Entwicklung/Libraries
Group(es):      Desarrollo/Bibliotecas
Group(fr):      Development/Librairies
Group(pl):      Programowanie/Biblioteki
Group(pt_BR):   Desenvolvimento/Bibliotecas
Group(ru):      Ú¡⁄“¡¬œ‘À¡/‚…¬Ã…œ‘≈À…
Group(uk):      Úœ⁄“œ¬À¡/‚¶¬Ã¶œ‘≈À…
Requires:       %{name}-devel = %{version}

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

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c
%configure
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog COPYING INSTALL NEWS README

rm -f doc/html/Makefile*
mv doc/html doc/programmer

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

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.la
