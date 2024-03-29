#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : unixODBC
Version  : 2.3.12
Release  : 6
URL      : ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.12.tar.gz
Source0  : ftp://ftp.unixodbc.org/pub/unixODBC/unixODBC-2.3.12.tar.gz
Summary  : unixODBC Driver Manager library
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: unixODBC-bin = %{version}-%{release}
Requires: unixODBC-lib = %{version}-%{release}
Requires: unixODBC-license = %{version}-%{release}
Requires: unixODBC-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : flex
BuildRequires : readline-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
+-------------------------------------------------------------+
| unixODBC                                                    |
+-------------------------------------------------------------+

%package bin
Summary: bin components for the unixODBC package.
Group: Binaries
Requires: unixODBC-license = %{version}-%{release}

%description bin
bin components for the unixODBC package.


%package dev
Summary: dev components for the unixODBC package.
Group: Development
Requires: unixODBC-lib = %{version}-%{release}
Requires: unixODBC-bin = %{version}-%{release}
Provides: unixODBC-devel = %{version}-%{release}
Requires: unixODBC = %{version}-%{release}

%description dev
dev components for the unixODBC package.


%package lib
Summary: lib components for the unixODBC package.
Group: Libraries
Requires: unixODBC-license = %{version}-%{release}

%description lib
lib components for the unixODBC package.


%package license
Summary: license components for the unixODBC package.
Group: Default

%description license
license components for the unixODBC package.


%package man
Summary: man components for the unixODBC package.
Group: Default

%description man
man components for the unixODBC package.


%prep
%setup -q -n unixODBC-2.3.12
cd %{_builddir}/unixODBC-2.3.12
pushd ..
cp -a unixODBC-2.3.12 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692123986
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1692123986
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/unixODBC
cp %{_builddir}/unixODBC-%{version}/COPYING %{buildroot}/usr/share/package-licenses/unixODBC/a4e796952ca80385ca199ae5a9d4b43ca63d81d2 || :
cp %{_builddir}/unixODBC-%{version}/exe/COPYING %{buildroot}/usr/share/package-licenses/unixODBC/41f867b9ac89aebe3dfc7fd10fe97bde3663030d || :
cp %{_builddir}/unixODBC-%{version}/libltdl/COPYING.LIB %{buildroot}/usr/share/package-licenses/unixODBC/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/dltest
/V3/usr/bin/isql
/V3/usr/bin/iusql
/V3/usr/bin/odbc_config
/V3/usr/bin/odbcinst
/V3/usr/bin/slencheck
/usr/bin/dltest
/usr/bin/isql
/usr/bin/iusql
/usr/bin/odbc_config
/usr/bin/odbcinst
/usr/bin/slencheck

%files dev
%defattr(-,root,root,-)
/usr/include/autotest.h
/usr/include/odbcinst.h
/usr/include/odbcinstext.h
/usr/include/sql.h
/usr/include/sqlext.h
/usr/include/sqlspi.h
/usr/include/sqltypes.h
/usr/include/sqlucode.h
/usr/include/unixODBC/unixodbc_conf.h
/usr/include/unixodbc.h
/usr/include/uodbc_extras.h
/usr/include/uodbc_stats.h
/usr/lib64/libodbc.so
/usr/lib64/libodbccr.so
/usr/lib64/libodbcinst.so
/usr/lib64/pkgconfig/odbc.pc
/usr/lib64/pkgconfig/odbccr.pc
/usr/lib64/pkgconfig/odbcinst.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libodbc.so.2.0.0
/V3/usr/lib64/libodbccr.so.2.0.0
/V3/usr/lib64/libodbcinst.so.2.0.0
/usr/lib64/libodbc.so.2
/usr/lib64/libodbc.so.2.0.0
/usr/lib64/libodbccr.so.2
/usr/lib64/libodbccr.so.2.0.0
/usr/lib64/libodbcinst.so.2
/usr/lib64/libodbcinst.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/unixODBC/01a6b4bf79aca9b556822601186afab86e8c4fbf
/usr/share/package-licenses/unixODBC/41f867b9ac89aebe3dfc7fd10fe97bde3663030d
/usr/share/package-licenses/unixODBC/a4e796952ca80385ca199ae5a9d4b43ca63d81d2

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dltest.1
/usr/share/man/man1/isql.1
/usr/share/man/man1/iusql.1
/usr/share/man/man1/odbc_config.1
/usr/share/man/man1/odbcinst.1
/usr/share/man/man5/odbc.ini.5
/usr/share/man/man5/odbcinst.ini.5
/usr/share/man/man7/unixODBC.7
