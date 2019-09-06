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

