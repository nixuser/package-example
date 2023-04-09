Name:           shellspec
Version:        0.28.1
Release:        1%{?dist}
Summary:        BDD unit testing framework for shell

License:        MIT
Source0:        %{name}-%{version}.tar.gz      

Requires:       bash
BuildArch:      noarch

%description
ShellSpec is a full-featured BDD unit testing framework for dash, bash, ksh, zsh and all POSIX shells that provides first-class features such as code coverage, mocking, parameterized test, parallel execution and more.

%prep
%setup -n shellspec

%install
install -d "%{buildroot}/usr/local/bin" "%{buildroot}/usr/local/lib"
find lib libexec -type d -exec install -d "%{buildroot}/usr/local/lib/shellspec/{}" \;
find LICENSE lib -type f -exec install -m 644 {} "%{buildroot}/usr/local/lib/shellspec/{}" \;
find shellspec libexec -type f -exec install {} "%{buildroot}/usr/local/lib/shellspec/{}" \;
install -m 0755 %{name}  %{buildroot}/usr/local/lib/shellspec/


%files
/usr/local/
%license LICENSE

%post
if [ "$1" = 1 ];
then

if   [ -f /usr/local/lib/shellspec/shellspec ] && [ ! -h /usr/local/sbin/shellspec ]
then
    ln -s /usr/local/lib/shellspec/shellspec /usr/local/sbin/
    ln -s /usr/local/lib/shellspec/shellspec /usr/local/bin/
fi

fi


%postun
if [ "$1" = 0 ];
then

if [ -h /usr/local/sbin/%{name} ]
then

unlink /usr/local/sbin/%{name}
unlink /usr/local/bin/%{name}

fi

fi


%changelog
* Sun Apr 09 2023 vagrant
- Remove stub pacakge
- Add symlinks to shellspec
* Wed Mar 22 2023 vagrant
- 
