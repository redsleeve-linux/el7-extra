#
# spec file for package bcm43xx-firmware
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           bcm43xx-firmware
Version:        20180314
Release:        5.1
Summary:        Firmware for the Broadcom/Cypress BCM43xx chipset family
License:        SUSE-Firmware
Group:          System/Kernel
Url:            https://community.cypress.com/community/linux
# From https://github.com/raspberrypi/linux/issues/1325#issuecomment-195560582
# Phil Elwell (Raspberry Pi Foundation) wrote: "Broadcom have said that
# the firmware files for the BCM43438 are covered under this licence:"
Source0:        https://git.kernel.org/cgit/linux/kernel/git/firmware/linux-firmware.git/plain/LICENCE.broadcom_bcm43xx
Source1:        50-brcmfmac.conf
Source2:        install-brcmfmac.sh
#BCM4329
Source291:      https://raw.githubusercontent.com/SolidRun/meta-solidrun-arm-imx6/fido/recipes-bsp/broadcom-nvram-config/files/solidrun-imx6/brcmfmac4329-sdio.txt#/brcmfmac4329-sdio-cubox-i.txt
#BCM4330
Source301:      https://raw.githubusercontent.com/SolidRun/meta-solidrun-arm-imx6/fido/recipes-bsp/broadcom-nvram-config/files/solidrun-imx6/brcmfmac4330-sdio.txt#/brcmfmac4330-sdio-cubox-i.txt
#BCM4339
Source391:      brcmfmac4339-sdio-vega-s95-telos.txt
#BCM43362
Source3621:     http://dl.cubieboard.org/public/Cubieboard/benn/firmware/ap6210/nvram_ap6210.txt#/brcmfmac43362-sdio-cubietruck.txt
Source3622:     https://github.com/Bananian/bananian/raw/master/deb/u-boot-m2-bananian_armhf/lib/firmware/brcm/brcmfmac43362-sdio.txt#/brcmfmac43362-sdio-bananapi-m2.txt
Source3623:     https://github.com/Bananian/bananian/raw/master/deb/u-boot-pro-bananian_armhf/lib/firmware/brcm/brcmfmac43362-sdio.txt#/brcmfmac43362-sdio-bananapi-m1+.txt
#BCM43430
Source4301:     https://github.com/RPi-Distro/firmware-nonfree/raw/master/brcm/brcmfmac43430-sdio.txt#/brcmfmac43430-sdio-raspberrypi3b.txt
Source4309:     http://phelum.net/temp/BCM43430A1.hcd
#BCM43455
Source4551:     https://github.com/RPi-Distro/firmware-nonfree/raw/master/brcm/brcmfmac43455-sdio.txt#/brcmfmac43455-sdio-raspberrypi3b.txt
# Owns /lib/firmware/brcm and potentially conflicts
BuildRequires:  kernel-firmware
# Owns /etc/modprobe.d
BuildRequires:  kmod
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
This package provides the firmware files needed for the
Broadcom (now Cypress) BCM43430 Wifi+Bluetooth chipset
as well as NVRAM config files for BCM43362, BCM43430 and
further related chipsets.

%prep
%setup -q -c -T
cp %{SOURCE0} .

%build

%install
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d
install -c -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/modprobe.d
mkdir -p %{buildroot}%{_sbindir}
install -c -m 0755 %{SOURCE2} %{buildroot}%{_sbindir}/install-brcmfmac
# Used by brcmfmac
mkdir -p %{buildroot}/lib/firmware/brcm
install -c -m 0644 %{SOURCE291} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE301} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE391} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE3621} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE3622} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE3623} %{buildroot}/lib/firmware/brcm/
install -c -m 0644 %{SOURCE4301} %{buildroot}/lib/firmware/brcm/brcmfmac43430-sdio.txt
install -c -m 0644 %{SOURCE4551} %{buildroot}/lib/firmware/brcm/brcmfmac43455-sdio.txt
# Used by bluez (hciattach)
install -c -m 0644 %{SOURCE4309} %{buildroot}/lib/firmware/

%files
%defattr(-,root,root)
%doc LICENCE.broadcom_bcm43xx
/lib/firmware/*.hcd
/lib/firmware/brcm/*.txt
%ghost /lib/firmware/brcm/brcmfmac4329-sdio.txt
%ghost /lib/firmware/brcm/brcmfmac4330-sdio.txt
%ghost /lib/firmware/brcm/brcmfmac4339-sdio.txt
%ghost /lib/firmware/brcm/brcmfmac43362-sdio.txt
%{_sysconfdir}/modprobe.d/50-brcmfmac.conf
%{_sbindir}/install-brcmfmac

%changelog
* Fri Mar 16 2018 Jacco Ligthart <jacco@redsleeve.org>
- removed the symlinking for raspberrypi.
- changed buildrequirements to RSEL packages

* Wed Mar 14 2018 agraf@suse.com
- Add support for RPi 3 B+ (bcm43455, bsc#1085262)
* Mon Jun 12 2017 afaerber@suse.de
- Add Supplements for Raspberry Pi 3 (bsc#1041823)
- Resolve NUL char warning on modprobe for Tumbleweed by properly
  iterating over zero-separated DT compatible strings
* Mon Apr 10 2017 afaerber@suse.de
- Require kernel-firmware, suggested by fvogt. (bsc#1033137)
  Don't require version 20161005 or later, to remain compatible
  with older distributions.
- Bump version to today's date. This will allow other packages
  such as kernel-firmware to conflict against our older version.
* Sun Jan 15 2017 afaerber@suse.de
- Add brcmfmac4339-sdio-vega-s95-telos.txt
* Sun Jan  8 2017 afaerber@suse.de
- Add vendor prefix for CuBox-i compatible string
- Reorder by board name
* Tue Jan  3 2017 tbechtold@suse.com
- Add brcmfmac4329-sdio-cubox-i.txt and brcmfmac4330-sdio-cubox-i.txt.
* Tue Oct 18 2016 afaerber@suse.de
- Dropped brcmfmac43430-sdio.bin (in kernel-firmware now)
* Wed Sep  7 2016 afaerber@suse.de
- Move %%post script to install-brcmfmac.sh, add 50-brcmfmac.conf.
  This avoids workarounds for Kiwi images. (tiwai)
* Sat Sep  3 2016 afaerber@suse.de
- Renamed package from bcm43430-firmware to bcm43xx-firmware (duwe)
- Renamed brcmfmac43430-sdio.txt to brcmfmac43430-sdio-rpi3.txt and
  added post-install script to symlink
  * Added brcmfmac43362-sdio-{cubietruck,bananapi-{m1+,m2}}.txt
* Tue Aug 30 2016 afaerber@suse.de
- Renamed package from brcm43430-firmware to bcm43430-firmware
* Mon Aug 29 2016 fvogt@suse.com
- Make Source: URLs absolute
- Update brcmfmac43430-sdio.bin to 7.45.41.26
* Thu Aug 25 2016 fvogt@suse.com
- Add initial package
