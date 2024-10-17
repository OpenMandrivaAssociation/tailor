
Summary:	A tool to migrate changesets between several version control systems
Name:		tailor
Version:	0.9.35
Release:	5
Source0:	http://darcs.arstecnica.it/tailor-%{version}.tar.gz
License:	GPL
Group:		Development/Other
Url:		https://progetti.arstecnica.it/tailor
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
Requires:	python
Provides:	python-vcpx = %{version}-%{release}
Obsoletes:	python-vcpx
BuildArch:	noarch

%description
Tailor is a tool to migrate changesets between CVS, Subversion,
darcs, monotone, Codeville, Mercurial and Baazar-NG [#]
repositories.

This script makes it easier to keep the upstream changes merged in
a branch of a product, storing needed information such as the upstream
URI and revision in special properties on the branched directory.

[#] Monotone, Codeville, Mercurial and Baazar-NG systems may be
used only as the `target` backend, since the `source` support
isn't coded yet. Contributions on these backends will be very
appreciated, since I do not use them enough to figure out the
best way to get pending changes and build tailor ChangeSets out
of them.

%prep
%setup -q 

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root,0755)
%{_bindir}/*
%{py_puresitedir}/vcpx
%{py_puresitedir}/*.egg-info
#%{_mandir}/man*/*
%doc README.rst






%changelog
* Tue Nov 02 2010 Michael Scherer <misc@mandriva.org> 0.9.35-4mdv2011.0
+ Revision: 592361
- rebuild for python 2.7

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.9.35-3mdv2010.0
+ Revision: 445347
- rebuild

* Mon Dec 29 2008 Crispin Boylan <crisb@mandriva.org> 0.9.35-2mdv2009.1
+ Revision: 321198
- Rebuild for python 2.6

* Mon Sep 01 2008 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.35-1mdv2009.0
+ Revision: 278326
- * New release 0.9.35

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.9.30-4mdv2009.0
+ Revision: 261368
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.9.30-3mdv2009.0
+ Revision: 254082
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 28 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.30-1mdv2008.1
+ Revision: 138837
- update to new version 0.9.30

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Jul 24 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.29-1mdv2008.0
+ Revision: 55062
- 0.9.29

* Thu May 10 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.28-1mdv2008.0
+ Revision: 25947
- 0.9.28


* Sat Dec 16 2006 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.27-1mdv2007.0
+ Revision: 98178
- 0.9.27

* Sat Dec 09 2006 Michael Scherer <misc@mandriva.org> 0.9.26-2mdv2007.1
+ Revision: 94199
- Rebuild for new python
- Use better macros

* Fri Aug 18 2006 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.26-1mdv2007.0
+ Revision: 56600
- update to 0.9.26

* Fri Aug 11 2006 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.23-1mdv2007.0
+ Revision: 55350
- update ot 0.9.23

* Thu Aug 10 2006 Gaëtan Lehmann <glehmann@mandriva.org> 0.9.22-2mdv2007.0
+ Revision: 55165
- rebuild
- Import tailor

* Sun May 07 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.9.22-1mdk
- 0.9.22
- noarch
- update url

* Sun Jan 15 2006 Olivier Thauvin <nanardon@mandriva.org> 0.9.19-3mdk
- no longer noarch and use macro for lib path to avoid breakage of python
  with its "noarch" files
- remove empty %%build 
[           1      -eq 1 ] || exit 0 
[           1      -eq 1 ] || exit 0 
 section

* Sat Dec 03 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.9.19-2mdk
- drop python-vcpx package

* Thu Nov 10 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.9.19-1mdk
- New release 0.9.19

* Fri Oct 21 2005 Nicolas L�cureuil <neoclust@mandriva.org> 0.9.18-2mdk
- Fix BuildRequires
- fix tomdv2007.1

* Tue Oct 18 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.9.18-1mdk
- New release 0.9.18

* Fri Oct 07 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.9.17-1mdk
- New release 0.9.17

* Fri Jul 29 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.8-1mdk
- 0.8
- update description and summary

* Thu Apr 21 2005 Gaetan Lehmann <glehmann@n4.mandrakesoft.com> 0-0.20050420.1mdk
- darcs pull
- create link tailor -> tailor.py

* Tue Mar 22 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0-0.20050301.1mdk
- mandrake contrib

