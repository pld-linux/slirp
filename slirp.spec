Summary:	TCP/IP emulator for a shell account
Summary(pl):	Emulator TCP/IP dla kont shellowych
Name:		slirp
Version:	1.0c
Release:	5
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
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

install -s src/slirp $RPM_BUILD_ROOT%{_bindir}
install src/slirp.man $RPM_BUILD_ROOT%{_mandir}/man1/slirp.1

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.gz README.gz 

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
