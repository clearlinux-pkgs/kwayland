#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v10
# autospec commit: 5905be9
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : kwayland
Version  : 6.0.4
Release  : 83
URL      : https://download.kde.org/stable/plasma/6.0.4/kwayland-6.0.4.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.4/kwayland-6.0.4.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.4/kwayland-6.0.4.tar.xz.sig
Source2  : D7574483BB57B18D.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kwayland-data = %{version}-%{release}
Requires: kwayland-lib = %{version}-%{release}
Requires: kwayland-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : extra-cmake-modules pkgconfig(wayland-client)
BuildRequires : extra-cmake-modules wayland
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qt6base-dev
BuildRequires : qt6wayland-dev
BuildRequires : qtbase-staticdev
BuildRequires : wayland-protocols-dev plasma-wayland-protocols-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# KWayland
KWayland is a Qt-style API to interact with the wayland-client API.
## Introduction

%package data
Summary: data components for the kwayland package.
Group: Data

%description data
data components for the kwayland package.


%package dev
Summary: dev components for the kwayland package.
Group: Development
Requires: kwayland-lib = %{version}-%{release}
Requires: kwayland-data = %{version}-%{release}
Provides: kwayland-devel = %{version}-%{release}
Requires: kwayland = %{version}-%{release}

%description dev
dev components for the kwayland package.


%package lib
Summary: lib components for the kwayland package.
Group: Libraries
Requires: kwayland-data = %{version}-%{release}
Requires: kwayland-license = %{version}-%{release}

%description lib
lib components for the kwayland package.


%package license
Summary: license components for the kwayland package.
Group: Default

%description license
license components for the kwayland package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) D7574483BB57B18D' gpg.status
%setup -q -n kwayland-6.0.4
cd %{_builddir}/kwayland-6.0.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1713294448
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
%cmake ..
make  %{?_smp_mflags}
popd
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
%cmake ..
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
export SOURCE_DATE_EPOCH=1713294448
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kwayland
cp %{_builddir}/kwayland-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kwayland/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kwayland-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kwayland/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kwayland-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kwayland/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kwayland-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kwayland/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/kwayland-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kwayland/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kwayland-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kwayland-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kwayland/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kwayland-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kwayland/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
export GOAMD64=v2
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/kwayland.categories
/usr/share/qlogging-categories6/kwayland.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KWayland/KWayland/Client/appmenu.h
/usr/include/KWayland/KWayland/Client/blur.h
/usr/include/KWayland/KWayland/Client/buffer.h
/usr/include/KWayland/KWayland/Client/compositor.h
/usr/include/KWayland/KWayland/Client/connection_thread.h
/usr/include/KWayland/KWayland/Client/contrast.h
/usr/include/KWayland/KWayland/Client/datadevice.h
/usr/include/KWayland/KWayland/Client/datadevicemanager.h
/usr/include/KWayland/KWayland/Client/dataoffer.h
/usr/include/KWayland/KWayland/Client/datasource.h
/usr/include/KWayland/KWayland/Client/dpms.h
/usr/include/KWayland/KWayland/Client/event_queue.h
/usr/include/KWayland/KWayland/Client/fakeinput.h
/usr/include/KWayland/KWayland/Client/idleinhibit.h
/usr/include/KWayland/KWayland/Client/keyboard.h
/usr/include/KWayland/KWayland/Client/kwaylandclient_export.h
/usr/include/KWayland/KWayland/Client/output.h
/usr/include/KWayland/KWayland/Client/plasmashell.h
/usr/include/KWayland/KWayland/Client/plasmavirtualdesktop.h
/usr/include/KWayland/KWayland/Client/plasmawindowmanagement.h
/usr/include/KWayland/KWayland/Client/plasmawindowmodel.h
/usr/include/KWayland/KWayland/Client/pointer.h
/usr/include/KWayland/KWayland/Client/pointerconstraints.h
/usr/include/KWayland/KWayland/Client/pointergestures.h
/usr/include/KWayland/KWayland/Client/region.h
/usr/include/KWayland/KWayland/Client/registry.h
/usr/include/KWayland/KWayland/Client/relativepointer.h
/usr/include/KWayland/KWayland/Client/seat.h
/usr/include/KWayland/KWayland/Client/shadow.h
/usr/include/KWayland/KWayland/Client/shell.h
/usr/include/KWayland/KWayland/Client/shm_pool.h
/usr/include/KWayland/KWayland/Client/slide.h
/usr/include/KWayland/KWayland/Client/subcompositor.h
/usr/include/KWayland/KWayland/Client/subsurface.h
/usr/include/KWayland/KWayland/Client/surface.h
/usr/include/KWayland/KWayland/Client/textinput.h
/usr/include/KWayland/KWayland/Client/touch.h
/usr/include/KWayland/KWayland/Client/xdgdecoration.h
/usr/include/KWayland/KWayland/Client/xdgforeign.h
/usr/include/KWayland/KWayland/Client/xdgoutput.h
/usr/include/KWayland/KWayland/Client/xdgshell.h
/usr/include/KWayland/kwayland_version.h
/usr/lib64/cmake/KWayland/KWaylandConfig.cmake
/usr/lib64/cmake/KWayland/KWaylandConfigVersion.cmake
/usr/lib64/cmake/KWayland/KWaylandTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KWayland/KWaylandTargets.cmake
/usr/lib64/libKWaylandClient.so
/usr/lib64/pkgconfig/KWaylandClient.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKWaylandClient.so.6.0.4
/usr/lib64/libKWaylandClient.so.6
/usr/lib64/libKWaylandClient.so.6.0.4

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwayland/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kwayland/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kwayland/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kwayland/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kwayland/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kwayland/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kwayland/e458941548e0864907e654fa2e192844ae90fc32
