%define	major	0
%define	libname	%mklibname stemmer %{major}
%define devname	%mklibname stemmer -d

Summary:	The C version of the libstemmer library
Name:		libstemmer
Version:	0
Release:	15
Group:		System/Libraries
License:	BSD
Url:		http://snowball.tartarus.org/
Source0:	http://snowball.tartarus.org/dist/libstemmer_c.tgz
Patch0:		libstemmer-libtool.diff
BuildRequires:	libtool

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

%package -n	%{devname}
Summary:	Development library and header files for the libstemmer library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} >= %{version}-%{release}
Obsoletes:	%{mklibname stemmer 0 -d}

%description -n	%{devname}
This package contains the development files for %{name}.

%package -n	stemwords
Summary:	The stemwords utility using the libstemmer library
Group:          System/Libraries

%description -n	stemwords
The stemwords utility using the libstemmer library

%prep
%setup -qn libstemmer_c
%patch0 -p0

# lib64 fix
sed -i -e "s|/usr/lib|%{_libdir}|g" Makefile

%build
%make LDFLAGS="%{ldflags}" CFLAGS="%{optflags} -Wall -Iinclude -fPIC -DPIC -D_REENTRANT"

%install
%makeinstall_std

# install referenced headers
install -m644 src_c/stem_*.h %{buildroot}%{_includedir}/%{name}/

# fix location
perl -pi -e "s|\.\./src_c/||g" %{buildroot}%{_includedir}/%{name}/modules.h

%files -n %{libname}
%doc README
%{_libdir}/libstemmer.so.%{major}*

%files -n %{devname}
%dir %{_includedir}/%{name}
%{_includedir}/%{name}/*.h
%{_libdir}/libstemmer.so

%files -n stemwords
%{_bindir}/stemwords

