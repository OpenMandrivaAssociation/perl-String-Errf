%define upstream_name    String-Errf
%define upstream_version 0.006

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A simple sprintf-like dialect
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/String/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Carp)
BuildRequires: perl(Date::Format)
BuildRequires: perl(JSON)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(String::Formatter)
BuildRequires: perl(Sub::Exporter)
BuildRequires: perl(Test::More) >= 0.960.0
BuildRequires: perl(Time::Piece)
BuildRequires: perl(autodie)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
String::Errf provides 'errf', a simple string formatter that works
something like 'perlfunc/sprintf'. It is implemented using the
String::Formatter manpage and the Sub::Exporter manpage. Their
documentation may be useful in understanding or extending String::Errf.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%perl_vendorlib/*


