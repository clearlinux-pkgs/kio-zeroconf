#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : zeroconf-ioslave
Version  : 22.04.3
Release  : 40
URL      : https://download.kde.org/stable/release-service/22.04.3/src/zeroconf-ioslave-22.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.04.3/src/zeroconf-ioslave-22.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.04.3/src/zeroconf-ioslave-22.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0
Requires: zeroconf-ioslave-data = %{version}-%{release}
Requires: zeroconf-ioslave-lib = %{version}-%{release}
Requires: zeroconf-ioslave-license = %{version}-%{release}
Requires: zeroconf-ioslave-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdnssd-dev
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the zeroconf-ioslave package.
Group: Data

%description data
data components for the zeroconf-ioslave package.


%package lib
Summary: lib components for the zeroconf-ioslave package.
Group: Libraries
Requires: zeroconf-ioslave-data = %{version}-%{release}
Requires: zeroconf-ioslave-license = %{version}-%{release}

%description lib
lib components for the zeroconf-ioslave package.


%package license
Summary: license components for the zeroconf-ioslave package.
Group: Default

%description license
license components for the zeroconf-ioslave package.


%package locales
Summary: locales components for the zeroconf-ioslave package.
Group: Default

%description locales
locales components for the zeroconf-ioslave package.


%prep
%setup -q -n zeroconf-ioslave-22.04.3
cd %{_builddir}/zeroconf-ioslave-22.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657552363
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1657552363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zeroconf-ioslave
cp %{_builddir}/zeroconf-ioslave-22.04.3/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/zeroconf-ioslave/3e8971c6c5f16674958913a94a36b1ea7a00ac46
cp %{_builddir}/zeroconf-ioslave-22.04.3/LICENSES/LGPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/zeroconf-ioslave/a4c60b3fefda228cd7439d3565df043192fef137
pushd clr-build
%make_install
popd
%find_lang kio5_zeroconf

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.kdnssd.xml
/usr/share/metainfo/org.kde.zeroconf-ioslave.metainfo.xml
/usr/share/remoteview/zeroconf.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/kded/dnssdwatcher.so
/usr/lib64/qt5/plugins/kf5/kio/zeroconf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zeroconf-ioslave/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/zeroconf-ioslave/a4c60b3fefda228cd7439d3565df043192fef137

%files locales -f kio5_zeroconf.lang
%defattr(-,root,root,-)

