#!/bin/bash
if  [ $# -ne 2 ]; then
echo "usage: addUserWithDebug.sh <user_name> <home_dir> "
exit 1
fi

home_dir="$2"

if [ -d "$home_dir" ] 
then
   echo "Found: $home_dir" 
else 
   mkdir "$home_dir"
fi

adduser $1 --create-home --base-dir "$home_dir"
echo "Created $1 with home $home_dir"

user_home_dir=$home_dir/$1

# Add ability to work and debug
mkdir -p $user_home_dir/.ssh
cat /home/vagrant/.ssh/authorized_keys >> $user_home_dir/.ssh/authorized_keys
chmod 700 $user_home_dir/.ssh
chmod 600 $user_home_dir/.ssh/authorized_keys
chown -R $1:$1 $user_home_dir