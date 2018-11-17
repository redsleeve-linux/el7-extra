%define debug_package %{nil}
%define product_family RedSleeve Linux
%define variant_titlecase Server
%define variant_lowercase server
%define release_name Core
%define base_release_version 7
%define full_release_version 7
%define dist_release_version 7
%define upstream_rel_long 7.6-4
%define upstream_rel 7.6
%define redsleeve_rel 6.1810
#define beta Beta
%define dist .el%{dist_release_version}

Name:           redsleeve-release
Version:        %{base_release_version}
Release:        %{redsleeve_rel}%{?dist}.1
Summary:        %{product_family} release file
Group:          System Environment/Base
License:        GPLv2
Provides:       redsleeve-release = %{version}-%{release}
Provides:       redsleeve-release(upstream) = %{upstream_rel}
Provides:       redhat-release = %{upstream_rel_long}
Provides:       system-release = %{upstream_rel_long}
Provides:       system-release(releasever) = %{base_release_version}
Source0:        redsleeve-release-%{base_release_version}-%{redsleeve_rel}.tar.gz
Source1:        85-display-manager.preset
Source2:        90-default.preset


%description
%{product_family} release files

%prep
%setup -q -n redsleeve-release-%{base_release_version}

%build
echo OK

%install
rm -rf %{buildroot}

# create /etc
mkdir -p %{buildroot}/etc

# create /etc/system-release and /etc/redhat-release
echo "%{product_family} release %{full_release_version}.%{redsleeve_rel} (%{release_name}) " > %{buildroot}/etc/redsleeve-release
echo "Derived from Red Hat Enterprise Linux %{upstream_rel} (Source)" > %{buildroot}/etc/redhat-release
ln -s redsleeve-release %{buildroot}/etc/system-release

# create /etc/os-release
cat << EOF >>%{buildroot}/etc/os-release
NAME="%{product_family}"
VERSION="%{full_release_version} (%{release_name})"
ID="redsleeve"
ID_LIKE="rhel fedora"
VERSION_ID="%{full_release_version}"
PRETTY_NAME="%{product_family} %{full_release_version} (%{release_name})"
ANSI_COLOR="0;31"
CPE_NAME="cpe:/o:redsleeve:redsleeve:7"
HOME_URL="https://www.redsleeve.org/"
BUG_REPORT_URL="https://bugs.redsleeve.org/"

CENTOS_MANTISBT_PROJECT="RedSleeve-7"
CENTOS_MANTISBT_PROJECT_VERSION="7"
REDHAT_SUPPORT_PRODUCT="redsleeve"
REDHAT_SUPPORT_PRODUCT_VERSION="7"

EOF
# write cpe to /etc/system/release-cpe
echo "cpe:/o:redsleeve:redsleeve:7" > %{buildroot}/etc/system-release-cpe

# create /etc/issue and /etc/issue.net
echo '\S' > %{buildroot}/etc/issue
echo 'Kernel \r on an \m' >> %{buildroot}/etc/issue
cp %{buildroot}/etc/issue %{buildroot}/etc/issue.net
echo >> %{buildroot}/etc/issue

# copy GPG keys
mkdir -p -m 755 %{buildroot}/etc/pki/rpm-gpg
for file in RPM-GPG-KEY* ; do
    install -m 644 $file %{buildroot}/etc/pki/rpm-gpg
done

# copy yum repos
mkdir -p -m 755 %{buildroot}/etc/yum.repos.d
for file in RedSleeve-*.repo; do 
    install -m 644 $file %{buildroot}/etc/yum.repos.d
done

mkdir -p -m 755 %{buildroot}/etc/yum/vars
install -m 0644 yum-vars-infra %{buildroot}/etc/yum/vars/infra

# set up the dist tag macros
install -d -m 755 %{buildroot}/etc/rpm
cat >> %{buildroot}/etc/rpm/macros.dist << EOF
# dist macros.

%%redsleeve_ver %{base_release_version}
%%redsleeve %{base_release_version}
%%rhel %{base_release_version}
%%dist %dist
%%el%{base_release_version} 1
EOF

# use unbranded datadir
mkdir -p -m 755 %{buildroot}/%{_datadir}/redsleeve-release
ln -s redsleeve-release %{buildroot}/%{_datadir}/redhat-release
install -m 644 EULA %{buildroot}/%{_datadir}/redsleeve-release

# use unbranded docdir
mkdir -p -m 755 %{buildroot}/%{_docdir}/redsleeve-release
ln -s redsleeve-release %{buildroot}/%{_docdir}/redhat-release
install -m 644 GPL %{buildroot}/%{_docdir}/redsleeve-release

# copy systemd presets
mkdir -p %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE1} %{buildroot}%{_prefix}/lib/systemd/system-preset/
install -m 0644 %{SOURCE2} %{buildroot}%{_prefix}/lib/systemd/system-preset/


%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
/etc/redhat-release
/etc/system-release
/etc/redsleeve-release
%config(noreplace) /etc/os-release
%config /etc/system-release-cpe
%config(noreplace) /etc/issue
%config(noreplace) /etc/issue.net
/etc/pki/rpm-gpg/
%config(noreplace) /etc/yum.repos.d/*
%config(noreplace) /etc/yum/vars/*
/etc/rpm/macros.dist
%{_docdir}/redhat-release
%{_docdir}/redsleeve-release/*
%{_datadir}/redhat-release
%{_datadir}/redsleeve-release/*
%{_prefix}/lib/systemd/system-preset/*

%changelog
* Fri Nov 16 2018 Jacco Ligthart <jacco@redsleeve.org>
- updated to 7.6

* Sat Apr 14 2018 Jacco Ligthart <jacco@redsleeve.org>
- updated to 7.5

* Thu Aug 03 2017 Jacco Ligthart <jacco@redsleeve.org>
- updated to 7.4

* Mon Dec 12 2016 Jacco Ligthart <jacco@redsleeve.org>
- updated to 7.3

* Fri Sep 23 2016 Jacco Ligthart <jacco@redsleeve.org>
- updated to 7.2

* Sun Jul 05 2015 Gordan Bobic <gordan@redsleeve.org>
- Initial release
