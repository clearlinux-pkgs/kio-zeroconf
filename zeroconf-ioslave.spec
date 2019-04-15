#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : zeroconf-ioslave
Version  : 18.12.3
Release  : 4
URL      : https://download.kde.org/stable/applications/18.12.3/src/zeroconf-ioslave-18.12.3.tar.xz
Source0  : https://download.kde.org/stable/applications/18.12.3/src/zeroconf-ioslave-18.12.3.tar.xz
Source99 : https://download.kde.org/stable/applications/18.12.3/src/zeroconf-ioslave-18.12.3.tar.xz.sig
Summary  : Network Monitor for DNS-SD services (Zeroconf)
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0 LGPL-2.1
Requires: zeroconf-ioslave-data = %{version}-%{release}
Requires: zeroconf-ioslave-lib = %{version}-%{release}
Requires: zeroconf-ioslave-license = %{version}-%{release}
Requires: zeroconf-ioslave-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
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
%setup -q -n zeroconf-ioslave-18.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555343132
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555343132
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/zeroconf-ioslave
cp COPYING %{buildroot}/usr/share/package-licenses/zeroconf-ioslave/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/zeroconf-ioslave/COPYING.DOC
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/zeroconf-ioslave/COPYING.LIB
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
/usr/share/remoteview/zeroconf.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kded_dnssdwatcher.so
/usr/lib64/qt5/plugins/kf5/kio/zeroconf.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/zeroconf-ioslave/COPYING
/usr/share/package-licenses/zeroconf-ioslave/COPYING.DOC
/usr/share/package-licenses/zeroconf-ioslave/COPYING.LIB

%files locales -f kio5_zeroconf.lang
%defattr(-,root,root,-)

