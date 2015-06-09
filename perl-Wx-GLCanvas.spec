#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Wx
%define		pnam	GLCanvas
%include	/usr/lib/rpm/macros.perl
Summary:	Wx::GLCanvas - interface to wxWidgets' OpenGL canvas
Name:		perl-Wx-GLCanvas
Version:	0.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Wx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f6475010bd6e4231e2dbb3fb52bc642
URL:		http://search.cpan.org/dist/Wx-GLCanvas/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Wx::build::MakeMaker) >= 0.16
BuildRequires:	perl-Wx >= 0.57
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The documentation for this module is included in the main
wxPerl distribution (wxGLCanvas).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cxx}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.txt
%{perl_vendorarch}/Wx/*.pm
%dir %{perl_vendorarch}/Wx/DemoModules
%{perl_vendorarch}/Wx/DemoModules/wxGLCanvas.pm
%dir %{perl_vendorarch}/auto/Wx/GLCanvas
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/GLCanvas/*.so
%{_mandir}/man3/*
