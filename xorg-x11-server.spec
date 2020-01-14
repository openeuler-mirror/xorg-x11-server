%undefine _hardened_build
%undefine _strict_symbol_defs_build

#global gitdate 20161026
%global stable_abi 1

%global ansic_major 0
%global ansic_minor 4
%global videodrv_major 24
%global videodrv_minor 0
%global xinput_major 24
%global xinput_minor 1
%global extension_major 10
%global extension_minor 0
%global pkgname xorg-server

Name:           xorg-x11-server
Version:        1.20.6
Release:        2
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

Patch6000:	xorg-s11-server-CVE-2018-20839.patch

BuildRequires:  audit-libs-devel autoconf automake bison dbus-devel flex flex-devel git
BuildRequires:  systemtap-sdt-devel libtool pkgconfig xorg-x11-util-macros xorg-x11-proto-devel
BuildRequires:  xorg-x11-font-utils libepoxy-devel systemd-devel xorg-x11-xtrans-devel
BuildRequires:  libXfont2-devel libXau-devel libxkbfile-devel libXres-devel
BuildRequires:  libfontenc-devel libXtst-devel libXdmcp-devel libX11-devel libXext-devel
BuildRequires:  libXinerama-devel libXi-devel libXt-devel libdmx-devel libXmu-devel libXrender-devel
BuildRequires:  libXi-devel libXpm-devel libXaw-devel libXfixes-devel libepoxy-devel
BuildRequires:  wayland-devel wayland-protocols-devel egl-wayland-devel libxshmfence-devel
BuildRequires:  libXv-devel pixman-devel libpciaccess-devel openssl-devel kernel-headers
BuildRequires:  mesa-libGL-devel mesa-libEGL-devel mesa-libgbm-devel libdrm-devel
BuildRequires:  xcb-util-devel xcb-util-image-devel xcb-util-wm-devel libudev-devel
BuildRequires:  xcb-util-keysyms-devel xcb-util-renderutil-devel libselinux-devel

%ifarch aarch64 %{arm} x86_64
BuildRequires:  libunwind-devel
%endif

Requires:       pixman >= 0.30.0 xkeyboard-config xkbcomp
Requires:       system-setup-keyboard xorg-x11-drv-libinput libEGL
Requires:       xorg-x11-xauth

Obsoletes:      %{name}-common %{name}-Xorg %{name}-Xorg %{name}-Xnest %{name}-source %{name}-Xdmx %{name}-Xvfb %{name}-Xwayland
Provides:       %{name}-common %{name}-Xorg %{name}-Xorg%{?_isa} %{name}-Xnest %{name}-source %{name}-Xdmx %{name}-Xvfb %{name}-Xwayland %{name}-Xwayland%{?_isa}

Provides:       Xorg = %{version}-%{release}
Provides:       Xserver
Provides:       xorg-x11-server-wrapper = %{version}-%{release}
Provides:       xserver-abi(ansic-%{ansic_major}) = %{ansic_minor}
Provides:       xserver-abi(videodrv-%{videodrv_major}) = %{videodrv_minor}
Provides:       xserver-abi(xinput-%{xinput_major}) = %{xinput_minor}
Provides:       xserver-abi(extension-%{extension_major}) = %{extension_minor}
Obsoletes:      xorg-x11-glamor < %{version}-%{release}
Provides:       xorg-x11-glamor = %{version}-%{release}
Obsoletes:      xorg-x11-drv-modesetting < %{version}-%{release}
Provides:       xorg-x11-drv-modesetting = %{version}-%{release}
Obsoletes:      xorg-x11-drv-vmmouse < 13.1.0-4
Provides:       Xnest Xdmx Xvfb Xephyr

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

export LDFLAGS="$RPM_LD_FLAGS -specs=/usr/lib/rpm/%{_vendor}/%{_vendor}-hardened-ld"
export CXXFLAGS="$RPM_OPT_FLAGS -specs=/usr/lib/rpm/%{_vendor}/%{_vendor}-hardened-cc1"
export CFLAGS="$RPM_OPT_FLAGS -specs=/usr/lib/rpm/%{_vendor}/%{_vendor}-hardened-cc1"

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
