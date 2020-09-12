#!/bin/bash

cd ~/Downloads

function showStatus() {
	printf "\n${1}\n"
}

function install() {
  sudo apt-get install -y "$@"
}


install ubuntu-restricted-extras software-properties-common -y && sudo apt-get update -y && sudo apt-get dist-upgrade -y && sudo apt-get autoremove -y


install vim vim-nox htop tree -y
