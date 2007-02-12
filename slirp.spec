Summary:	TCP/IP emulator for a shell account
Summary(pl.UTF-8):   Emulator TCP/IP dla kont shellowych
Name:		slirp
Version:	1.0.16
Release:	0.1
License:	distributable
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/sourceforge/slirp/%{name}-%{version}.tar.gz
# Source0-md5:	b712f2fe58aaf87172cfd31c95fc1e31
URL:		http://slirp.sourceforge.net/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Slirp is a TCP/IP emulator which turns an ordinary shell account into
a (C)SLIP/PPP account. This allows shell users to use all the funky
Internet applications like Netscape, Mosaic, CUSeeMe, etc.

%description -l pl.UTF-8
Slirp pozwala na dostęp SLIP/PPP posiadaczom zwykłych kont shellowych.
Umożliwia używanie większości aplikacji sieciowych takich jak Netscape
Mosaic, CUSeeMe itp.

%prep
%setup -q

%build
cd src
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/slirp $RPM_BUILD_ROOT%{_bindir}
install src/slirp.man $RPM_BUILD_ROOT%{_mandir}/man1/slirp.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README docs TODO 
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
