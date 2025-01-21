#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v13
# autospec commit: dc0ff31b4314
#
Name     : perl-Locale-gettext
Version  : 1.07
Release  : 6
URL      : https://cpan.metacpan.org/authors/id/P/PV/PVANDRY/Locale-gettext-1.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/P/PV/PVANDRY/Locale-gettext-1.07.tar.gz
Summary  : 'Perl bindings for POSIX i18n gettext functions'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Locale-gettext-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Locale::gettext
version 1.07
This is a perl5 module quickly written to gain access to
the C library functions for internatialization. They
work just like the C versions.

%package dev
Summary: dev components for the perl-Locale-gettext package.
Group: Development
Provides: perl-Locale-gettext-devel = %{version}-%{release}
Requires: perl-Locale-gettext = %{version}-%{release}

%description dev
dev components for the perl-Locale-gettext package.


%package perl
Summary: perl components for the perl-Locale-gettext package.
Group: Default
Requires: perl-Locale-gettext = %{version}-%{release}

%description perl
perl components for the perl-Locale-gettext package.


%prep
%setup -q -n Locale-gettext-1.07
cd %{_builddir}/Locale-gettext-1.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
# Have to set the lang explicitly to English instead of C so the lookups will work right
LANG=en_US.UTF-8 make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Locale::gettext.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
