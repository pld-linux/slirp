Summary:	TCP/IP emulator for a shell account
Summary(pl):	Emulator TCP/IP dla kont shellowych
Name:		slirp
Version:	1.0c
Release:	4d
Copyright:	distributable
Group:		Networking/Utilities
Group(pl):	Sieci/U¿ytki
#######		ftp://blitzen.canberra.edu.au/pub/slirp
Source:		%{name}-%{version}.tar.gz
Patch:		slirp-glibc.patch
URL:		http://blitzen.canberra.edu.au/slirp/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Slirp is a TCP/IP emulator which turns an ordinary shell account into a
(C)SLIP/PPP account.  This allows shell users to use all the funky Internet
applications like Netscape, Mosaic, CUSeeMe, etc.

%description -l pl
Slirp pozwala na dostêp SLIP/PPP posiadaczom zwyk³ych kont shellowych.
Umo¿liwia u¿ywanie wiêkszo¶ci aplikacji sieciowych takich jak Netscape
Mosaic, CUSeeMe itp.

%prep
%setup -q
%patch

%build
cd src
autoconf
CFLAGS=$RPM_OPT_FLAGS \
    ./configure %{_target_platform} \
	--prefix=/usr

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

install -s src/slirp $RPM_BUILD_ROOT%{_bindir}
install src/slirp.man $RPM_BUILD_ROOT%{_mandir}/man1/slirp.1

bzip2 -9 $RPM_BUILD_ROOT%{_mandir}/man1/* ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.bz2 README.bz2 

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Jan 22 1999 Wojtek ¦lusarczyk <wojtek@shadow.eu.org>
  [1.0c-4d]
- build against glibc-2.1,
- added Group(pl),
- compressed man page && documentation,
- minor changes.

* Tue Jan 19 1999 Konrad Stêpieñ <konrad@interdata.com.pl>
  [1.0c-4]
- Added %attr macros
- Added polish translation

* Sat Dec 27 1997 Alexey Nogin <nogin@dnttm.ru>
 - Added glibc patch

* Sat Jul 5 1997 Timo Karjalainen <timok@iki.fi>
 - Some changes to specfile
 - Removed unnecessary patch
