%define upstream_name    String-Errf
%define upstream_version 0.009

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	A simple sprintf-like dialect
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/rjbs/String-Errf
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/String-Errf-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Carp)
BuildRequires:	perl(Date::Format)
BuildRequires:	perl(JSON)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(String::Formatter)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::More) >= 0.960.0
BuildRequires:	perl(Time::Piece)
BuildRequires:	perl(autodie)
BuildArch:	noarch

%description
String::Errf provides 'errf', a simple string formatter that works
something like 'perlfunc/sprintf'. It is implemented using the
String::Formatter manpage and the Sub::Exporter manpage. Their
documentation may be useful in understanding or extending String::Errf.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes LICENSE META.yml META.json
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.6.0-2mdv2011.0
+ Revision: 657467
- rebuild for updated spec-helper

* Sun Feb 20 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.0-1
+ Revision: 638974
- import perl-String-Errf


