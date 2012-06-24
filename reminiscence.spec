%define		_vname REminiscence
Summary:	Free reimplementation of the Flashback engine
Summary(pl):	Wolnodost�pna reimplementacja silnika gry Flashback
Name:		reminiscence
Version:	0.1.5
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://membres.lycos.fr/cyxdown/reminiscence/%{_vname}-%{version}.tar.bz2
# Source0-md5:	06fc5630e64ed309e6cc965cdb5a12f7
URL:		http://membres.lycos.fr/cyxdown/reminiscence/
BuildRequires:	SDL-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
REminiscence is a re-implementation of the engine used in the game Flashback
made by Delphine Software and released in 1992. 

Please be aware that, currently, this implementation is not yet complete.

%description -l pl
REminiscence to reimplementacja silnika u�ytego w grze Flashback
stworzonej przez Delphine Software i opublikowanej w 1992 roku.

Warto pami�ta�, �e na chwil� obecn� ta implementacja jest jeszcze
niekompletna.

%prep
%setup -q -n %{_vname}-%{version}

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags} `sdl-config --cflags` -DSYS_LITTLE_ENDIAN"
	LDFLAGS="%{rpmldflags} `sdl-config --libs`"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install rs $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/*
