# $Id$

# Authority: dries
# Upstream: Jos Boumans <gro,miwd$enak>

%define real_name Object-Accessor
%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

Summary: Interface to create per object accessors
Name: perl-Object-Accessor
Version: 0.03
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Object-Accessor/

Packager: Dries Verachtert <dries@ulyssis.org>
Vendor: Dries Apt/Yum Repository http://dries.ulyssis.org/ayo/

Source: http://search.cpan.org/CPAN/authors/id/K/KA/KANE/Object-Accessor-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
Object::Accessor provides an interface to create per object 
accessors (as opposed to per Class accessors, as, for example,
Class::Accessor> provides.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX=%{buildroot}%{_prefix}
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
%doc %{_mandir}/man3/*
%{perl_vendorlib}/Object/Accessor.pm

%changelog
* Thu Mar 31 2005 Dries Verachtert <dries@ulyssis.org> - 0.03-1
- Initial package.
