#!/bin/bash

sudo yum install -y rpmdevtools rpmlint

rpmdev-setuptree
# Repository contains binary files, so install git lfs
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.rpm.sh | sudo bash
sudo yum -y install git-lfs

git clone https://github.com/nixuser/package-example.git

cp package-example/stub.tar.gz ~/rpmbuild/SOURCES/
cp package-example/shellspec-0.28.1.tar.gz ~/rpmbuild/SOURCES
cp package-example/shellspec.spec ~/rpmbuild/SPECS/
rpmbuild -ba ~/rpmbuild/SPECS/shellspec.spec




