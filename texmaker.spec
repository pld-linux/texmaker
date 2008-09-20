#
# TODO:	- use system hunspell
#
Summary:	LaTeX development environment
Summary(pl.UTF-8):	Środowisko do tworzenia dokumentów LaTeXa
Name:		texmaker
Version:	1.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Publishing
Source0:	http://www.xm1math.net/texmaker/%{name}-%{version}.tar.bz2
# Source0-md5:	2b59114f02b0e4ad65db78c10c740bf8
Source1:	%{name}.desktop
URL:		http://www.xm1math.net/texmaker/
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	QtGui-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Texmaker is a free LaTeX editor, that integrates many tools needed to
develop documents with LaTeX, in just one application.

%description -l pl.UTF-8
Texmaker to darmowy edytor LaTeXa, który łączy wiele narzędzi
potrzebnych do tworzenia dokumentów LaTeXa w jednej aplikacji.

%prep
%setup -q

%build
export QTDIR="%{_prefix}"
qmake-qt4 -unix texmaker.pro \
	PREFIX="%{_prefix}" \
	CXXFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_datadir}/texmaker}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install utilities/{*.gif,*.png,psheader.txt,*.aff,*.dic,*.qm} $RPM_BUILD_ROOT%{_datadir}/texmaker
for i in latexhelp.html style.css usermanual_en.html usermanual_fr.html; do
	ln -s %{_docdir}/%{name}-%{version}/$i $RPM_BUILD_ROOT%{_datadir}/texmaker
done
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install utilities/texmaker32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}/texmaker.png
# are SVG icons supported?
#install utilities/texmaker.svg $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc utilities/AUTHORS utilities/CHANGELOG.txt utilities/latexhelp.html utilities/style.css utilities/usermanual_*.html
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/en_GB.*
%lang(fr) %{_datadir}/%{name}/fr_FR.*
%lang(fr) %{_datadir}/%{name}/texmaker_fr.qm
%{_datadir}/%{name}/*.css
%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/*.gif
%{_datadir}/%{name}/*.png
%{_datadir}/%{name}/*.txt
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
