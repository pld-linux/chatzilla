Summary:	IRC in Mozilla, aka ChatZilla
Summary(pl.UTF-8):   IRC w Mozilli, znany też jako ChatZilla
Name:		chatzilla
Version:	0.9.77
Release:	1
License:	GPL v2
Group:		X11/Applications/Networking
Source0:	http://chatzilla.rdmsoft.com/xulrunner/download/%{name}-%{version}-xr.zip
# Source0-md5:	b14c59ebc541454da2e2c4ce375c8679
Source1:	%{name}.desktop
URL:		http://chatzilla.rdmsoft.com/xulrunner/
Requires:	xulrunner
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_desktopdir}}

cat <<'EOF' > $RPM_BUILD_ROOT%{_bindir}/%{name}
#!/bin/sh
exec %{_bindir}/xulrunner %{_appdir}/application.ini
EOF
chmod a+x $RPM_BUILD_ROOT%{_bindir}/%{name}
cp -a application.ini $RPM_BUILD_ROOT%{_appdir}
cp -a chrome components defaults extensions $RPM_BUILD_ROOT%{_appdir}
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

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
