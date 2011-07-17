Summary:	TCP/IP emulator for a shell account
Summary(pl.UTF-8):	Emulator TCP/IP dla kont shellowych
Name:		slirp
Version:	1.0.17
Release:	1
License:	BSD
Group:		Networking/Utilities
Source0:	http://downloads.sourceforge.net/slirp/%{name}-1.0.16.tar.gz
# Source0-md5:	b712f2fe58aaf87172cfd31c95fc1e31
Source1:	http://downloads.sourceforge.net/slirp/%{name}_1_0_17_patch.tar.gz
# Source1-md5:	3662f4b696b6103e736063a31317d6f5
Patch0:		%{name}-build.patch
Patch1:		%{name}-link.patch
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
%setup -q -n %{name}-1.0.16
mkdir -p patch
%{__tar} xzf %{SOURCE1} -C patch
mv patch/README README-1.0.17
cd src
patch -p1 <../patch/fix17.patch
cd ..
%patch0 -p1
%patch1 -p1

%build
cd src
%{__autoconf}
%configure

# avoid running mkpro, breaks pointers in args
%{__make} \
	MAKEPRO='touch $@'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install src/slirp $RPM_BUILD_ROOT%{_bindir}
install src/slirp.man $RPM_BUILD_ROOT%{_mandir}/man1/slirp.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog README README-1.0.17 README.NEXT TODO docs
%attr(755,root,root) %{_bindir}/slirp
%{_mandir}/man1/slirp.1*
