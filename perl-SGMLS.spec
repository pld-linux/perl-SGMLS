%include	/usr/lib/rpm/macros.perl
Summary:	SGMLS - postprocessing the output from the sgmls and nsgmls parsers
Summary(pl):	SGMLS - przetwarzanie wyj¶cia z analizatorów sk³adni: sgmls i nsgmls
Name:		perl-SGMLS
Version:	1.03ii
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/SGMLS/SGMLSpm-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution contains SGMLS.pm, a perl5 class library for parsing
the output from James Clark's SGMLS and NSGMLS parsers.

%description -l pl
Pakiet ten zawiera bibliotekê klas Perla 5 SGMLS.pm s³u¿±c± do
przetwarzania wyj¶cia z analizatorów sk³adniowych SGMLS i NSGMLS
Jamesa Clarka.

%prep
%setup -q -n SGMLSpm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man3,%{perl_sitelib}/SGMLS}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	PERL5DIR=$RPM_BUILD_ROOT%{perl_sitelib} \
	SPECDIR=$RPM_BUILD_ROOT%{perl_sitelib}/SGMLS

pod2man --section=3pm SGMLS.pm  > $RPM_BUILD_ROOT%{_mandir}/man3/SGMLS.3pm
pod2man --section=3pm Output.pm > $RPM_BUILD_ROOT%{_mandir}/man3/SGMLS::Output.3pm
pod2man --section=3pm Refs.pm   > $RPM_BUILD_ROOT%{_mandir}/man3/SGMLS::Refs.3pm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README BUGS TODO DOC/*sgml DOC/*pl elisp
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/SGMLS.pm
%{perl_sitelib}/SGMLS
%{_mandir}/man3/*
