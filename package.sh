#!/bin/bash
yum install -y rpmdevtools
rpmdev-setuptree
cp shellspec-0.28.1.tar.gz ~/rpmbuild/SOURCES
cp shellspec.spec ~/rpmbuild/SPECS/
rpmbuild -ba ~/rpmbuild/SPECS/shellspec.spec
cp /root/rpmbuild/RPMS/noarch/shellspec-0.28.1-1.el9.noarch.rpm ./
