Name:           redsleeve-bookmarks
Version:        7
Release:        1%{?dist}.redsleeve
Summary:        RedSleeve Linux bookmarks
Group:          Applications/Internet
License:        GFDL
URL:            http://www.redsleeve.org
Source0:        default-bookmarks.html
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Provides:       system-bookmarks, redhat-bookmarks
Obsoletes:	redhat-bookmarks, centos-bookmarks



%description
This package contains the default bookmarks for RedSleeve Linux

%prep

%build

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks


%clean
%{__rm} -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Wed Jun 03 2015 Jacco Ligthart <jacco@redsleeve.org> 7-1.el7.redsleeve
- initial version based on C7
