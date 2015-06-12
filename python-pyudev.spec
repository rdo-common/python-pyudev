Name:             python-pyudev
Version:          0.16.1
Release:          3%{?dist}
Summary:          A libudev binding

License:          LGPLv2+
URL:              http://pypi.python.org/pypi/pyudev
Source0:          http://pypi.python.org/packages/source/p/pyudev/pyudev-%{version}.tar.gz

# Based on 0113ccdbba1aef69f3f890fd72622f24d79d907a in github.com/lunaryorn/pyudev.git
Patch0:           pyudev-0.16.1-global-libudev.patch

# Based on af9ba7b27478274a2f5f9676de662b079a3a8c22 in github.com/dashea/pyudev.git
Patch1:           pyudev-eintr-retry.patch

BuildArch:        noarch

BuildRequires:    python2-devel
BuildRequires:    python-setuptools

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

%package -n python3-pyudev
Summary:          A libudev binding
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
%setup -qc
mv pyudev-%{version} python2

pushd python2
rm -rf pyudev.egg-info

%patch0 -p1 -b .global-libudev
%patch1 -p1 -b .eintr-retry

# Copy common doc files to the top directory
cp -pr COPYING README.rst CHANGES.rst ../
popd

cp -a python2 python3

%build
pushd python2
%{__python2} setup.py build 
popd

pushd python3
%{__python3} setup.py build
popd

%install
pushd python2
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd

pushd python3
%{__python3} setup.py install --skip-build --root $RPM_BUILD_ROOT
popd

%files
%license COPYING
%doc README.rst CHANGES.rst
%{python2_sitelib}/pyudev
%{python2_sitelib}/pyudev-%{version}-*.egg-info

%files -n python3-pyudev
%license COPYING
%doc README.rst CHANGES.rst
%{python3_sitelib}/pyudev
%{python3_sitelib}/pyudev-%{version}-*.egg-info

%changelog
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
