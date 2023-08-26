#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kolf
Version  : 23.08.0
Release  : 55
URL      : https://download.kde.org/stable/release-service/23.08.0/src/kolf-23.08.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.08.0/src/kolf-23.08.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.08.0/src/kolf-23.08.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0 LGPL-2.0 Zlib
Requires: kolf-bin = %{version}-%{release}
Requires: kolf-data = %{version}-%{release}
Requires: kolf-license = %{version}-%{release}
Requires: kolf-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n kolf-23.08.0
cd %{_builddir}/kolf-23.08.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693011940
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1693011940
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kolf
cp %{_builddir}/kolf-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kolf/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kolf-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kolf/88d0ee521bcbddeff0f97979d84760ef8d1529cc || :
cp %{_builddir}/kolf-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kolf/1bd373e4851a93027ba70064bd7dbdc6827147e1 || :
cp %{_builddir}/kolf-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/kolf/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
cp %{_builddir}/kolf-%{version}/external/COPYING %{buildroot}/usr/share/package-licenses/kolf/2968029980d16f3e4c5ca945099a747725a5eacb || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang kolf
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kolf
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
/usr/share/doc/HTML/ca/kolf/index.cache.bz2
/usr/share/doc/HTML/ca/kolf/index.docbook
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
/usr/share/doc/HTML/gl/kolf/index.cache.bz2
/usr/share/doc/HTML/gl/kolf/index.docbook
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kolf/1bd373e4851a93027ba70064bd7dbdc6827147e1
/usr/share/package-licenses/kolf/2968029980d16f3e4c5ca945099a747725a5eacb
/usr/share/package-licenses/kolf/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/kolf/88d0ee521bcbddeff0f97979d84760ef8d1529cc
/usr/share/package-licenses/kolf/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f kolf.lang
%defattr(-,root,root,-)

