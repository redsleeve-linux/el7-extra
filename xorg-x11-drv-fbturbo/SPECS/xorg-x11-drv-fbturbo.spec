%define moduledir %(pkg-config xorg-server --variable=moduledir )
%define driverdir %{moduledir}/drivers
%define gitdate 20150221
%define gitrev .%{gitdate}

Summary:   Xorg X11 fbturbo driver
Name:      xorg-x11-drv-fbturbo
Version:   0.5.1
Release:   0.4%{?gitrev}%{?dist}
URL:       https://github.com/ssvb/xf86-video-fbturbo
License:   MIT and GPLv2
Group:     User Interface/X Hardware Support

Source0:    xf86-video-fbturbo-%{gitdate}.tar.bz2
Source1:    make-git-snapshot.sh

BuildRequires: kernel-headers
BuildRequires: libdrm-devel
BuildRequires: libudev-devel
BuildRequires: libXext-devel 
BuildRequires: libXrandr-devel 
BuildRequires: libXv-devel
BuildRequires: mesa-libGL-devel
BuildRequires: pixman-devel
BuildRequires: xorg-x11-server-devel
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf automake libtool
BuildRequires: perl-Carp

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

ExcludeArch: s390 s390x

%description 
Xorg DDX driver for ARM devices (Allwinner, RPi and others), it's
based on the fbdev driver so will work in all places it does
but has NEON optimised code paths to improve ARM

%if 0%{?gitdate}
%define dirsuffix %{gitdate}
%else
%define dirsuffix %{version}
%endif

%prep
%setup -q -n xf86-video-fbturbo-%{?gitdate:%{gitdate}}%{!?gitdate:%{dirsuffix}} 
touch AUTHORS

%build
%{?gitdate:autoreconf -v --install}

%configure --disable-static  --libdir=%{_libdir} --mandir=%{_mandir}
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

# Remove libtool archives and static libs
find %{buildroot} -type f -name "*.la" -delete

%files
%{!?_licensedir:%global license %%doc}
%license COPYING
%doc README
%{driverdir}/fbturbo_drv.so
%{_mandir}/man4/fbturbo.4*

%changelog
* Mon Aug 28 2017 Jacco Ligthart <jacco@redsleeve.org> 0.5.1-0.4
- rebuild for new xorg ABI

* Fri Dec 18 2015 Jacco Ligthart <jacco@redsleeve.org> 0.5.1-0.3
- rebuild for new xorg ABI

* Tue Mar 24 2015 Dan Horák <dan[at]danny.cz> 0.5.1-0.2
- exclude s390(x)

* Sat Feb 21 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.5.1-0.1
- Initial build
