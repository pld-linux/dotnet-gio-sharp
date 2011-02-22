#
%include	/usr/lib/rpm/macros.mono
#
Summary:	.NET language bindings for GIO
Summary(pl.UTF-8):	Wiązania GIO dla .NET
Name:		dotnet-gio-sharp
Version:	0.2
Release:	2
License:	MIT
Group:		Libraries
Source0:	gio-sharp-%{version}.tar.gz
# Source0-md5:	57b0189de1f43e90f795e0213500e807
URL:		http://github.com/mono/gio-sharp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-gtk-sharp2-devel
BuildRequires:	glib2-devel >= 1:2.22.0
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(monoautodeps)
Requires:	glib2 >= 1:2.22.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides bindings for .NET to GIO library.

%description -l pl.UTF-8
Pakiet ten dostarcza wiązania dla .NET do biblioteki z GIO.

%package devel
Summary:	GIO# development files
Summary(pl.UTF-8):	Pliki programistyczne GIO#
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dotnet-gtk-sharp2-devel

%description devel
GIO# development files.

%description devel -l pl.UTF-8
Pliki programistyczne GIO#.

%prep
%setup -q -n mono-gio-sharp-017c8a5

%build
NOCONFIGURE=true ./autogen-2.22.sh
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_prefix}/lib/gio-sharp

%files devel
%defattr(644,root,root,755)
%{_datadir}/gapi-2.0/gio-api.xml
%{_pkgconfigdir}/gio-sharp-2.0.pc
