#
# Conditional build:
%bcond_without	unicode	# ANSI instead of Unicode version of wxGTK
%bcond_without	gtk3	# wxGTK3 instead of wxGTK2
%bcond_with	tests	# "make test" (requires $DISPLAY)
#
%define		wxpkg	wxGTK%{?with_gtk3:3}%{!?with_gtk3:2}%{?with_unicode:-unicode}
%define		pdir	Wx
%define		pnam	GLCanvas
Summary:	Wx::GLCanvas - interface to wxWidgets' OpenGL canvas
Summary(pl.UTF-8):	Wx::GLCanvas - interfejs do "płótna" OpenGL biblioteki wxWidgets
Name:		perl-Wx-GLCanvas
Version:	0.09
Release:	13
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Wx/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4f6475010bd6e4231e2dbb3fb52bc642
URL:		http://search.cpan.org/dist/Wx-GLCanvas/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Pluggable
BuildRequires:	perl(Wx::build::MakeMaker) >= 0.16
BuildRequires:	perl-Wx-devel >= 0.57
BuildRequires:	%{wxpkg}-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wx::GLCanvas is an interface to wxWidgets' OpenGL canvas.

%description -l pl.UTF-8
Wx::GLCanvas to interfejs do "płótna" OpenGL biblioteki wxWidgets.

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
%{perl_vendorarch}/Wx/GLCanvas.pm
%dir %{perl_vendorarch}/Wx/DemoModules
%{perl_vendorarch}/Wx/DemoModules/wxGLCanvas.pm
%dir %{perl_vendorarch}/auto/Wx/GLCanvas
%attr(755,root,root) %{perl_vendorarch}/auto/Wx/GLCanvas/GLCanvas.so
%{_mandir}/man3/Wx::GLCanvas.3pm*
