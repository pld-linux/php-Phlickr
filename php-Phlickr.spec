# TODO:
#  - this isn't a PEAR package - it's merely PEAR compatible,
#    maybe we should keep these somewhere outside PEAR tree?
%include	/usr/lib/rpm/macros.php
%define		_status		beta
%define		_pearname	Phlickr
Summary:	%{_pearname} - Access the Flickr API (PHP 5)
Summary(pl):	%{_pearname} - Dostêp do API Flickr (PHP 5)
Name:		php-%{_pearname}
Version:	0.2.6
Release:	1
Epoch:		0
License:	LGPL
Group:		Development/Languages/PHP
Source0:	http://dl.sourceforge.net/phlickr/%{_pearname}-%{version}.tgz
# Source0-md5:	66ae0b934d5ccbf88c175dce5f6d3781
URL:		http://phlickr.sourceforge.net/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-common >= 4:5.0.0
Requires:	php-curl
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(PHPUnit2.*)'

%description
Phlickr is a PHP5 library designed to wrap the web service API
provided by Flickr, a web based photo storage service. Phlickr
requires that PHP5 be compiled with the CURL and SimpleXML extensions.

Status of this package is: %{_status}.

%description -l pl
Phlickr to biblioteka dla PHP5 zaprojektowana by "opakowaæ" API us³ug
sieciowych dostarczonych przez serwis zdjêæ online Flickr. Phlickr
korzysta z rozszerzeñ CURL oraz SimpleXML.

Ta klasa ma status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	php-pear-PHPUnit2
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Phlickr

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Phlickr
