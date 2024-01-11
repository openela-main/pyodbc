%global modulename pyodbc

Name:           pyodbc
Version:        4.0.30
Release:        2%{?dist}
Summary:        Python DB API 2.0 Module for ODBC
License:        MIT
URL:            https://github.com/mkleehammer/pyodbc
Source0:        https://github.com/mkleehammer/pyodbc/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  unixODBC-devel
BuildRequires:  python3-devel

Recommends: (postgresql-odbc if postgresql-server)
Recommends: (mariadb-connector-odbc if mariadb-server)

%global _description\
A Python DB API 2 and 3 module for ODBC. This project provides an up-to-date,\
convenient interface to ODBC using native data types like datetime and\
decimal.

%description %_description

%package -n python3-%{modulename}
Summary:        Python DB API 2.0 Module for ODBC
%{?python_provide:%python_provide python3-%{modulename}}
Recommends: (mariadb-connector-odbc if mariadb-server)
Recommends: (postgresql-odbc if postgresql-server)

%description -n python3-%{modulename}
A Python DB API 2 and 3 module for ODBC. This project provides an up-to-date,
convenient interface to ODBC using native data types like datetime and
decimal.


%prep
%setup -q

%build
%py3_build

%install
%py3_install

%files -n python3-%{name}
%license LICENSE.txt
%doc README.md notes.txt
%{python3_sitearch}/*

%changelog
* Fri Nov 27 2020 Filip Janus <fjanus@redhat.com> - 4.0.30-2
- Enable gating, release bump

* Fri Oct 2 2020 Filip Janus <fjanus@redhat.com> - 4.0.30-1
- Upstream released 4.0.30
- Add Recommendation to install database connector

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 4.0.27-3
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 23 2019 Filip Janus <fjanus@redhat.com> - 4.0.27-1
- Upstream released 4.0.27

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.10-19
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 14 2019 Miro Hrončok <mhroncok@redhat.com> - 3.0.10-16
- Subpackage python2-pyodbc has been removed
  See https://fedoraproject.org/wiki/Changes/Mass_Python_2_Package_Removal

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 3.0.10-14
- Rebuilt for Python 3.7

* Wed Feb 14 2018 Iryna Shcherbina <ishcherb@redhat.com> - 3.0.10-13
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Aug 20 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.10-11
- Add Provides for the old name without %%_isa

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 3.0.10-10
- Python 2 binary package renamed to python2-pyodbc
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 3.0.10-6
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.10-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Orion Poplawski <orion@cora.wnra.com> - 3.0.10-1
- Update to 3.0.10

* Tue May 12 2015 Orion Poplawski <orion@cora.wnra.com> - 3.0.7-4
- Cleanup and update spec

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 3.0.7-3
- Rebuilt for GCC 5 C++11 ABI change

* Tue Feb 17 2015 Honza Horak <hhorak@redhat.com> - 3.0.7-2
- Start compiling for python3
  Thanks Ganapathi Kamath

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Aug 13 2012 Honza Horak <hhorak@redhat.com> - 3.0.6-1
- Upstream released 3.0.6
 
* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 2.1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Apr 22 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.5-2
- EVR bump

* Wed Apr 22 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.5-1
- Upstream released 2.1.5

* Mon Feb 23 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-5
- Removing versioned BuildRequires

* Mon Feb 23 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-4
- Changes for plague

* Sun Feb 22 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-3
- Removed extraneous Requires

* Sun Feb 22 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-2
- Added README.rst file from git repo

* Wed Jan 07 2009 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.4-1
- Upstream released 2.1.4

* Wed Dec 03 2008 Ray Van Dolson <rayvd@fedoraproject.org> - 2.1.1-1
- New upstream version and homepage

* Mon Jun 02 2008 Ray Van Dolson <rayvd@fedoraproject.org> - 2.0.58-3
- Removed silly python BuildRequires

* Mon Jun 02 2008 Ray Van Dolson <rayvd@fedoraproject.org> - 2.0.58-2
- Added python and python-devel to BuildRequires

* Fri May 30 2008 Ray Van Dolson <rayvd@fedoraproject.org> - 2.0.58-1
- Initial package
