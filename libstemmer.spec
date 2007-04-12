%define	major 0
%define libname	%mklibname stemmer %{major}

Summary:	The C version of the libstemmer library
Name:		libstemmer
Version:	0
Release:	%mkrel 1
Group:		System/Libraries
License:	BSD
URL:		http://snowball.tartarus.org/
Source0:	http://snowball.tartarus.org/dist/libstemmer_c.tar.bz2
Patch0:		libstemmer-libtool.diff
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Snowball is a small string processing language designed for
creating stemming algorithms for use in Information Retrieval.
This site describes Snowball, and presents several useful stemmers
which have been implemented using it.

This package containst the C version of the libstemmer library.

%package -n	%{libname}
Summary:	The C version of the libstemmer library
Group:          System/Libraries

%description -n	%{libname}
Snowball is a small string processing language designed for
creating stemming algorithms for use in Information Retrieval.
This site describes Snowball, and presents several useful stemmers
which have been implemented using it.

This package containst the C version of the libstemmer library.

%package -n	%{libname}-devel
Summary:	Static library and header files for the libevent library
Group:		Development/C
Provides:	%{name}-devel
Provides:	lib%{name}-devel
Requires:	%{libname} = %{version}

%description -n	%{libname}-devel
Snowball is a small string processing language designed for
creating stemming algorithms for use in Information Retrieval.
This site describes Snowball, and presents several useful stemmers
which have been implemented using it.

This package contains the static libstemmer library and its header
files.

%package -n	stemwords
Summary:	The stemwords utility using the libstemmer library
Group:          System/Libraries

%description -n	stemwords
The stemwords utility using the libstemmer library

%prep

%setup -q -n libstemmer_c
%patch0 -p0

# lib64 fix
perl -pi -e "s|/usr/lib|%{_libdir}|g" Makefile

%build

%make CFLAGS="%{optflags} -Wall -Iinclude -fPIC -DPIC -D_REENTRANT"

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/*.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

%files -n stemwords
%defattr(-,root,root)
%{_bindir}/stemwords


