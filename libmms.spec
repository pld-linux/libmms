Summary:	LibMMS - mms:// and mmsh:// parsing library
Summary(pl.UTF-8):	LibMMS - biblioteka przetwarzająca mms:// i mmsh://
Name:		libmms
Version:	0.6.2
Release:	2
License:	LGPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libmms/%{name}-%{version}.tar.gz
# Source0-md5:	9f63aa363deb4874e072a45850161bff
URL:		http://sourceforge.net/projects/libmms/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibMMS is mms:// and mmsh:// (Microsoft streaming protocols) parsing
library.

%description -l pl.UTF-8
LibMMS to biblioteka przetwarzająca mms:// i mmsh:// (protokoły
strumieni Microsoftu).

%package devel
Summary:	Header files for libmms library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libmms
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 2.0.0

%description devel
Header files for libmms library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libmms.

%package static
Summary:	Static libmms library
Summary(pl.UTF-8):	Statyczna biblioteka libmms
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libmms library.

%description static -l pl.UTF-8
Statyczna biblioteka libmms.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README README.LICENSE
%attr(755,root,root) %{_libdir}/libmms.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmms.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmms.so
%{_libdir}/libmms.la
%{_includedir}/libmms
%{_pkgconfigdir}/libmms.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libmms.a
