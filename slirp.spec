Summary:	TCP/IP emulator for a shell account
Summary(pl):	Emulator TCP/IP dla kont shellowych
Name:		slirp
Version:	1.0c
Release:	5
License:	distributable
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(es):	Red/Utilitarios
Group(pl):	Sieciowe/Narzêdzia
Group(pt_BR):	Rede/Utilitários
Source0:	ftp://blitzen.canberra.edu.au/pub/slirp/%{name}-%{version}.tar.gz
Patch0:		%{name}-glibc.patch
URL:		http://blitzen.canberra.edu.au/slirp/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slirp is a TCP/IP emulator which turns an ordinary shell account into
a (C)SLIP/PPP account. This allows shell users to use all the funky
Internet applications like Netscape, Mosaic, CUSeeMe, etc.

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

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_mandir}/man1}

install src/slirp $RPM_BUILD_ROOT%{_bindir}
install src/slirp.man $RPM_BUILD_ROOT%{_mandir}/man1/slirp.1

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog.gz README.gz 

%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
