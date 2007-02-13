Summary:	LibMMS - mms:// and mmsh:// parsing library
Summary(pl.UTF-8):	LibMMS - biblioteka przetwarzająca mms:// i mmsh://
Name:		libmms
Version:	0.3
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/libmms/%{name}-%{version}.tar.gz
# Source0-md5:	1601705f38143687a575630a3f9d6a56
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
%{__make} \
	PKG_LIBS='$(GLIB_LIBS)'

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
%doc AUTHORS ChangeLog README README.LICENSE TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/libmms
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
