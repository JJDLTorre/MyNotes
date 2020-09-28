#!/bin/bash

/vagrant/provision/addUserWithDebug.sh "$1" "$2"

echo "%"$1 " ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/"$1"
echo "Added $1 to the sudoers"