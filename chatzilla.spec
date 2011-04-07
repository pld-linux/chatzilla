Summary:	IRC in Mozilla, aka ChatZilla
Summary(pl.UTF-8):	IRC w Mozilli, znany też jako ChatZilla
Name:		chatzilla
Version:	0.9.86.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://chatzilla.rdmsoft.com/xulrunner/download/%{name}-%{version}-xr.zip
# Source0-md5:	4ba49087521f6c0cb0eb6ca6a4797f72
Source1:	%{name}.desktop
URL:		http://chatzilla.rdmsoft.com/xulrunner/
BuildRequires:	unzip
Requires:	xulrunner >= 1.9.0.4
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
ChatZilla is an IRC client that is written entirely in JavaScript and
XUL.

%description -l pl.UTF-8
ChatZilla to klient IRC-a napisany całkowicie w JavaScripcie i XUL-u.

%prep
%setup -qc

cat <<'EOF' > %{name}.sh
#!/bin/sh
exec %{_bindir}/xulrunner %{_appdir}/application.ini
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_desktopdir}}

install -p %{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -p application.ini $RPM_BUILD_ROOT%{_appdir}
cp -a chrome components defaults extensions $RPM_BUILD_ROOT%{_appdir}
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}

%dir %{_appdir}
%{_appdir}/application.ini
%dir %{_appdir}/components
%{_appdir}/components/*.js
%{_appdir}/chrome
%{_appdir}/defaults
%dir %{_appdir}/extensions
%{_appdir}/extensions/{972ce4c6-7e08-4474-a285-3208198ce6fd}

%{_desktopdir}/chatzilla.desktop
