#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : kolf
Version  : 19.08.2
Release  : 12
URL      : https://download.kde.org/stable/applications/19.08.2/src/kolf-19.08.2.tar.xz
Source0  : https://download.kde.org/stable/applications/19.08.2/src/kolf-19.08.2.tar.xz
Source1 : https://download.kde.org/stable/applications/19.08.2/src/kolf-19.08.2.tar.xz.sig
Summary  : A miniature golf game with 2d top-down view
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.0 Zlib
Requires: kolf-bin = %{version}-%{release}
Requires: kolf-data = %{version}-%{release}
Requires: kolf-lib = %{version}-%{release}
Requires: kolf-license = %{version}-%{release}
Requires: kolf-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
This directory contains code from Project Tagaro, which has been copied into
the source tree of Kolf to ease porting to KGameRenderer, while Tagaro is not
stable.

%package bin
Summary: bin components for the kolf package.
Group: Binaries
Requires: kolf-data = %{version}-%{release}
Requires: kolf-license = %{version}-%{release}

%description bin
bin components for the kolf package.


%package data
Summary: data components for the kolf package.
Group: Data

%description data
data components for the kolf package.


%package doc
Summary: doc components for the kolf package.
Group: Documentation

%description doc
doc components for the kolf package.


%package lib
Summary: lib components for the kolf package.
Group: Libraries
Requires: kolf-data = %{version}-%{release}
Requires: kolf-license = %{version}-%{release}

%description lib
lib components for the kolf package.


%package license
Summary: license components for the kolf package.
Group: Default

%description license
license components for the kolf package.


%package locales
Summary: locales components for the kolf package.
Group: Default

%description locales
locales components for the kolf package.


%prep
%setup -q -n kolf-19.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570766210
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1570766210
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kolf
cp COPYING %{buildroot}/usr/share/package-licenses/kolf/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/kolf/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/kolf/COPYING.LIB
cp external/COPYING %{buildroot}/usr/share/package-licenses/kolf/external_COPYING
pushd clr-build
%make_install
popd
%find_lang kolf

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kolf

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.kolf.desktop
/usr/share/icons/hicolor/128x128/apps/kolf.png
/usr/share/icons/hicolor/16x16/apps/kolf.png
/usr/share/icons/hicolor/22x22/apps/kolf.png
/usr/share/icons/hicolor/32x32/apps/kolf.png
/usr/share/icons/hicolor/48x48/apps/kolf.png
/usr/share/icons/hicolor/64x64/apps/kolf.png
/usr/share/icons/hicolor/scalable/apps/kolf.svgz
/usr/share/kolf/courses/Classic.kolf
/usr/share/kolf/courses/Easy.kolf
/usr/share/kolf/courses/Hard.kolf
/usr/share/kolf/courses/Impossible
/usr/share/kolf/courses/Medium.kolf
/usr/share/kolf/courses/Practice
/usr/share/kolf/courses/ReallyEasy
/usr/share/kolf/courses/USApro
/usr/share/kolf/intro
/usr/share/kolf/pics/default_theme.svgz
/usr/share/kolf/sounds/blackhole.wav
/usr/share/kolf/sounds/blackholeeject.wav
/usr/share/kolf/sounds/blackholeputin.wav
/usr/share/kolf/sounds/bumper.wav
/usr/share/kolf/sounds/hit.wav
/usr/share/kolf/sounds/holed.wav
/usr/share/kolf/sounds/holeinone.wav
/usr/share/kolf/sounds/puddle.wav
/usr/share/kolf/sounds/wall.wav
/usr/share/kolf/sounds/woohoo.wav
/usr/share/kolf/tutorial.kolf
/usr/share/kolf/tutorial.kolfgame
/usr/share/kxmlgui5/kolf/kolfui.rc
/usr/share/metainfo/org.kde.kolf.appdata.xml

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/de/kolf/index.cache.bz2
/usr/share/doc/HTML/de/kolf/index.docbook
/usr/share/doc/HTML/en/kolf/index.cache.bz2
/usr/share/doc/HTML/en/kolf/index.docbook
/usr/share/doc/HTML/es/kolf/index.cache.bz2
/usr/share/doc/HTML/es/kolf/index.docbook
/usr/share/doc/HTML/et/kolf/index.cache.bz2
/usr/share/doc/HTML/et/kolf/index.docbook
/usr/share/doc/HTML/fr/kolf/index.cache.bz2
/usr/share/doc/HTML/fr/kolf/index.docbook
/usr/share/doc/HTML/it/kolf/index.cache.bz2
/usr/share/doc/HTML/it/kolf/index.docbook
/usr/share/doc/HTML/nl/kolf/index.cache.bz2
/usr/share/doc/HTML/nl/kolf/index.docbook
/usr/share/doc/HTML/pt/kolf/index.cache.bz2
/usr/share/doc/HTML/pt/kolf/index.docbook
/usr/share/doc/HTML/pt_BR/kolf/index.cache.bz2
/usr/share/doc/HTML/pt_BR/kolf/index.docbook
/usr/share/doc/HTML/ru/kolf/index.cache.bz2
/usr/share/doc/HTML/ru/kolf/index.docbook
/usr/share/doc/HTML/sv/kolf/index.cache.bz2
/usr/share/doc/HTML/sv/kolf/index.docbook
/usr/share/doc/HTML/uk/kolf/index.cache.bz2
/usr/share/doc/HTML/uk/kolf/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkolfprivate.so.5.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kolf/COPYING
/usr/share/package-licenses/kolf/COPYING.DOC
/usr/share/package-licenses/kolf/COPYING.LIB
/usr/share/package-licenses/kolf/external_COPYING

%files locales -f kolf.lang
%defattr(-,root,root,-)

