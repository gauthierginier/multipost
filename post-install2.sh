#!/bin/bash
export DEBIAN_FRONTEND=noninteractive 
echo "UBUNTU POST-INSTALL SCRIPT"
apt -yq install net-tools zsh

echo "Setting local date/time"
timedatectl set-timezone Europe/Paris

echo "enabling the Mysql APT repository"
wget /home/gogodev/mysql-apt-config_0.8.16-1_all.deb https://dev.mysql.com/get/mysql-apt-config_0.8.16-1_all.deb

echo "Installing base packages"
apt-get -yq install  git git-extras build-essential python3-pip htop glances

echo "Installing oh my zsh"
#echo "2" | zsh
#echo n | sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

echo "PermitRootLogin without-password" >> /etc/ssh/sshd_config
sed -i 's/PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

dpkg -i /home/gogodev/mysql-apt-config_0.8.16-1_all.deb
echo "Updating APT..."
apt -yq install mysql-server

#apt-get update
#mysql_secure_installation
mysqladmin --user=root password "2011Ggg2"
mysql --user=root --password=2011Ggg2 < file.sql
sudo sed -i 's/^bind-address.*/bind-address = 192.168.1.3/' /etc/mysql/mysql.conf.d/mysqld.cnf
echo "Updated mysql bind address in the good file to my VM to allow external connections."
systemctl restart mysql

