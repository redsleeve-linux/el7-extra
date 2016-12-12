Name:           epel-release
Version:        7
Release:        20150510
Summary:        Extra Packages for Enterprise Linux repository configuration

Group:          System Environment/Base
License:        GPLv2

# This is a Red Hat maintained package which is specific to
# our distribution.  Thus the source is only available from
# within this srpm.
URL:            http://ftp.redsleeve.org/pub/el7/EPEL-full/
#Source0:        http://ftp.redsleeve.org/pub/el6/packages/epel/RPM-GPG-KEY-epel
Source0:        GPL
Source1:        epel.repo

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:     noarch
Requires:      redhat-release >=  %{version}
Conflicts:     fedora-release

%description
This package contains the Extra Packages for Enterprise Linux (EPEL) repository
GPG key as well as configuration for yum.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
#install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
#install -Dpm 644 %{SOURCE0} \
#    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-epel

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d
install -pm 644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc GPL
%config(noreplace) /etc/yum.repos.d/*
#/etc/pki/rpm-gpg/*


%changelog
* Sun May 10 2015 <jacco@redsleeve.org> - 7-20150510
- adjusted for el7

* Sun Mar 02 2014 <gordan@redsleeve.org> - 6-20140302
- Initial release