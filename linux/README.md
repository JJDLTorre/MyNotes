# Juan_Linux_Notes

### Crate users and add them to the sudoers with allow all
```bash
adduser user01
passwd  user01
echo "%user01 ALL=(ALL) ALL" > /etc/sudoers.d/user01
```

### Add up/down arrows to get history matches
```bash
sudo sed -ie 's/^.*: history-search-backward/\"\\e[A\": history-search-backward/' /etc/inputrc
sudo sed -ie 's/^.*: history-search-forward/\"\\e[B\": history-search-forward/' /etc/inputrc
```

### Allow ssh and restart sshd
```bash
sed -ie 's/^PasswordAuthentication no/PasswordAuthentication yes/' /etc/ssh/sshd_config
systemctl restart sshd
```

### Move MySQL logs to my dir and change owner
```bash
mv /var/lib/mysql/l-moodledb1.log /home/user01/.
chown user01:user01 /home/user01/l-moodledb1.log 
```

### Append group to a user

```bash
$ sudo usermod -a -G xboxsf tmp
```

The **-a** is to append and the **-G** is to a group. 


### Update date and time using another server
```bash
@l-server ~]# date --utc --set="`ssh user@192.168.56.1 date -u`"
```

### Enable sshd when server starts
```bash
[root@juanLinux ~]# chkconfig
Note: This output shows SysV services only and does not include native
      systemd services. SysV configuration data might be overridden by native
      systemd configuration.

      If you want to list systemd services use 'systemctl list-unit-files'.
      To see services enabled on particular target use
      'systemctl list-dependencies [target]'.

livesys         0:off   1:off   2:off   3:on    4:on    5:on    6:off
livesys-late    0:off   1:off   2:off   3:on    4:on    5:on    6:off
netconsole      0:off   1:off   2:off   3:off   4:off   5:off   6:off
network         0:off   1:off   2:off   3:off   4:off   5:off   6:off

[root@juanLinux ~]# chkconfig sshd
Note: Forwarding request to 'systemctl is-enabled sshd.service'.
disabled

[root@juanLinux ~]# chkconfig sshd on
Note: Forwarding request to 'systemctl enable sshd.service'.
Created symlink from /etc/systemd/system/multi-user.target.wants/sshd.service to /usr/lib/systemd/system/sshd.service.

[root@juanLinux ~]# chkconfig sshd
Note: Forwarding request to 'systemctl is-enabled sshd.service'.
enabled

```

## SSH Authorized Key 

### Client

- Create ssh-key and get the public key
```bash
$ ssh-keygen
$ cat .ssh/id_rsa.pub
```
- Set the correct permissions
```bash
$ chmod 700 ~/.ssh
$ chmod 400 ~/.ssh/id_rsa
```

### Server

- Create directory and authorized_keys
```bash
$ mkdir .ssh
$ echo client_id_rsa.pub >> .ssh/authorized_keys
```

- Set the correct permissions
```bash
$ chmod 700 ~/.ssh
$ chmod 600 ~/.ssh/authorized_keys
```

## Verifying SSL Certificates

nginx errored: 
```
failed (SSL: error:0B080074:x509 certificate routines:X509_check_private_key:key values mismatch)
```

To look at the certificate:
```
openssl x509 -noout -text -in yourcert.cert
```
Look for the "Subject" and then verify you see you site's infor, if not it's more likely the CA. 

### Check the MD5 has of both the public key and cert

```
$ openssl x509 -noout -modulus -in yourcert.cer | openssl md5
12345676aafcbb03e54de5d1dd1b

$ openssl rsa -noout -modulus -in yourcert.key | openssl md5
12345676aafcbb03e54de5d1dd1b
```


### Command line
Date and time format

date +%F_%H-%M-%S	2019-01-25_08-57-25
date +%F
2019-01-25
date +%F_%H-%M-%S
```
#!/bin/bash
DATE_TIME=`date +%Y-%m-%d_%H:%M:%S"`
 
echo "${DATE_TIME} Start Script"
```
