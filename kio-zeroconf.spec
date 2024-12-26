#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: 5424026
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : kio-zeroconf
Version  : 24.12.0
Release  : 55
URL      : https://download.kde.org/stable/release-service/24.12.0/src/kio-zeroconf-24.12.0.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.12.0/src/kio-zeroconf-24.12.0.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.12.0/src/kio-zeroconf-24.12.0.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: kio-zeroconf-data = %{version}-%{release}
Requires: kio-zeroconf-lib = %{version}-%{release}
Requires: kio-zeroconf-license = %{version}-%{release}
Requires: kio-zeroconf-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kdnssd-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%package data
Summary: data components for the kio-zeroconf package.
Group: Data

%description data
data components for the kio-zeroconf package.


%package lib
Summary: lib components for the kio-zeroconf package.
Group: Libraries
Requires: kio-zeroconf-data = %{version}-%{release}
Requires: kio-zeroconf-license = %{version}-%{release}

%description lib
lib components for the kio-zeroconf package.


%package license
Summary: license components for the kio-zeroconf package.
Group: Default

%description license
license components for the kio-zeroconf package.


%package locales
Summary: locales components for the kio-zeroconf package.
Group: Default

%description locales
locales components for the kio-zeroconf package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n kio-zeroconf-24.12.0
cd %{_builddir}/kio-zeroconf-24.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1735187523
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
%cmake .. -DQT_MAJOR_VERSION=6  -G 'Unix Makefiles'
make  %{?_smp_mflags}
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
export SOURCE_DATE_EPOCH=1735187523
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kio-zeroconf
cp %{_builddir}/kio-zeroconf-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kio-zeroconf/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kio-zeroconf-%{version}/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/kio-zeroconf/a4c60b3fefda228cd7439d3565df043192fef137 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kio5_zeroconf

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.kdnssd.xml
/usr/share/metainfo/org.kde.kio_zeroconf.metainfo.xml
/usr/share/remoteview/zeroconf.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/plugins/kf6/kded/dnssdwatcher.so
/usr/lib64/qt6/plugins/kf6/kio/zeroconf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kio-zeroconf/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kio-zeroconf/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f kio5_zeroconf.lang
%defattr(-,root,root,-)

