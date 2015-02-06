%define upstream_name    WWW-Mechanize-Shell
%define upstream_version 0.53

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	An interactive shell for WWW::Mechanize
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/WWW/WWW-Mechanize-Shell-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(File::Modified)
BuildRequires:	perl(Hook::LexWrap)
BuildRequires:	perl(HTML::TokeParser::Simple)
BuildRequires:	perl(Pod::Constants)
BuildRequires:	perl(Term::Shell)
BuildRequires:	perl(Test::Inline)
BuildRequires:	perl(Test::Without::Module)
BuildRequires:	perl(WWW::Mechanize::FormFiller)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# make test don't work...
#make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/WWW/Mechanize/Shell.pm
%{_mandir}/*/*


%changelog
* Fri Jan 07 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.520.0-1mdv2011.0
+ Revision: 629502
- update to new version 0.52

* Mon Aug 23 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.500.0-1mdv2011.0
+ Revision: 572243
- update to 0.50

* Mon Aug 03 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.480.0-1mdv2010.0
+ Revision: 408100
- rebuild using %%perl_convert_version

* Mon Nov 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.48-1mdv2009.1
+ Revision: 301685
- update to new version 0.48

* Mon Nov 03 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.47-1mdv2009.1
+ Revision: 299406
- update to new version 0.47

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.46-5mdv2009.0
+ Revision: 258792
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.46-4mdv2009.0
+ Revision: 246714
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Nov 17 2007 Funda Wang <fwang@mandriva.org> 0.46-2mdv2008.1
+ Revision: 109345
- rebuild

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.46-1mdv2008.1
+ Revision: 105434
- new version

* Mon Jul 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.44-1mdv2008.0
+ Revision: 52528
- update to new version 0.44

* Mon Jul 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.43-1mdv2008.0
+ Revision: 46894
- 0.43

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 0.42-1mdv2008.0
+ Revision: 20748
- 0.42


* Sun Dec 24 2006 Olivier Thauvin <nanardon@mandriva.org> 0.39-1mdv2007.0
+ Revision: 101958
- 0.39
- Import perl-WWW-Mechanize-Shell

* Sat Apr 29 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.36-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Thu Jul 21 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.36-1mdk
- 0.36

* Sat Jul 16 2005 Oden Eriksson <oeriksson@mandriva.com> 0.34-1mdk
- initial Mandriva package


