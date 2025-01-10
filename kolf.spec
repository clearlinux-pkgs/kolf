#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kolf
Version  : 24.12.1
Release  : 75
URL      : https://download.kde.org/stable/release-service/24.12.1/src/kolf-24.12.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.1/src/kolf-24.12.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.1/src/kolf-24.12.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This directory contains a source snapshot of Box2D, taken from revision 141 of https://web.archive.org/web/20110429162509/http://box2d.googlecode.com/svn/trunk/Box2D/Box2D

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kolf-24.12.1
cd %{_builddir}/kolf-24.12.1
pushd ..
cp -a kolf-24.12.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736529346
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1736529346
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kolf
cp %{_builddir}/kolf-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/kolf/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/kolf-%{version}/COPYING %{buildroot}/usr/share/package-licenses/kolf/88d0ee521bcbddeff0f97979d84760ef8d1529cc || :
cp %{_builddir}/kolf-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/kolf/1bd373e4851a93027ba70064bd7dbdc6827147e1 || :
cp %{_builddir}/kolf-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/kolf/ba8966e2473a9969bdcab3dc82274c817cfd98a1 || :
cp %{_builddir}/kolf-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kolf/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kolf-%{version}/src/3rdparty/COPYING %{buildroot}/usr/share/package-licenses/kolf/2968029980d16f3e4c5ca945099a747725a5eacb || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
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
/usr/share/kolf/themes/default.svgz
/usr/share/kolf/tutorial.kolf
/usr/share/kolf/tutorial.kolfgame
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
/usr/share/doc/HTML/sl/kolf/index.cache.bz2
/usr/share/doc/HTML/sl/kolf/index.docbook
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
/usr/share/package-licenses/kolf/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kolf/ba8966e2473a9969bdcab3dc82274c817cfd98a1

%files locales -f kolf.lang
%defattr(-,root,root,-)

