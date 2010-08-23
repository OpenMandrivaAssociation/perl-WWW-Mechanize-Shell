%define upstream_name    WWW-Mechanize-Shell
%define upstream_version 0.50

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	An interactive shell for WWW::Mechanize
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(File::Modified)
BuildRequires:	perl(Hook::LexWrap)
BuildRequires:	perl(HTML::TokeParser::Simple)
BuildRequires:	perl(Pod::Constants)
BuildRequires:	perl(Term::Shell)
BuildRequires:	perl(Test::Inline)
BuildRequires:	perl(Test::Without::Module)
BuildRequires:	perl(WWW::Mechanize::FormFiller)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module implements a www-like shell above WWW::Mechanize
and also has the capability to output crude Perl code that recreates
the recorded session. Its main use is as an interactive starting point
for automating a session through WWW::Mechanize.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

# pod2test is gone in perl-Test-Inline
perl -pi -e "s|pod2test|/bin/true|g" Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

# make test don't work...
#make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Shell.pm
%{_mandir}/*/*
