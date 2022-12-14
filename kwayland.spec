#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : kwayland
Version  : 5.101.0
Release  : 60
URL      : https://download.kde.org/stable/frameworks/5.101/kwayland-5.101.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.101/kwayland-5.101.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.101/kwayland-5.101.0.tar.xz.sig
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
BuildRequires : extra-cmake-modules qtwayland-dev
BuildRequires : extra-cmake-modules wayland
BuildRequires : extra-cmake-modules-data
BuildRequires : pkg-config
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : plasma-wayland-protocols-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-staticdev
BuildRequires : weston-dev weston

%description
# KWayland
KWayland is a Qt-style API to interact with the wayland-client and wayland-server API.

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
%setup -q -n kwayland-5.101.0
cd %{_builddir}/kwayland-5.101.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1671044463
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
export SOURCE_DATE_EPOCH=1671044463
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
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/org-kde-kf5-kwayland-testserver

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/kwayland.categories
/usr/share/qlogging-categories5/kwayland.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/KWayland/KWayland/Client/appmenu.h
/usr/include/KF5/KWayland/KWayland/Client/blur.h
/usr/include/KF5/KWayland/KWayland/Client/buffer.h
/usr/include/KF5/KWayland/KWayland/Client/compositor.h
/usr/include/KF5/KWayland/KWayland/Client/connection_thread.h
/usr/include/KF5/KWayland/KWayland/Client/contrast.h
/usr/include/KF5/KWayland/KWayland/Client/datadevice.h
/usr/include/KF5/KWayland/KWayland/Client/datadevicemanager.h
/usr/include/KF5/KWayland/KWayland/Client/dataoffer.h
/usr/include/KF5/KWayland/KWayland/Client/datasource.h
/usr/include/KF5/KWayland/KWayland/Client/dpms.h
/usr/include/KF5/KWayland/KWayland/Client/event_queue.h
/usr/include/KF5/KWayland/KWayland/Client/fakeinput.h
/usr/include/KF5/KWayland/KWayland/Client/fullscreen_shell.h
/usr/include/KF5/KWayland/KWayland/Client/idle.h
/usr/include/KF5/KWayland/KWayland/Client/idleinhibit.h
/usr/include/KF5/KWayland/KWayland/Client/keyboard.h
/usr/include/KF5/KWayland/KWayland/Client/keystate.h
/usr/include/KF5/KWayland/KWayland/Client/kwaylandclient_export.h
/usr/include/KF5/KWayland/KWayland/Client/output.h
/usr/include/KF5/KWayland/KWayland/Client/outputconfiguration.h
/usr/include/KF5/KWayland/KWayland/Client/outputdevice.h
/usr/include/KF5/KWayland/KWayland/Client/outputmanagement.h
/usr/include/KF5/KWayland/KWayland/Client/plasmashell.h
/usr/include/KF5/KWayland/KWayland/Client/plasmavirtualdesktop.h
/usr/include/KF5/KWayland/KWayland/Client/plasmawindowmanagement.h
/usr/include/KF5/KWayland/KWayland/Client/plasmawindowmodel.h
/usr/include/KF5/KWayland/KWayland/Client/pointer.h
/usr/include/KF5/KWayland/KWayland/Client/pointerconstraints.h
/usr/include/KF5/KWayland/KWayland/Client/pointergestures.h
/usr/include/KF5/KWayland/KWayland/Client/region.h
/usr/include/KF5/KWayland/KWayland/Client/registry.h
/usr/include/KF5/KWayland/KWayland/Client/relativepointer.h
/usr/include/KF5/KWayland/KWayland/Client/remote_access.h
/usr/include/KF5/KWayland/KWayland/Client/seat.h
/usr/include/KF5/KWayland/KWayland/Client/server_decoration.h
/usr/include/KF5/KWayland/KWayland/Client/server_decoration_palette.h
/usr/include/KF5/KWayland/KWayland/Client/shadow.h
/usr/include/KF5/KWayland/KWayland/Client/shell.h
/usr/include/KF5/KWayland/KWayland/Client/shm_pool.h
/usr/include/KF5/KWayland/KWayland/Client/slide.h
/usr/include/KF5/KWayland/KWayland/Client/subcompositor.h
/usr/include/KF5/KWayland/KWayland/Client/subsurface.h
/usr/include/KF5/KWayland/KWayland/Client/surface.h
/usr/include/KF5/KWayland/KWayland/Client/textinput.h
/usr/include/KF5/KWayland/KWayland/Client/touch.h
/usr/include/KF5/KWayland/KWayland/Client/xdgdecoration.h
/usr/include/KF5/KWayland/KWayland/Client/xdgforeign.h
/usr/include/KF5/KWayland/KWayland/Client/xdgoutput.h
/usr/include/KF5/KWayland/KWayland/Client/xdgshell.h
/usr/include/KF5/KWayland/Server/appmenu_interface.h
/usr/include/KF5/KWayland/Server/blur_interface.h
/usr/include/KF5/KWayland/Server/buffer_interface.h
/usr/include/KF5/KWayland/Server/clientconnection.h
/usr/include/KF5/KWayland/Server/compositor_interface.h
/usr/include/KF5/KWayland/Server/contrast_interface.h
/usr/include/KF5/KWayland/Server/datadevice_interface.h
/usr/include/KF5/KWayland/Server/datadevicemanager_interface.h
/usr/include/KF5/KWayland/Server/dataoffer_interface.h
/usr/include/KF5/KWayland/Server/datasource_interface.h
/usr/include/KF5/KWayland/Server/display.h
/usr/include/KF5/KWayland/Server/dpms_interface.h
/usr/include/KF5/KWayland/Server/eglstream_controller_interface.h
/usr/include/KF5/KWayland/Server/fakeinput_interface.h
/usr/include/KF5/KWayland/Server/filtered_display.h
/usr/include/KF5/KWayland/Server/global.h
/usr/include/KF5/KWayland/Server/idle_interface.h
/usr/include/KF5/KWayland/Server/idleinhibit_interface.h
/usr/include/KF5/KWayland/Server/keyboard_interface.h
/usr/include/KF5/KWayland/Server/keystate_interface.h
/usr/include/KF5/KWayland/Server/kwaylandserver_export.h
/usr/include/KF5/KWayland/Server/linuxdmabuf_v1_interface.h
/usr/include/KF5/KWayland/Server/output_interface.h
/usr/include/KF5/KWayland/Server/outputchangeset.h
/usr/include/KF5/KWayland/Server/outputconfiguration_interface.h
/usr/include/KF5/KWayland/Server/outputdevice_interface.h
/usr/include/KF5/KWayland/Server/outputmanagement_interface.h
/usr/include/KF5/KWayland/Server/plasmashell_interface.h
/usr/include/KF5/KWayland/Server/plasmavirtualdesktop_interface.h
/usr/include/KF5/KWayland/Server/plasmawindowmanagement_interface.h
/usr/include/KF5/KWayland/Server/pointer_interface.h
/usr/include/KF5/KWayland/Server/pointerconstraints_interface.h
/usr/include/KF5/KWayland/Server/pointergestures_interface.h
/usr/include/KF5/KWayland/Server/qtsurfaceextension_interface.h
/usr/include/KF5/KWayland/Server/region_interface.h
/usr/include/KF5/KWayland/Server/relativepointer_interface.h
/usr/include/KF5/KWayland/Server/remote_access_interface.h
/usr/include/KF5/KWayland/Server/resource.h
/usr/include/KF5/KWayland/Server/seat_interface.h
/usr/include/KF5/KWayland/Server/server_decoration_interface.h
/usr/include/KF5/KWayland/Server/server_decoration_palette_interface.h
/usr/include/KF5/KWayland/Server/shadow_interface.h
/usr/include/KF5/KWayland/Server/shell_interface.h
/usr/include/KF5/KWayland/Server/slide_interface.h
/usr/include/KF5/KWayland/Server/subcompositor_interface.h
/usr/include/KF5/KWayland/Server/surface_interface.h
/usr/include/KF5/KWayland/Server/tablet_interface.h
/usr/include/KF5/KWayland/Server/textinput_interface.h
/usr/include/KF5/KWayland/Server/touch_interface.h
/usr/include/KF5/KWayland/Server/xdgdecoration_interface.h
/usr/include/KF5/KWayland/Server/xdgforeign_interface.h
/usr/include/KF5/KWayland/Server/xdgoutput_interface.h
/usr/include/KF5/KWayland/Server/xdgshell_interface.h
/usr/include/KF5/KWayland/kwayland_version.h
/usr/lib64/cmake/KF5Wayland/KF5WaylandConfig.cmake
/usr/lib64/cmake/KF5Wayland/KF5WaylandConfigVersion.cmake
/usr/lib64/cmake/KF5Wayland/KF5WaylandTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Wayland/KF5WaylandTargets.cmake
/usr/lib64/libKF5WaylandClient.so
/usr/lib64/libKF5WaylandServer.so
/usr/lib64/pkgconfig/KF5WaylandClient.pc
/usr/lib64/qt5/mkspecs/modules/qt_KWaylandClient.pri
/usr/lib64/qt5/mkspecs/modules/qt_KWaylandServer.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5WaylandClient.so.5
/usr/lib64/libKF5WaylandClient.so.5.101.0
/usr/lib64/libKF5WaylandServer.so.5
/usr/lib64/libKF5WaylandServer.so.5.101.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kwayland/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kwayland/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/kwayland/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kwayland/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kwayland/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kwayland/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/kwayland/e458941548e0864907e654fa2e192844ae90fc32
