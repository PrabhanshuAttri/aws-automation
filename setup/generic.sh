#!/bin/bash

function showStatus() {
	printf "\n${1}\n"
}

function install() {
  sudo apt-get install -y "$@"
}

echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula select true | sudo debconf-set-selections
install ttf-mscorefonts-installer

install software-properties-common && sudo apt-get update -y && sudo apt-get dist-upgrade -y && sudo apt-get autoremove -y

install vim vim-nox htop git

sudo snap install tree -y

install ubuntu-restricted-extras

sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get autoremove -y