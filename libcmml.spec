%define	major 1
%define libname %mklibname cmml %{major}
%define develname %mklibname cmml -d

Summary:	Library for handling Continuous Media Markup Language
Name:		libcmml
Version:	0.9.4
Release:	6
Group:		System/Libraries
License:	BSD
URL:		https://www.annodex.net/
Source0:	https://www.annodex.net/software/libcmml/download/%{name}-%{version}.tar.gz
Patch0:		libcmml-malloc_fix.diff
BuildRequires:	doxygen
BuildRequires:	expat-devel
BuildRequires:	autoconf2.5
BuildRequires:	libtool

%description
Libcmml is a library which enables the handling of documents written in CMML
(Continuous Media Markup Language) for the Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the Continuous
Media Markup Language (CMML), and returns C structures containing this
information in a format which can be used by an Annodexer for creating
ANNODEX(tm) format documents (ANX).

%package -n	%{libname}
Summary:	Library for handling Continuous Media Markup Language
Group:          System/Libraries

%description -n	%{libname}
Libcmml is a library which enables the handling of documents written in CMML
(Continuous Media Markup Language) for the Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the Continuous
Media Markup Language (CMML), and returns C structures containing this
information in a format which can be used by an Annodexer for creating
ANNODEX(tm) format documents (ANX).

%files -n %{libname}
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

#----------------------------------------------------------------------------

%package -n	%{develname}
Summary:	Files needed for development using libcmml
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname cmml 1 -d}

%description -n	%{develname}
Libcmml is a library which enables the handling of documents written in CMML
(Continuous Media Markup Language) for the Continuous Media Web (CMWeb).

It provides a very simple API for reading files marked up with the Continuous
Media Markup Language (CMML), and returns C structures containing this
information in a format which can be used by an Annodexer for creating
ANNODEX(tm) format documents (ANX).

This package contains the header files and documentation needed for development
using libcmml.

%files -n %{develname}
%doc doc/libcmml/html/* TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/pkgconfig/cmml.pc

#----------------------------------------------------------------------------

%package	tools
Summary:	Various tools using the Continuous Media Markup Language library
Group:          File tools

%description	tools
Libcmml is a library which enables the handling of documents written in CMML
(Continuous Media Markup Language) for the Continuous Media Web (CMWeb).

This package contains various tools using the Continuous Media Markup Language
library.

%files tools
%{_bindir}/cmml*
%{_mandir}/man1/*
%{_mandir}/man6/*

#----------------------------------------------------------------------------

%prep
%autosetup -p0 -n %{name}-%{version}

%build
%config_update
%configure
%make_build

%check
make check

%install
%make_install

install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man6

install -m0644 doc/*.1 %{buildroot}%{_mandir}/man1/
install -m0644 doc/*.6 %{buildroot}%{_mandir}/man6/

# cleanup
rm -rf %{buildroot}%{_docdir}/libcmml

%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-3mdv2011.0
+ Revision: 620087
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.9.4-2mdv2010.0
+ Revision: 429718
- rebuild

* Sat Jun 28 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.4-1mdv2009.0
+ Revision: 229596
- 0.9.4
- added P0 to make it build with gcc43

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-2mdv2008.0
+ Revision: 83598
- new devel naming


* Sat Dec 09 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-1mdv2007.0
+ Revision: 94064
- Import libcmml

* Mon Aug 07 2006 Oden Eriksson <oeriksson@mandriva.com> 0.9.2-1mdv2007.0
- initial Mandriva package (fc5 extras import)

