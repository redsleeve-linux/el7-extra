# EL7-extra

This repository contains the sources for rpms which RedSleeve adds on top of the upstream rpms
Some rpms are just rebuilds of items found elsewhere on the web. They are documented below.

| package | source | reason
| --- | --- | ---
| cmocka | EPEL | needed for building `ipa`
| nss_wrapper | CentOS BuildSystem | needed for building `ipa`
| python-cryptography-vectors | CentOS BuildSystem | needed for building `python-cryptography`
| python-hypothesis | CentOS BuildSystem | needed for building `python-cryptography`
| python-iso8601 | CentOS BuildSystem | needed for building `python-cryptography`
| python-lesscpy | CentOS BuildSystem | needed for building `ipa`
| python-mock | CentOS BuildSystem | needed for building `python-requests-oauthlib`
| python-pretend | CentOS BuildSystem | needed for building `python-cryptography`
| ttembed | EPEL | needed for building `fontawesome-fonts` and `open-sans-fonts`
| vboot-utils | ??? | build by Gordan
| zfs-fuse | ??? | build by Gordan

The original packages from 'CentOS BuildSystem' can be found here: https://buildlogs.centos.org/c7.1708.00/.staging/
