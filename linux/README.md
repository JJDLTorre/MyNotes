# Juan_Linux_Notes

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
