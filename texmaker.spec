#
# TODO:	- use system hunspell
# TODO: pl.UTF-8: summary, description
#
%define		qt_ver	5.7
Summary:	LaTeX development environment
Summary(hu.UTF-8):	LaTeX fejlesztői környezet
Summary(pl.UTF-8):	Środowisko do tworzenia dokumentów LaTeXa
Name:		texmaker
Version:	5.0.2
Release:	1
License:	GPL
Group:		X11/Applications/Publishing
Source0:	http://www.xm1math.net/texmaker/%{name}-%{version}.tar.bz2
# Source0-md5:	9157bd4838caa69cbd6e377a2e980084
Source1:	%{name}.desktop
URL:		http://www.xm1math.net/texmaker/
BuildRequires:	Qt5Concurrent-devel >= %{qt_ver}
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5Gui-devel >= %{qt_ver}
BuildRequires:	Qt5Network-devel >= %{qt_ver}
BuildRequires:	Qt5PrintSupport-devel >= %{qt_ver}
BuildRequires:	Qt5Script-devel >= %{qt_ver}
BuildRequires:	Qt5WebKit-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	Qt5Xml-devel >= %{qt_ver}
BuildRequires:	poppler-qt5-devel
BuildRequires:	qt5-build
BuildRequires:	qt5-qmake
Requires:	Qt5Concurrent >= %{qt_ver}
Requires:	Qt5Core >= %{qt_ver}
Requires:	Qt5Gui >= %{qt_ver}
Requires:	Qt5Network >= %{qt_ver}
Requires:	Qt5PrintSupport >= %{qt_ver}
Requires:	Qt5Script >= %{qt_ver}
Requires:	Qt5WebKit >= %{qt_ver}
Requires:	Qt5Widgets >= %{qt_ver}
Requires:	Qt5Xml >= %{qt_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Texmaker is a free LaTeX editor, that integrates many tools needed to
develop documents with LaTeX, in just one application.

%description  -l hu.UTF-8
Texmaker egy ingyenes LaTeX szerkesztő, amely eszközök tömkelegét
integrálja egybe LaTeX dokumentumok fejlesztéséhez.

%description -l pl.UTF-8
Texmaker to darmowy edytor LaTeXa, który łączy wiele narzędzi
potrzebnych do tworzenia dokumentów LaTeXa w jednej aplikacji.

%prep
%setup -q

%build
qmake-qt5 -unix texmaker.pro \
	PREFIX="%{_prefix}" \
	QMAKE_CXXFLAGS="%{rpmcflags}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir},%{_datadir}/texmaker}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install utilities/*.png dictionaries/{*.aff,*.dic} locale/*.qm \
	$RPM_BUILD_ROOT%{_datadir}/texmaker
cd doc
for i in *; do
	ln -s %{_docdir}/%{name}-%{version}/doc/$i $RPM_BUILD_ROOT%{_datadir}/texmaker
done
cd ..
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install utilities/texmaker32x32.png $RPM_BUILD_ROOT%{_pixmapsdir}/texmaker.png
install utilities/texmaker.svg $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc utilities/AUTHORS utilities/CHANGELOG.txt dictionaries/*.txt doc
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/en_GB.*
%{_datadir}/%{name}/en_US.*
%lang(cs) %{_datadir}/%{name}/cs_CZ.*
%lang(de) %{_datadir}/%{name}/de_DE.*
%lang(es) %{_datadir}/%{name}/es_ES.*
%lang(fr) %{_datadir}/%{name}/fr_FR.*
%lang(hu) %{_datadir}/%{name}/hu_HU.*
%lang(it) %{_datadir}/%{name}/it_IT.*
%lang(nl) %{_datadir}/%{name}/nl_NL.*
%lang(pl) %{_datadir}/%{name}/pl_PL.*
%lang(cs) %{_datadir}/%{name}/qt_cs.qm
%lang(de) %{_datadir}/%{name}/qt_de.qm
%lang(es) %{_datadir}/%{name}/qt_es.qm
%lang(fa) %{_datadir}/%{name}/qt_fa.qm
%lang(fr) %{_datadir}/%{name}/qt_fr.qm
%lang(pl) %{_datadir}/%{name}/qt_pl.qm
%lang(pt) %{_datadir}/%{name}/qt_pt.qm
%lang(ru) %{_datadir}/%{name}/qt_ru.qm
%lang(zh_CN) %{_datadir}/%{name}/qt_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/qt_zh_TW.qm
%lang(ar) %{_datadir}/%{name}/texmaker_ar.qm
%lang(ca) %{_datadir}/%{name}/texmaker_ca.qm
%lang(cs) %{_datadir}/%{name}/texmaker_cs.qm
%lang(da) %{_datadir}/%{name}/texmaker_da.qm
%lang(de) %{_datadir}/%{name}/texmaker_de.qm
%lang(el) %{_datadir}/%{name}/texmaker_el.qm
%lang(es) %{_datadir}/%{name}/texmaker_es.qm
%lang(fa) %{_datadir}/%{name}/texmaker_fa.qm
%lang(fr) %{_datadir}/%{name}/texmaker_fr.qm
%lang(gl) %{_datadir}/%{name}/texmaker_gl.qm
%lang(hu) %{_datadir}/%{name}/texmaker_hu.qm
%lang(it) %{_datadir}/%{name}/texmaker_it.qm
%lang(lv) %{_datadir}/%{name}/texmaker_lv.qm
%lang(nl) %{_datadir}/%{name}/texmaker_nl.qm
%lang(pl) %{_datadir}/%{name}/texmaker_pl.qm
%lang(pt) %{_datadir}/%{name}/texmaker_pt_BR.qm
%lang(pt) %{_datadir}/%{name}/texmaker_pt.qm
%lang(ru) %{_datadir}/%{name}/texmaker_ru.qm
%lang(se) %{_datadir}/%{name}/texmaker_se.qm
%lang(sr) %{_datadir}/%{name}/texmaker_sr.qm
%lang(uk) %{_datadir}/%{name}/texmaker_uk.qm
%lang(zh_CN) %{_datadir}/%{name}/texmaker_zh_CN.qm
%lang(zh_TW) %{_datadir}/%{name}/texmaker_zh_TW.qm
%{_datadir}/%{name}/*.html
%{_datadir}/%{name}/*.png
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
