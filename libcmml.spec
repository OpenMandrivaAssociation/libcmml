%define	major 1
%define libname %mklibname cmml %{major}
%define develname %mklibname cmml -d

Summary:	Library for handling Continuous Media Markup Language
Name:		libcmml
Version:	0.9.2
Release:	%mkrel 2
Group:		System/Libraries
License:	BSD
URL:		http://www.annodex.net/
Source0:	http://www.annodex.net/software/libcmml/download/%{name}-%{version}.tar.bz2
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

%package	tools
Summary:	Various tools using the Continuous Media Markup Language library
Group:          File tools

%description	tools
Libcmml is a library which enables the handling of documents written in CMML
(Continuous Media Markup Language) for the Continuous Media Web (CMWeb).

This package contains various tools using the Continuous Media Markup Language
library.

%prep

%setup -q -n %{name}-%{version}

%build

%configure2_5x

%make

%check
make check

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

install -d %{buildroot}%{_mandir}/man1
install -d %{buildroot}%{_mandir}/man6

install -m0644 doc/*.1 %{buildroot}%{_mandir}/man1/
install -m0644 doc/*.6 %{buildroot}%{_mandir}/man6/


# cleanup
rm -rf %{buildroot}%{_docdir}/libcmml

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
                                                                                
%files -n %{libname}
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc doc/libcmml/html/* TODO
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/cmml.pc

%files tools
%defattr(-,root,root)
%{_bindir}/cmml*
%{_mandir}/man1/*
%{_mandir}/man6/*
