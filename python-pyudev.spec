%global srcname pyudev
Name:             python-%{srcname}
Version:          0.17
Release:          1%{?dist}
Summary:          A libudev binding

License:          LGPLv2+
URL:              http://pypi.python.org/pypi/pyudev
Source0:          http://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

Patch0:           0001-Do-not-install-the-tests-as-a-module.patch

BuildArch:        noarch

%description
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%package -n python2-%{srcname}
Summary:          A libudev binding
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:    python2-devel
BuildRequires:    python-setuptools

%description -n python2-%{srcname}
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%package -n python3-%{srcname}
Summary:          A libudev binding
%{?python_provide:%python_provide python2-%{srcname}}

BuildRequires:    python3-devel
BuildRequires:    python3-setuptools

%description -n python3-pyudev
pyudev is a LGPL licensed, pure Python binding for libudev, the device
and hardware management and information library for Linux.  It supports
almost all libudev functionality, you can enumerate devices, query device
properties and attributes or monitor devices, including asynchronous
monitoring with threads, or within the event loops of Qt, Glib or wxPython.

The binding supports CPython 2 (2.6 or newer) and 3 (3.1 or newer), and
PyPy 1.5 or newer.  It is tested against udev 151 or newer, earlier
versions of udev as found on dated Linux systems may work, but are not
officially supported.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf pyudev.egg-info

%build
%py2_build
%py3_build

%install
%py2_install
%py3_install

%files -n python2-%{srcname}
%license COPYING
%doc README.rst CHANGES.rst
%{python2_sitelib}/pyudev
%{python2_sitelib}/pyudev-%{version}-*.egg-info

%files -n python3-%{srcname}
%license COPYING
%doc README.rst CHANGES.rst
%{python3_sitelib}/pyudev
%{python3_sitelib}/pyudev-%{version}-*.egg-info

%changelog
* Mon Sep 14 2015 David Shea <dshea@redhat.com> - 0.17.1-1
- Really start the monitor on pyudev.Monitor.poll()
- Force non-blocking IO in pyudev.Monitor to avoid blocking on receiving the device
- Set proper flags on pipe fs
- Handle irregular polling events properly
- Rename MonitorObserver GUI classes and deprecate the old ones
- Remove patches for #1170337 and #1230773 that are now part of upstream
- Switch to new packaging guidelines which renames python-pyudev to python2-pyudev

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.16.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 12 2015 David Shea <dshea@redhat.com> - 0.16.1-3
- Retry interrupted system calls (#1230773)
- Rearrange the build process to match current packaging recommendations

* Wed Jan 28 2015 David Shea <dshea@redhat.com> - 0.16.1-2
- Use %%license for the license file

* Wed Dec 10 2014 David Shea <dshea@redhat.com> - 0.16.1-1
- Update to pyudev-0.16.1 (#880644)
- Apply a patch from upstream to remove a global reference to libudev (#1170337)

* Wed Dec 10 2014 David Shea <dshea@redhat.com> - 0.15-7
- Fix license tag (LGPL -> LGPLv2+) (#990579)
- Remove rst tags from description
- Remove unnecessary requires and buildrequires (#1095459)
- Avoid packaging upstream egg-info files
- Add a python3 package
- Drop the Group tag which wasn't even the right group

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Jul 23 2012 Chris Lockfort <clockfort@redhat.com> 0.15-3
- Reflect rawhide merging udev into systemd
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.15-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Mon Jun 18 2012 Chris Lockfort <clockfort@redhat.com> 0.15-1
- initial package
