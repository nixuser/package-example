# -*- mode: ruby -*-
# vi: set ft=ruby :
# export VAGRANT_EXPERIMENTAL="disks"

Vagrant.configure("2") do |config|

  config.vm.box = 'almalinux/9'
  config.vm.network :forwarded_port, guest: 22, host: 4000

config.vm.define "server" do |server|

  server.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
  end

  server.vm.disk :disk, size: "1GB", name: "disk1"
  server.vm.host_name = 'server'
  server.vm.network :private_network, ip: "10.0.0.41"


end
end
