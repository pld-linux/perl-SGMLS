%include	/usr/lib/rpm/macros.perl
Summary:	SGMLS - postprocessing the output from the sgmls and nsgmls parsers
#Summary(pl):	
Name:		perl-SGMLS
Version:	1.03ii
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SGMLS/SGMLSpm-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
Obsoletes:	perl-SGMLSpm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains SGMLS.pm, a perl5 class library for parsing
the output from James Clark's SGMLS and NSGMLS parsers.

# %description -l pl
# TODO

%prep
%setup -q -n SGMLSpm
mkdir -p lib/SGMLS
mv Output.pm Refs.pm skel.pl lib/SGMLS
mv SGMLS.pm lib
mv sgmlspl.pl sgmlspl
mv test-SGMLS.pl test.pl

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -wle 'WriteMakefile(NAME=>"SGMLS", EXE_FILES=>["sgmlspl"])' \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README BUGS TODO DOC/*sgml DOC/*pl elisp
%attr(755,root,root) %{_bindir}/*
%{perl_vendorlib}/SGMLS.pm
%{perl_vendorlib}/SGMLS
%{_mandir}/man3/*
