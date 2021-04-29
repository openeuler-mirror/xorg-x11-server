%undefine _hardened_build
%undefine _strict_symbol_defs_build

#global gitdate 20161026
%global stable_abi 1

%global ansic_major 0
%global ansic_minor 4
%global videodrv_major 24
%global videodrv_minor 1
%global xinput_major 24
%global xinput_minor 1
%global extension_major 10
%global extension_minor 0
%global pkgname xorg-server

Name:           xorg-x11-server
Version:        1.20.8
Release:        5
Summary:        X.Org X11 X server
License:        MIT and GPLv2
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/xserver/xorg-server-%{version}.tar.bz2
Source1:        gitignore
Source4:        10-quirks.conf
Source10:       xserver.pamd

# "useful" xvfb-run script
Source20:       http://svn.exactcode.de/t2/trunk/package/xorg/xorg-server/xvfb-run.sh

# for requires generation in drivers
Source30:       xserver-sdk-abi-requires.release
Source31:       xserver-sdk-abi-requires.git

# maintainer convenience script
Source40: driver-abi-rebuild.sh
 
# From Debian use intel ddx driver only for gen4 and older chipsets
Patch0000: 06_use-intel-only-on-pre-gen4.diff
# Default to xf86-video-modesetting on GeForce 8 and newer
Patch0001: 0001-xfree86-use-modesetting-driver-by-default-on-GeForce.patch
 
# Default to va_gl on intel i965 as we use the modesetting drv there
# va_gl should probably just be the default everywhere ?
Patch0002: 0001-xf86-dri2-Use-va_gl-as-vdpau_driver-for-Intel-i965-G.patch
 
# Submitted upstream, but not going anywhere
Patch0003: 0001-autobind-GPUs-to-the-screen.patch
 
# because the display-managers are not ready yet, do not upstream
Patch0004: 0001-Fedora-hack-Make-the-suid-root-wrapper-always-start-.patch
 
# Backports from current stable "server-1.20-branch":
# Backports from "master" upstream:
# Backported Xwayland randr resolution change emulation support
Patch0005: 0001-dix-Add-GetCurrentClient-helper.patch
Patch0006: 0002-xwayland-Add-wp_viewport-wayland-extension-support.patch
Patch0007: 0003-xwayland-Use-buffer_damage-instead-of-surface-damage.patch
Patch0008: 0004-xwayland-Add-fake-output-modes-to-xrandr-output-mode.patch
Patch0009: 0005-xwayland-Use-RandR-1.2-interface-rev-2.patch
Patch0010: 0006-xwayland-Add-per-client-private-data.patch
Patch0011: 0007-xwayland-Add-support-for-storing-per-client-per-outp.patch
Patch0012: 0008-xwayland-Add-support-for-randr-resolution-change-emu.patch
Patch0013: 0009-xwayland-Add-xwlRRModeToDisplayMode-helper-function.patch
Patch0014: 0010-xwayland-Add-xwlVidModeGetCurrentRRMode-helper-to-th.patch
Patch0015: 0011-xwayland-Add-vidmode-mode-changing-emulation-support.patch
Patch0016: 0012-xwayland-xwl_window_should_enable_viewport-Add-extra.patch
Patch0017: 0013-xwayland-Set-_XWAYLAND_RANDR_EMU_MONITOR_RECTS-prope.patch
Patch0018: 0014-xwayland-Cache-client-id-for-the-window-manager-clie.patch
Patch0019: 0015-xwayland-Reuse-viewport-instead-of-recreating.patch
Patch0020: 0016-xwayland-Recurse-on-finding-the-none-wm-owner.patch
Patch0021: 0017-xwayland-Make-window_get_none_wm_owner-return-a-Wind.patch
Patch0022: 0018-xwayland-Check-emulation-on-client-toplevel-resize.patch
Patch0023: 0019-xwayland-Also-check-resolution-change-emulation-when.patch
Patch0024: 0020-xwayland-Also-hook-screen-s-MoveWindow-method.patch
Patch0025: 0021-xwayland-Fix-emulated-modes-not-being-removed-when-s.patch
Patch0026: 0022-xwayland-Call-xwl_window_check_resolution_change_emu.patch
Patch0027: 0023-xwayland-Fix-setting-of-_XWAYLAND_RANDR_EMU_MONITOR_.patch
Patch0028: 0024-xwayland-Remove-unnecessary-xwl_window_is_toplevel-c.patch
Patch0029: xorg-s11-server-CVE-2018-20839.patch
Patch0030: CVE-2020-14346.patch
Patch0031: CVE-2020-14361.patch
Patch0032: CVE-2020-14362.patch
Patch0033: CVE-2020-14345.patch
Patch0034: backport-CVE-2020-25712.patch
Patch0035: backport-CVE-2020-14360.patch
Patch0036: backport-CVE-2020-14347.patch

BuildRequires:  audit-libs-devel autoconf automake bison dbus-devel flex flex-devel git
BuildRequires:  systemtap-sdt-devel libtool pkgconfig 
BuildRequires:  xorg-x11-font-utils libepoxy-devel systemd-devel 
BuildRequires:  libXfont2-devel libXau-devel libxkbfile-devel libXres-devel
BuildRequires:  libfontenc-devel libXtst-devel libXdmcp-devel libX11-devel libXext-devel
BuildRequires:  libXinerama-devel libXi-devel libXt-devel libdmx-devel libXmu-devel libXrender-devel
BuildRequires:  libXi-devel libXpm-devel libXaw-devel libXfixes-devel libepoxy-devel libXv-devel 
BuildRequires:  wayland-devel wayland-protocols-devel egl-wayland-devel openssl-devel kernel-headers
BuildRequires:  mesa-libEGL-devel mesa-libgbm-devel libudev-devel xcb-util-devel 
BuildRequires:  xcb-util-image-devel xcb-util-wm-devel xcb-util-keysyms-devel xcb-util-renderutil-devel 
BuildRequires:  xorg-x11-xtrans-devel >= 1.3.2 xorg-x11-util-macros >= 1.17 xorg-x11-proto-devel >= 7.7  
BuildRequires:  xorg-x11-font-utils >= 7.2 libselinux-devel >= 2.0.86 wayland-devel >= 1.3.0
BuildRequires:  libxshmfence-devel >= 1.1 pixman-devel >= 0.30.0 libdrm-devel >= 2.4.0  
BuildRequires:  mesa-libGL-devel >= 9.2 libpciaccess-devel >= 0.13.1

%ifarch aarch64 %{arm} x86_64
BuildRequires:  libunwind-devel
%endif

Requires:       pixman >= 0.30.0 xkeyboard-config xkbcomp
Requires:       system-setup-keyboard xorg-x11-drv-libinput libEGL
Requires:       xorg-x11-xauth

Obsoletes:      %{name}-common < %{version}-%{release} %{name}-Xorg < %{version}-%{release} %{name}-Xnest < %{version}-%{release} %{name}-source %{name}-Xdmx < %{version}-%{release} %{name}-Xvfb < %{version}-%{release} %{name}-Xwayland < %{version}-%{release}
Provides:       %{name}-common = %{version}-%{release} %{name}-Xorg = %{version}-%{release} %{name}-Xorg%{?_isa} = %{version}-%{release} %{name}-Xnest = %{version}-%{release} %{name}-source = %{version}-%{release} %{name}-Xdmx = %{version}-%{release} %{name}-Xvfb = %{version}-%{release} %{name}-Xwayland = %{version}-%{release} %{name}-Xwayland%{?_isa} = %{version}-%{release}

Provides:       Xorg = %{version}-%{release}
Obsoletes: 		Xorg < %{version}-%{release}
Provides:       Xserver = %{version}-%{release}
Obsoletes: 		Xserver < %{version}-%{release}
Provides:       xorg-x11-server-wrapper = %{version}-%{release}
Obsoletes:      xorg-x11-server-wrapper < %{version}-%{release}
Provides:       xserver-abi(ansic-%{ansic_major}) = %{ansic_minor}
Provides:       xserver-abi(videodrv-%{videodrv_major}) = %{videodrv_minor}
Provides:       xserver-abi(xinput-%{xinput_major}) = %{xinput_minor}
Provides:       xserver-abi(extension-%{extension_major}) = %{extension_minor}
Obsoletes:      xorg-x11-glamor < %{version}-%{release}
Provides:       xorg-x11-glamor = %{version}-%{release}
Obsoletes:      xorg-x11-drv-modesetting < %{version}-%{release}
Provides:       xorg-x11-drv-modesetting = %{version}-%{release}
Obsoletes:      xorg-x11-drv-vmmouse < 13.1.0-4
Provides:       Xnest = %{version}-%{release} Xdmx = %{version}-%{release}  Xvfb = %{version}-%{release} Xephyr = %{version}-%{release}
Obsoletes:      Xnest < %{version}-%{release} Xdmx < %{version}-%{release}  Xvfb < %{version}-%{release} Xephyr < %{version}-%{release}

%description
X.Org X11 X server

%package        Xephyr
Summary:        A nested server
Requires:       xorg-x11-server >= %{version}-%{release}
Provides:       Xephyr

%description    Xephyr
Xephyr is an X server which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.  Unlike
Xnest, Xephyr renders to an X image rather than relaying the
X protocol, and therefore supports the newer X extensions like
Render and Composite.

%package        devel
Summary:        SDK for X server driver module development
Requires:       xorg-x11-util-macros xorg-x11-proto-devel libXfont2-devel
Requires:       pkgconfig pixman-devel libpciaccess-devel
Provides:       xorg-x11-server-static
Obsoletes:      xorg-x11-glamor-devel < %{version}-%{release}
Provides:       xorg-x11-glamor-devel = %{version}-%{release}

%description    devel
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.

%package_help

%prep
%autosetup -N -n xorg-server-%{version}
rm -rf .git
cp %{SOURCE1} .gitignore
%global __scm git
%{expand:%__scm_setup_git -q}
%autopatch

getmajor() {
    grep -i ^#define.ABI.$1_VERSION hw/xfree86/common/xf86Module.h |
    tr '(),' '   ' | awk '{ print $4 }'
}

getminor() {
    grep -i ^#define.ABI.$1_VERSION hw/xfree86/common/xf86Module.h |
    tr '(),' '   ' | awk '{ print $5 }'
}

test `getmajor ansic` == %{ansic_major}
test `getminor ansic` == %{ansic_minor}
test `getmajor videodrv` == %{videodrv_major}
test `getminor videodrv` == %{videodrv_minor}
test `getmajor xinput` == %{xinput_major}
test `getminor xinput` == %{xinput_minor}
test `getmajor extension` == %{extension_major}
test `getminor extension` == %{extension_minor}


%build

export LDFLAGS="$RPM_LD_FLAGS -specs=/usr/lib/rpm/generic-hardened-ld"
export CXXFLAGS="$RPM_OPT_FLAGS -specs=/usr/lib/rpm/generic-hardened-cc1"
export CFLAGS="$RPM_OPT_FLAGS -specs=/usr/lib/rpm/generic-hardened-cc1"

%ifnarch %{ix86} x86_64
%global no_int10 --disable-vbe --disable-int10-module
%endif

%global xservers --enable-xvfb --enable-xnest %{kdrive} --enable-xorg
%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"
%global kdrive --enable-kdrive --enable-xephyr --disable-xfake --disable-xfbdev
%global bodhi_flags --with-vendor-name="openEuler Project"
%global dri_flags --enable-dri --enable-dri2 --enable-dri3 --enable-suid-wrapper --enable-glamor

autoreconf -ivf || exit 1

%configure %{xservers} \
        --enable-dependency-tracking \
        --enable-xwayland-eglstream \
        --with-pic \
        %{?no_int10} --with-int10=x86emu \
        --with-default-font-path=%{default_font_path} \
        --with-module-dir=%{_libdir}/xorg/modules \
        --with-builderstring="Build ID: %{name} %{version}-%{release}" \
        --with-os-name="$(hostname -s) $(uname -r)" \
        --with-xkb-output=%{_localstatedir}/lib/xkb \
        --without-dtrace \
        --disable-linux-acpi --disable-linux-apm \
        --enable-xselinux --enable-record --enable-present \
        --enable-config-udev \
        --disable-unit-tests \
        --enable-dmx \
        --enable-xwayland \
        %{dri_flags} %{?bodhi_flags} \
        ${CONFIGURE}

%make_build V=1

%check
make check

%install
%make_install

install -d %{buildroot}/%{_libdir}/xorg/modules/{drivers,input}

install -d %{buildroot}/%{_sysconfdir}/pam.d
install -m 644 %{SOURCE10} %{buildroot}/%{_sysconfdir}/pam.d/xserver

install -d %{buildroot}/%{_datadir}/X11/xorg.conf.d
install -m 644 %{SOURCE4} %{buildroot}/%{_datadir}/X11/xorg.conf.d

install -d %{buildroot}/%{_sysconfdir}/X11/xorg.conf.d

%if %{stable_abi}
install -m 755 %{SOURCE30} %{buildroot}/%{_bindir}/xserver-sdk-abi-requires
%else
sed -e s/@MAJOR@/%{gitdate}/g -e s/@MINOR@/%{minor_serial}/g %{SOURCE31} > \
    %{buildroot}/%{_bindir}/xserver-sdk-abi-requires
chmod 755 %{buildroot}/%{_bindir}/xserver-sdk-abi-requires
%endif

install -m 0755 %{SOURCE20} %{buildroot}/%{_bindir}/xvfb-run

%global xserver_source_dir %{_datadir}/xorg-x11-server-source
%global inst_srcdir %{buildroot}/%{xserver_source_dir}

install -d %{inst_srcdir}/{Xext,xkb,GL,hw/{xquartz/bundle,xfree86/common}}
install -d %{inst_srcdir}/{hw/dmx/doc,man,doc,hw/dmx/doxygen}
cp {,%{inst_srcdir}/}hw/xquartz/bundle/cpprules.in
cp {,%{inst_srcdir}/}man/Xserver.man
cp {,%{inst_srcdir}/}doc/smartsched
cp {,%{inst_srcdir}/}hw/dmx/doxygen/doxygen.conf.in
cp {,%{inst_srcdir}/}xserver.ent.in
cp {,%{inst_srcdir}/}hw/xfree86/Xorg.sh.in
cp xkb/README.compiled %{inst_srcdir}/xkb
cp hw/xfree86/xorgconf.cpp %{inst_srcdir}/hw/xfree86

find . -type f | egrep '.*\.(c|h|am|ac|inc|m4|h.in|pc.in|man.pre|pl|txt)$' |
xargs tar cf - | (cd %{inst_srcdir} && tar xf -)
find %{inst_srcdir}/hw/xfree86 -name \*.c -delete

{
%delete_la
%ifnarch %{ix86} x86_64
    rm -f %{buildroot}/%{_libdir}/xorg/modules/lib{int10,vbe}.so
%endif
}

%files
%defattr(-,root,root)
%doc COPYING
%config %attr(0644,root,root) %{_sysconfdir}/pam.d/xserver
%{_bindir}/*
%{_libexecdir}/Xorg
%attr(4755,root,root) %{_libexecdir}/Xorg.wrap
%{_libdir}/xorg/modules/drivers/modesetting_drv.so
%{_libdir}/xorg/modules/extensions/libglx.so
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libfb*.so
%{_libdir}/xorg/modules/libglamoregl.so
%{_libdir}/xorg/modules/libs*.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libwfb.so
%ifarch %{ix86} x86_64
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libvbe.so
%endif
%dir %{_sysconfdir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-quirks.conf
%{_datadir}/xorg-x11-server-source
%exclude %{_bindir}/Xephyr

%files Xephyr
%defattr(-,root,root)
%{_bindir}/Xephyr

%files devel
%defattr(-,root,root)
%{_bindir}/xserver-sdk-abi-requires
%{_libdir}/pkgconfig/xorg-server.pc
%{_includedir}/xorg/*.h
%{_datadir}/aclocal/xorg-server.m4

%files help
%defattr(-,root,root)
%doc ChangeLog README.md
%{_mandir}/man*/*
%{_localstatedir}/lib/xkb/README.compiled
%{_libdir}/xorg/protocol.txt

%changelog
* Thu Apr 29 2021 wangkerong <wangkerong@huawei.com> - 1.20.8-5
- Type:BugFix
- Id:NA
- SUG:Compilation optimization

* Mon Feb 01 2020 yeah_wang<wangye70@huawei.com> - 1.20.8-4
- Type:CVE
- Id:CVE-2020-14347 CVE-2020-14360 CVE-2020-25712
- SUG:NA
- DESC:fix CVE-2020-14347CVE-2020-14360CVE-2020-25712

* Wed Dec 09 2020 orange-snn<songnannan2@huawei.com> - 1.20.8-3
- Type:CVE
- Id:CVE-2020-14345
- SUG:NA
- DESC:fix CVE-2020-14345

* Tue Dec 08 2020 zhanzhimin<zhanzhimin@huawei.com> - 1.20.8-2
- Type:CVE
- Id:CVE-2020-14346,CVE-2020-14361,CVE-2020-14362
- SUG:NA
- DESC:fix CVE-2020-14346,CVE-2020-14361,CVE-2020-14362

* Tue Jul 28 2020 chengguipeng<chengguipeng1@huawei.com> - 1.20.8-1
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:Update to 1.20.8

* Mon Mar 16 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.20.6-4
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:patch init

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.20.6-3
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:enable make test

* Tue Jan 14 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.20.6-2
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:delete the isa in Obsoletes

* Sat Jan 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.20.6-1
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:update version to 1.20.6

* Thu Jan 3 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.20.1-12
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:bugfix about CVE-2018-20839.patch

* Tue Dec 31 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.20.1-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimization the spec

* Sun Dec 29 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.20.1-10
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:optimization the spec

* Mon Dec 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.20.1-9
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:modify the standard for fonts

* Thu Oct 31 2019 shenyangyang <shenyangyang4@huawei.com> - 1.20.1-8
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:add provides of xorg-x11-server-Xwayland(aarch-64)

* Wed Oct 23 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.20.1-7
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:change the path of the lib*.so files

* Sat Oct 12 2019 openEuler Buildteam <buildteam@openeuler.org> - 1.20.1-6
- Package init
