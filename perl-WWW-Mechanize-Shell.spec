%define module  WWW-Mechanize-Shell

Name:		perl-%{module}
Version:	0.46
Release:    %mkrel 5
Summary:	An interactive shell for WWW::Mechanize
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(WWW::Mechanize::FormFiller)
BuildRequires:	perl(HTML::TokeParser::Simple)
BuildRequires:	perl(Term::Shell)
BuildRequires:	perl(Hook::LexWrap)
BuildRequires:	perl(Test::Without::Module)
BuildRequires:	perl(File::Modified)
BuildRequires:	perl(Pod::Constants)
BuildRequires:	perl(Test::Inline)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module implements a www-like shell above WWW::Mechanize
and also has the capability to output crude Perl code that recreates
the recorded session. Its main use is as an interactive starting point
for automating a session through WWW::Mechanize.

%prep
%setup -q -n %{module}-%{version} 

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


