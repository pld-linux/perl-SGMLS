%include	/usr/lib/rpm/macros.perl
Summary:	SGMLS perl module
Summary(pl):	Modu³ perla SGMLS
Name:		perl-SGMLS
Version:	1.03ii
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(cs):	Vývojové prostøedky/Programovací jazyky/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(es):	Desarrollo/Lenguajes/Perl
Group(fr):	Development/Langues/Perl
Group(ja):	³«È¯/¸À¸ì/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Group(pt):	Desenvolvimento/Linguagens/Perl
Group(ru):	òÁÚÒÁÂÏÔËÁ/ñÚÙËÉ/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/SGMLS/SGMLSpm-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-18
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SGMLS perl module.

%description -l pl
Modu³ perla SGMLS.

%prep
%setup -q -n SGMLSpm

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man3,%{perl_sitelib}/SGMLS}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	PERL5DIR=$RPM_BUILD_ROOT%{perl_sitelib} \
	SPECDIR=$RPM_BUILD_ROOT%{perl_sitelib}/SGMLS

pod2man SGMLS.pm  > $RPM_BUILD_ROOT%{_mandir}/man3/SGMLS.3pm
pod2man Output.pm > $RPM_BUILD_ROOT%{_mandir}/man3/SGMLS::Output.3pm
pod2man Refs.pm   > $RPM_BUILD_ROOT%{_mandir}/man3/SGMLS::Refs.3pm

gzip -9nf ChangeLog README BUGS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz DOC/*sgml DOC/*pl elisp
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/SGMLS.pm
%{perl_sitelib}/SGMLS
%{_mandir}/man3/*
