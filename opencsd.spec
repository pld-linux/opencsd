Summary:	OpenCSD - open source CodeSight Trace Decode library
Summary(pl.UTF-8):	OpenCSD - mająca otwarte źródła biblioteka dekodowania śladów CodeSight
Name:		opencsd
Version:	0.12.0
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/Linaro/OpenCSD/releases
Source0:	https://github.com/Linaro/OpenCSD/archive/v%{version}/OpenCSD-%{version}.tar.gz
# Source0-md5:	3094532ae3bfccc4c285132ab7ccb99c
URL:		https://github.com/Linaro/OpenCSD
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenCSD is an open source ARM(R) CoreSight(TM) Trace Decode library.

%description -l pl.UTF-8
OpenCSD to mająca otwarte źródła biblioteka do dekodowania śladów
ARM(R) CoreSight(TM).

%package devel
Summary:	Header files for OpenCSD library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki OpenCSD
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel >= 6:4.7

%description devel
Header files for OpenCSD library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki OpenCSD.

%package static
Summary:	Static OpenCSD library
Summary(pl.UTF-8):	Statyczna biblioteka OpenCSD
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static OpenCSD library.

%description static -l pl.UTF-8
Statyczna biblioteka OpenCSD.

%prep
%setup -q -n OpenCSD-%{version}

%build
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
%{__make} -C decoder/build/linux

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C decoder/build/linux install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix} \
	LIB_PATH=%{_lib}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc HOWTO.md LICENSE README.md TODO
%attr(755,root,root) %{_bindir}/trc_pkt_lister
%attr(755,root,root) %{_libdir}/libopencsd.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopencsd.so.0
%attr(755,root,root) %{_libdir}/libopencsd_c_api.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libopencsd_c_api.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libopencsd.so
%attr(755,root,root) %{_libdir}/libopencsd_c_api.so
%{_includedir}/opencsd

%files static
%defattr(644,root,root,755)
%{_libdir}/libopencsd.a
%{_libdir}/libopencsd_c_api.a
