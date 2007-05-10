
Summary:	A tool to migrate changesets between several version control systems
Name:		tailor
Version:	0.9.28
Release:	%mkrel 1
Source0:	http://darcs.arstecnica.it/tailor-%{version}.tar.bz2
License:	GPL
Group:		Development/Other
Url:		http://progetti.arstecnica.it/tailor
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
%doc README




