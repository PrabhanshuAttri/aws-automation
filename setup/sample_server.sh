#!/bin/bash

function install() {
  sudo apt-get install -y "$@"
}

install redis-server
sudo systemctl restart redis.service