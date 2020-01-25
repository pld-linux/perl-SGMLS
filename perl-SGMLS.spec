#
# Conditional build:
%bcond_with	tests	# perform "make test"

%define		pdir	SGMLS
Summary:	SGMLS - postprocessing the output from the SGMLS and NSGMLS parsers
Summary(pl.UTF-8):	SGMLS - przetwarzanie wyjścia z analizatorów składni: SGMLS i NSGMLS
Name:		perl-SGMLS
Version:	1.03ii
Release:	15
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SGMLS/SGMLSpm-%{version}.tar.gz
# Source0-md5:	5bcb197fd42e67d51c739b1414d514a7
URL:		http://search.cpan.org/dist/SGMLS-/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-SGMLSpm
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains SGMLS.pm, a perl5 class library for parsing
the output from James Clark's SGMLS and NSGMLS parsers.

%description -l pl.UTF-8
Pakiet ten zawiera bibliotekę klas Perla 5 SGMLS.pm służącą do
przetwarzania wyjścia z analizatorów składniowych SGMLS i NSGMLS
Jamesa Clarka.

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

%{?with_tests:%{__make} test}

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
