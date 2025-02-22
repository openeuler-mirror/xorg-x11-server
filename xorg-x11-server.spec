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
Version:        1.20.11
Release:        13
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

Patch0100: 0001-Fix-the-crash-in-shadowUpdatePacked-because-of-memcp.patch
Patch0101: 0002-present-Crash-in-present_scmd_get_crtc-and-present_flush.patch

Patch0029: xorg-s11-server-CVE-2018-20839.patch
Patch0030: 0025-fix-compile-error-with-gcc-12.patch
Patch6000: backport-CVE-2021-4008.patch
Patch6001: backport-CVE-2021-4009.patch
Patch6002: backport-CVE-2021-4010.patch
Patch6003: backport-CVE-2021-4011.patch
Patch6004: backport-rename-bool-to-boolean.patch
Patch6005: backport-0001-CVE-2022-2319.patch
Patch6006: backport-0002-CVE-2022-2319.patch
Patch6007: backport-CVE-2022-2320.patch
Patch6008: backport-CVE-2022-3551.patch
%ifarch sw_64
Patch6009: xorg-server-1.20.11-sw.patch
%endif
Patch6010: backport-CVE-2022-3553.patch

BuildRequires:  audit-libs-devel autoconf automake bison dbus-devel flex git gcc 
BuildRequires:  systemtap-sdt-devel libtool pkgconfig 
BuildRequires:  xorg-x11-font-utils systemd-devel 
BuildRequires:  libXfont2-devel libXau-devel libxkbfile-devel libXres-devel
BuildRequires:  libfontenc-devel libXtst-devel libXdmcp-devel libX11-devel libXext-devel
BuildRequires:  libXinerama-devel libXt-devel libdmx-devel libXmu-devel libXrender-devel
BuildRequires:  libXi-devel libXpm-devel libXaw-devel libXfixes-devel libepoxy-devel libXv-devel 
BuildRequires:  openssl-devel kernel-headers
BuildRequires:  mesa-libEGL-devel mesa-libgbm-devel libudev-devel xcb-util-devel 
BuildRequires:  xcb-util-image-devel xcb-util-wm-devel xcb-util-keysyms-devel xcb-util-renderutil-devel 
BuildRequires:  xorg-x11-xtrans-devel >= 1.3.2 xorg-x11-util-macros >= 1.17 xorg-x11-proto-devel >= 7.7  
BuildRequires:  xorg-x11-font-utils >= 7.2 libselinux-devel >= 2.0.86 
BuildRequires:  libxshmfence-devel >= 1.1 pixman-devel >= 0.30.0 libdrm-devel >= 2.4.0  
BuildRequires:  mesa-libGL-devel >= 9.2 libpciaccess-devel >= 0.13.1
BuildRequires:  wayland-devel wayland-protocols-devel egl-wayland-devel 

%ifarch aarch64 %{arm} x86_64 sw_64
BuildRequires:  libunwind-devel
%endif

Requires:       pixman >= 0.30.0 xkeyboard-config xkbcomp
Requires:       system-setup-keyboard xorg-x11-drv-libinput libEGL
Requires:       xorg-x11-xauth
Requires:       xorg-x11-server-common >= %{version}-%{release}
Obsoletes:      %{name}-Xorg < %{version}-%{release}
Provides:       %{name}-Xorg = %{version}-%{release} %{name}-Xorg%{?_isa} = %{version}-%{release}

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

%description
X.Org X11 X server

%package common
Summary: Xorg server common files
Requires: pixman >= 0.30.0
Requires: xkeyboard-config xkbcomp
 
%description common
Common files shared among all X servers.

%package Xnest
Summary: A nested server
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xnest
 
%description Xnest
Xnest is an X server which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.
  
%package Xdmx
Summary: Distributed Multihead X Server and utilities
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xdmx
 
%description Xdmx
Xdmx is proxy X server that provides multi-head support for multiple displays
attached to different machines (each of which is running a typical X server).
When Xinerama is used with Xdmx, the multiple displays on multiple machines
are presented to the user as a single unified screen.  A simple application
for Xdmx would be to provide multi-head support using two desktop machines,
each of which has a single display device attached to it.  A complex
application for Xdmx would be to unify a 4 by 4 grid of 1280x1024 displays
(each attached to one of 16 computers) into a unified 5120x4096 display.
  
%package Xvfb
Summary: A X Windows System virtual framebuffer X server
# xvfb-run is GPLv2, rest is MIT
License: MIT and GPLv2
Requires: xorg-x11-server-common >= %{version}-%{release}
# required for xvfb-run
Requires: xorg-x11-xauth
Provides: Xvfb
 
%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X server that is able to run on
machines with no display hardware and no physical input devices.
Xvfb simulates a dumb framebuffer using virtual memory.  Xvfb does
not open any devices, but behaves otherwise as an X display.  Xvfb
is normally used for testing servers.

%package        Xephyr
Summary:        A nested server
Requires:       xorg-x11-server-common >= %{version}-%{release}
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

%package source
Summary: Xserver source code required to build VNC server (Xvnc)
BuildArch: noarch
 
%description source
Xserver source code needed to build VNC server (Xvnc)

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

%ifnarch %{ix86} x86_64 sw_64
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
        --disable-xwayland-eglstream \
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
        --enable-xcsecurity \
        --enable-config-udev \
        --disable-unit-tests \
        --enable-dmx \
        --disable-xwayland \
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
%ifnarch %{ix86} x86_64 sw_64
    rm -f %{buildroot}/%{_libdir}/xorg/modules/lib{int10,vbe}.so
%endif
}

%files common
%doc COPYING
%{_libdir}/xorg/protocol.txt
%dir %{_localstatedir}/lib/xkb
%{_localstatedir}/lib/xkb/README.compiled
 
%if 1
%global Xorgperms %attr(4755, root, root)
%else
# disable until module loading is audited
%global Xorgperms %attr(0711,root,root) %caps(cap_sys_admin,cap_sys_rawio,cap_dac_override=pe)
%endif
 
%files 
%config %attr(0644,root,root) %{_sysconfdir}/pam.d/xserver
%{_bindir}/X
%{_bindir}/Xorg
%{_libexecdir}/Xorg
%{Xorgperms} %{_libexecdir}/Xorg.wrap
%{_bindir}/cvt
%{_bindir}/gtf
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/modesetting_drv.so
%dir %{_libdir}/xorg/modules/extensions
%{_libdir}/xorg/modules/extensions/libglx.so
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/libfbdevhw.so
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libfb.so
%{_libdir}/xorg/modules/libglamoregl.so
%{_libdir}/xorg/modules/libshadow.so
%{_libdir}/xorg/modules/libshadowfb.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libwfb.so
%ifarch %{ix86} x86_64
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libvbe.so
%endif
%dir %{_sysconfdir}/X11/xorg.conf.d
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-quirks.conf
 
%files Xnest
%{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*
 
%files Xdmx
%{_bindir}/Xdmx
%{_bindir}/dmxaddinput
%{_bindir}/dmxaddscreen
%{_bindir}/dmxreconfig
%{_bindir}/dmxresize
%{_bindir}/dmxrminput
%{_bindir}/dmxrmscreen
%{_bindir}/dmxtodmx
%{_bindir}/dmxwininfo
%{_bindir}/vdltodmx
%{_bindir}/dmxinfo
%{_bindir}/xdmxconfig
 
%files Xvfb
%{_bindir}/Xvfb
%{_bindir}/xvfb-run
%{_mandir}/man1/Xvfb.1*
 
%files Xephyr
%{_bindir}/Xephyr
%{_mandir}/man1/Xephyr.1*
 
%files source
%{xserver_source_dir}

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

%changelog
* Tue Nov 29 2022 misaka00251 <liuxin@iscas.ac.cn> - 1.20.11-13
- Backport patch to fix build with gcc 12

* Fri Nov 18 2022 wangkerong <wangkerong@h-partners.com> -1.20.11-12
- fix CVE-2022-3551,CVE-2022-3553

* Wed Oct 26 2022 wuzx<wuzx1226@qq.com> - 1.20.11-11
- Add sw64 architecture

* Mon Oct 24 2022 qz_cx <wangqingzheng@kylinos.cn> - 1.20.11-10
- Type:CVE
- ID:NA
- SUG:NA
- DESC: fix CVE-2022-3551

* Wed Aug 03 2022 wangkerong<wangkerong@h-partners.com> - 1.20.11-9
- fix CVE-2022-2319,CVE-2022-2320

* Fri Jul 22 2022 baiguo<baiguo@kylinos.cn> - 1.20.11-8
- xkb: switch to array index loops to moving pointers
- fix CVE-2022-2319
 
* Fri Jul 22 2022 ouyangminxiang<ouyangminxiang@kylinsec.com.cn> - 1.20.11-7
- Fix the crash in shadowUpdatePacked because of memcpy acts randomly with overlapping areas.
- Fix the problem of black screen after entering the login interface

* Fri Jun 24 2022 wangkerong<wangkerong@h-partners.com> - 1.20.11-6
- disable Xwayland provide by xorg-x11-server-Xwayland
- delete the same files of common and help

* Mon Jun 6 2022 houjinchang <houjinchang@huawei.com> - 1.20.11-5
- Type:bugfix
- CVE:NA
- SUG:NA
- DESC:add xorg-x11-common require in main package

* Sat Jan 8 2022 yangcheng<yangcheng87@huawei.com> - 1.20.11-4
- rename bool to boolean

* Mon Dec 27 2021 yangcheng<yangcheng87@huawei.com> - 1.20.11-3
- provide xorg-x11-server-Xorg and xorg-x11-server-Xwayland

* Sat Dec 25 2021 yangcheng<yangcheng87@huawei.com> - 1.20.11-2
- Type:CVE
- Id:CVE-2021-4008 CVE-2021-4009 CVE-2021-4010 CVE-2021-4011
- SUG:NA
- DESC:fix CVE-2021-4008 CVE-2021-4009 CVE-2021-4010 CVE-2021-4011

* Fri Dec 3 2021 yangcheng<yangcheng87@huawei.com> - 1.20.11-1
- upgrade to 1.20.11
- split the main xorg-x11-server package


* Thu Jun 10 2021 wangkerong<wangkerong@huawei.com> - 1.20.10-6
- revert add secure compilation options

* Tue Jun 08 2021 zhanzhimin<zhanzhimin@huawei.com> - 1.20.10-5
- add secure compilation options

* Tue Jun 08 2021 zhanglin <lin.zhang@turbolinux.com.cn> - 1.20.10-4
- Remove pam_console dependency

* Mon Jun 07 2021 wangkerong<wangkerong@huawei.com> - 1.20.10-3
- Type:NA
- Id:NA
- SUG:NA
- DESC:Add a BuildRequires for gcc

* Thu Jun 03 2021 zhanzhimin<zhanzhimin@huawei.com> - 1.20.10-2
- Type:CVE
- Id:CVE-2021-3472
- SUG:NA
- DESC:fix CVE-2021-3472

* Sat Jan 30 2021 jinzhimin<jinzhmin2@huawei.com> - 1.20.10-1
- Upgrade to 1.20.10

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
