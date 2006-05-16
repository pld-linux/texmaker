Summary:	LaTeX development environment
Summary(pl):	¦rodowisko do tworzenia dokumentów LaTeXa
Name:		texmaker
Version:	1.3
Release:	0.1
License:	GPL
Group:		Applications/Publishing
Source0:	http://www.xm1math.net/texmaker/%{name}-%{version}.tar.bz2
# Source0-md5:	17f91175a32827e9c9f45dc7a20a0c2b
Source1:	%{name}.desktop
URL:		http://www.xm1math.net/texmaker/
BuildRequires:	qmake
BuildRequires:	qt-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Texmaker is a free LaTeX editor, that integrates many tools needed to
develop documents with LaTeX, in just one application.

%description -l pl
Texmaker to darmowy edytor LaTeXa, który ³±czy wiele narzêdzi
potrzebnych do tworzenia dokumentów LaTeXa w jednej aplikacji.

%prep
%setup -q

%build
export QTDIR="%{_prefix}"
qmake -unix texmaker.pro \
	PREFIX="%{_prefix}" \
	CXXFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_datadir}/texmaker}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install utilities/{*.png,*.gif,usermanual.html,style.css} $RPM_BUILD_ROOT%{_datadir}/texmaker
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install utilities/texmaker32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}/texmaker.png
# are SVG icons supported?
#install utilities/texmaker.svg $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc utilities/AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*
%{_pixmapsdir}/*
