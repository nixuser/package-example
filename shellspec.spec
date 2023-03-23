Name:           shellspec
Version:        0.28.1
Release:        1%{?dist}
Summary:        BDD unit testing framework for shell

License:        MIT
Source0:        %{name}-%{version}.tar.gz      
Source1:        stub.tar.gz      

Requires:       bash
BuildArch:      noarch

%description
ShellSpec is a full-featured BDD unit testing framework for dash, bash, ksh, zsh and all POSIX shells that provides first-class features such as code coverage, mocking, parameterized test, parallel execution and more.

%prep
%setup -n shellspec -a 1

%install
install -d "%{buildroot}/usr/local/bin" "%{buildroot}/usr/local/lib"
install -m 0755 %{name}  %{buildroot}/usr/local/bin
install stub/shellspec "%{buildroot}/usr/local/bin/shellspec"
find lib libexec -type d -exec install -d "%{buildroot}/usr/local/lib/shellspec/{}" \;
find LICENSE lib -type f -exec install -m 644 {} "%{buildroot}/usr/local/lib/shellspec/{}" \;
find shellspec libexec -type f -exec install {} "%{buildroot}/usr/local/lib/shellspec/{}" \;


%files
/usr/local/
#/usr/libexec/shellspec/
%license LICENSE


%changelog
* Wed Mar 22 2023 vagrant
- 
