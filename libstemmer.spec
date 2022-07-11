%define major 0
%define libname %mklibname stemmer %{major}
%define devname %mklibname stemmer -d

%define snapshot 20200123

Summary:	The C version of the libstemmer library
Name:		libstemmer
Version:	2.2.0
Release:	1
License:	BSD
Group:		System/Libraries
Url:		http://snowballstem.org/
# libstemmer tarball generated with following commands
# git clone https://github.com/snowballstem/snowball.git
# cd snowball && make dist_libstemmer_c
# cd dist && mv libstemmer_c.tgz libstemmer_c-SNAPDATE.tar.gz
Source0:	http://snowball.tartarus.org/dist/libstemmer_c-%{snapshot}.tar.gz
Patch0:		libstemmer-libtool.diff
BuildRequires:	libtool

%description
Snowball is a small string processing language designed for
creating stemming algorithms for use in Information Retrieval.
This site describes Snowball, and presents several useful stemmers
which have been implemented using it.

This package containst the C version of the libstemmer library.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	The C version of the libstemmer library
Group:		System/Libraries

%description -n %{libname}
Snowball is a small string processing language designed for
creating stemming algorithms for use in Information Retrieval.
This site describes Snowball, and presents several useful stemmers
which have been implemented using it.

This package containst the C version of the libstemmer library.

%files -n %{libname}
%{_libdir}/libstemmer.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development library and header files for the libstemmer library
Group:		Development/C
Requires:	%{libname} >= %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devname}
This package contains the development files for %{name}.

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libstemmer.so

#----------------------------------------------------------------------------

%package -n stemwords
Summary:	The stemwords utility using the libstemmer library
Group:		System/Libraries
Requires:	%{libname} >= %{EVRD}

%description -n stemwords
The stemwords utility using the libstemmer library.

%files -n stemwords
%{_bindir}/stemwords

#----------------------------------------------------------------------------

%prep
%autosetup -p1 -n libstemmer_c

# lib64 fix
sed -i -e "s|/usr/lib|%{_libdir}|g" Makefile

%build
%make CC=%{__cc} LDFLAGS="%{ldflags}" CFLAGS="%{optflags} -O3 -Wall -Iinclude -fPIC -DPIC -D_REENTRANT"

%install
%makeinstall_std

# install referenced headers
install -m644 src_c/stem_*.h %{buildroot}%{_includedir}/%{name}/

# fix location
sed -i -e "s|\.\./src_c/||g" %{buildroot}%{_includedir}/%{name}/modules.h

# we don't want these
find %{buildroot} -name "*.la" -delete
find %{buildroot} -name '*.a' -delete
