# $Id$
# Authority: dag

### EL6 ships with cifs-utils-4.4-5.el6
# ExclusiveDist: el2 el3 el4 el5

%{?el4:%define _without_keyutils 1}
%{?el3:%define _without_keyutils 1}

Summary: Utilities for mounting and managing CIFS mounts
Name: cifs-utils
Version: 4.6
Release: 2%{?dist}
License: GPLv3
Group: System Environment/Daemons
URL: http://linux-cifs.samba.org/cifs-utils/

Source: ftp://ftp.samba.org/pub/linux-cifs/cifs-utils/cifs-utils-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: autoconf
BuildRequires: automake
%{!?_without_keyutils:BuildRequires: keyutils-libs-devel}
BuildRequires: krb5-devel
#BuildRequires: libcap-ng-devel
BuildRequires: libtalloc-devel
Requires: keyutils

%description
The SMB/CIFS protocol is a standard file sharing protocol widely deployed
on Microsoft Windows machines. This package contains tools for mounting
shares on Linux using the SMB/CIFS protocol. The tools in this package
work in conjunction with support in the kernel to allow one to mount a
SMB/CIFS share onto a client and use it as if it were a standard Linux
file system.

%prep
%setup

%build
%configure
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{!?_without_keyutils:%doc %{_mandir}/man8/cifs.upcall.8*}
%doc %{_mandir}/man8/mount.cifs.8*
/sbin/mount.cifs
%{!?_without_keyutils:%{_sbindir}/cifs.upcall}

%changelog
* Tue Oct 19 2010 Dag Wieers <dag@wieers.com> - 4.6-2
- Rebuild against libtalloc 1.2.0 on RHEL5.

* Mon Aug 02 2010 Dag Wieers <dag@wieers.com> - 4.6-1
- Updated to release 4.6.

* Sun Jun 13 2010 Dag Wieers <dag@wieers.com> - 4.5-1
- Initial package. (based on Fedora)
