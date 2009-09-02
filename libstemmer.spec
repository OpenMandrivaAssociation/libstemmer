%define	major 0
%define libname %mklibname stemmer %{major}
%define develname %mklibname stemmer -d

Summary:	The C version of the libstemmer library
Name:		libstemmer
Version:	0
Release:	%mkrel 7
Group:		System/Libraries
License:	BSD
URL:		http://snowball.tartarus.org/
Source0:	http://snowball.tartarus.org/dist/libstemmer_c.tgz
Patch0:		libstemmer-libtool.diff
BuildRequires:	libtool
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n	%{develname}
Summary:	Static library and header files for the libstemmer library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname stemmer 0 -d}

%description -n	%{develname}
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

# voodoo magic
LDFLAGS=`rpm --eval %%configure|grep LDFLAGS|cut -d\" -f2`
perl -pi -e "s|^LDFLAGS.*|LDFLAGS = $LDFLAGS|g" Makefile

%make CFLAGS="%{optflags} -Wall -Iinclude -fPIC -DPIC -D_REENTRANT"

%install
rm -rf %{buildroot}

%makeinstall_std

# install referenced headers
install -m0644 src_c/stem_*.h %{buildroot}%{_includedir}/%{name}/

# fix location
perl -pi -e "s|\.\./src_c/||g" %{buildroot}%{_includedir}/%{name}/modules.h

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc README
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la

%files -n stemwords
%defattr(-,root,root)
%{_bindir}/stemwords
