# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  # Ubuntu 14.04
  config.vm.box = "ubuntu/trusty64"

  # Mount the repo in /home/vagrant/docs/
  config.vm.synced_folder ".", "/home/vagrant/docs/"

  # Expose 4000 to host
  config.vm.network "forwarded_port", guest: 4000, host: 4000

  config.vm.provision "shell", inline: <<-SHELL
    # Update machine
    sudo apt-get update
    sudo apt-get upgrade -y

    # Install dependencies
    sudo apt-get install nodejs python-software-properties git-core -y

    # Add GPG key to get RVM
    sudo gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3

    # Install rvm
    curl -sSL https://get.rvm.io | bash -s stable --ruby=2.1.5

    # Reload rvm into bash
    source /etc/profile.d/rvm.sh

    # Set default ruby to 2.1.5
    rvm --default use 2.1.5

    # Install bundler gem
    sudo gem install bundler

    # Repo
    cd /home/vagrant/docs/
    bundle install
  SHELL
end
