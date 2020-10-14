#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : zeroconf-ioslave
Version  : 20.08.2
Release  : 22
URL      : https://download.kde.org/stable/release-service/20.08.2/src/zeroconf-ioslave-20.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.08.2/src/zeroconf-ioslave-20.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.08.2/src/zeroconf-ioslave-20.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1
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
%setup -q -n zeroconf-ioslave-20.08.2
cd %{_builddir}/zeroconf-ioslave-20.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602652608
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1602652608
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zeroconf-ioslave
cp %{_builddir}/zeroconf-ioslave-20.08.2/COPYING %{buildroot}/usr/share/package-licenses/zeroconf-ioslave/3860f7708aae6a8ddfe8483263b2a5f29b83c975
cp %{_builddir}/zeroconf-ioslave-20.08.2/COPYING.DOC %{buildroot}/usr/share/package-licenses/zeroconf-ioslave/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
cp %{_builddir}/zeroconf-ioslave-20.08.2/COPYING.LIB %{buildroot}/usr/share/package-licenses/zeroconf-ioslave/9a1929f4700d2407c70b507b3b2aaf6226a9543c
pushd clr-build
%make_install
popd
%find_lang kio5_zeroconf

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/dbus-1/interfaces/org.kde.kdnssd.xml
/usr/share/kservices5/kded/dnssdwatcher.desktop
/usr/share/metainfo/org.kde.zeroconf-ioslave.metainfo.xml
/usr/share/remoteview/zeroconf.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kded_dnssdwatcher.so
/usr/lib64/qt5/plugins/kf5/kio/zeroconf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zeroconf-ioslave/3860f7708aae6a8ddfe8483263b2a5f29b83c975
/usr/share/package-licenses/zeroconf-ioslave/9a1929f4700d2407c70b507b3b2aaf6226a9543c
/usr/share/package-licenses/zeroconf-ioslave/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files locales -f kio5_zeroconf.lang
%defattr(-,root,root,-)

