### VirtualBox notes

## How to resize your dirve

- Settings -> Storage -> Select th dirve and right-click and  Remove it


VBoxMange.exe modifymedium "vdi" --resize 100000


```bash
jdelat04@IS-JDELAT04-1 /cygdrive/c/Program Files/Oracle/VirtualBox
$ ./VBoxManage.exe modifymedium --help
Oracle VM VirtualBox Command Line Management Interface Version 6.0.10
(C) 2005-2019 Oracle Corporation
All rights reserved.

Usage:

VBoxManage modifymedium     [disk|dvd|floppy] <uuid|filename>
                            [--type normal|writethrough|immutable|shareable|
                                    readonly|multiattach]
                            [--autoreset on|off]
                            [--property <name=[value]>]
                            [--compact]
                            [--resize <megabytes>|--resizebyte <bytes>]
                            [--move <path>]
                            [--setlocation <path>]
                            [--description <description string>]

Syntax error: unknown option: --help


jdelat04@IS-JDELAT04-1 /cygdrive/c/Program Files/Oracle/VirtualBox
$ ./VBoxManage.exe modifymedium "F:\VMs\l-climateWeb1\l-climateWeb1-2018-10-26.vhd" --resize 100000
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
```
- Settings -> Storage -> Click on "Add hard disk." and "Choose existing disk"

### Re-attach the drive and restart the linux machine


## Add new partition

### Verify the disk was resized

```bash
jdelat04@juanlinux ~
$ sudo su - root
[sudo] password for jdelat04: 
Last login: Fri Sep  6 11:22:44 PDT 2019 on pts/2

root@juanlinux ~
# fdisk -l

Disk /dev/sda: 104.9 GB, 104857600000 bytes, 204800000 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x000af094

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    33554431    15727616   8e  Linux LVM

Disk /dev/sdb: 107.4 GB, 107374182400 bytes, 209715200 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0xbd361eb9

   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1            2048   209715199   104856576   83  Linux

Disk /dev/mapper/cl-root: 14.4 GB, 14382268416 bytes, 28090368 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes


Disk /dev/mapper/cl-swap: 1719 MB, 1719664640 bytes, 3358720 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
```

Notice that __/dev/sda__ has 2 partitions and it now has 104.9 GB size. 


### Add the third partition to the root drive

```bash
root@juanlinux ~
# fdisk /dev/sda
Welcome to fdisk (util-linux 2.23.2).

Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): n
Partition type:
   p   primary (2 primary, 0 extended, 2 free)
   e   extended
Select (default p): p
Partition number (3,4, default 3): 3
First sector (33554432-204799999, default 33554432): 
Using default value 33554432
Last sector, +sectors or +size{K,M,G} (33554432-204799999, default 204799999): 
Using default value 204799999
Partition 3 of type Linux and of size 81.7 GiB is set

Command (m for help): t
Partition number (1-3, default 3): 3
Hex code (type L to list all codes): 8e
Changed type of partition 'Linux' to 'Linux LVM'


Command (m for help): w
The partition table has been altered!

Calling ioctl() to re-read partition table.

WARNING: Re-reading the partition table failed with error 16: Device or resource busy.
The kernel still uses the old table. The new table will be used at
the next reboot or after you run partprobe(8) or kpartx(8)
Syncing disks.
```

### Reboot the VM

```bash
root@juanlinux ~
# shutdown -r now
```

### Initialize the LVM 

Verify that there is a third partition (__/dev/sda3__). 
```bash 
root@juanlinux ~
# fdisk -l

Disk /dev/sda: 104.9 GB, 104857600000 bytes, 204800000 sectors
Units = sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disk label type: dos
Disk identifier: 0x000af094

   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *        2048     2099199     1048576   83  Linux
/dev/sda2         2099200    33554431    15727616   8e  Linux LVM
/dev/sda3        33554432   204799999    85622784   8e  Linux LVM
```

```bash
root@juanlinux ~
# pvcreate /dev/sda3
  Physical volume "/dev/sda3" successfully created.
```

### Add partition to volume group
 
Get the name of the VG to extend (__cl__)

```bash
root@juanlinux ~
# pvdisplay 
  --- Physical volume ---
  PV Name               /dev/sda2
  VG Name               cl
  PV Size               <15.00 GiB / not usable 3.00 MiB
  Allocatable           yes (but full)
  PE Size               4.00 MiB
  Total PE              3839
  Free PE               0
  Allocated PE          3839
  PV UUID               2Zc6GJ-qfja-u6q5-5f6L-bARb-71wL-xkh6Wy
   
  "/dev/sda3" is a new physical volume of "<81.66 GiB"
  --- NEW Physical volume ---
  PV Name               /dev/sda3
  VG Name               
  PV Size               <81.66 GiB
  Allocatable           NO
  PE Size               0   
  Total PE              0
  Free PE               0
  Allocated PE          0
  PV UUID               rt9f6d-B1YH-7MmV-Fhes-LZgG-3ncq-p5ZHp1

```


Extend the Volume group

```bash
# vgextend cl /dev/sda3
  Volume group "cl" successfully extended
```
 
Confirm Volume group

```bash
# pvdisplay 
  --- Physical volume ---
  PV Name               /dev/sda2
  VG Name               cl
  PV Size               <15.00 GiB / not usable 3.00 MiB
  Allocatable           yes (but full)
  PE Size               4.00 MiB
  Total PE              3839
  Free PE               0
  Allocated PE          3839
  PV UUID               2Zc6GJ-qfja-u6q5-5f6L-bARb-71wL-xkh6Wy
   
  --- Physical volume ---
  PV Name               /dev/sda3
  VG Name               cl
  PV Size               <81.66 GiB / not usable 4.00 MiB
  Allocatable           yes 
  PE Size               4.00 MiB
  Total PE              20903
  Free PE               20903
  Allocated PE          0
  PV UUID               rt9f6d-B1YH-7MmV-Fhes-LZgG-3ncq-p5ZHp1
```

### Extend the root logical volume

Get the root logical volume name (__/dev/cl/root__)
```bash
root@juanlinux ~
# lvdisplay
  --- Logical volume ---
  LV Path                /dev/cl/swap
  LV Name                swap
  VG Name                cl
  LV UUID                iv168V-VfnN-JZAE-RlEU-ZprG-LjtC-Et6fCc
  LV Write Access        read/write
  LV Creation host, time juanlinux.localdomain, 2017-04-21 13:39:17 -0700
  LV Status              available
  # open                 2
  LV Size                1.60 GiB
  Current LE             410
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           253:1
   
  --- Logical volume ---
  LV Path                /dev/cl/root
  LV Name                root
  VG Name                cl
  LV UUID                HfJvuA-ftOs-UfLH-Ndn0-uWyb-dMak-JW6vkH
  LV Write Access        read/write
  LV Creation host, time juanlinux.localdomain, 2017-04-21 13:39:17 -0700
  LV Status              available
  # open                 1
  LV Size                13.39 GiB
  Current LE             3429
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  Block device           253:0

```

```bash
root@juanlinux ~
# lvextend --size +81.6G --resizefs /dev/cl/root
  Rounding size to boundary between physical extents: 81.60 GiB.
  Size of logical volume cl/root changed from 13.39 GiB (3429 extents) to <95.00 GiB (24319 extents).
  Logical volume cl/root successfully resized.
meta-data=/dev/mapper/cl-root    isize=512    agcount=4, agsize=877824 blks
         =                       sectsz=512   attr=2, projid32bit=1
         =                       crc=1        finobt=0 spinodes=0
data     =                       bsize=4096   blocks=3511296, imaxpct=25
         =                       sunit=0      swidth=0 blks
naming   =version 2              bsize=4096   ascii-ci=0 ftype=1
log      =internal               bsize=4096   blocks=2560, version=2
         =                       sectsz=512   sunit=0 blks, lazy-count=1
realtime =none                   extsz=4096   blocks=0, rtextents=0
data blocks changed from 3511296 to 24902656

```

### Verify we have increased the root mount size

```bash 
root@juanlinux ~
# df -h
Filesystem           Size  Used Avail Use% Mounted on
/dev/mapper/cl-root   95G   14G   82G  14% /
```


### Recovered from missing files after resize

#### Find the snapshot that had the last change

I looked in the "F:\VMs\juanLinux\Snapshots" directory and found the snapshot that had the last modified date that I wanted. 

```bash
$ ./VBoxManage.exe list hdds
UUID:           947cadf1-edc7-4023-a311-d6cec2a8f41e
Parent UUID:    86c91997-b355-441b-8c59-5ceebd635f4b
State:          created
Type:           normal (differencing)
Location:       F:\VMs\juanLinux\Snapshots/{947cadf1-edc7-4023-a311-d6cec2a8f41e}.vdi
Storage format: VDI
Capacity:       16384 MBytes
Encryption:     disabled

```

Clone a new disk from that snapshot. 
```bash
$ ./VBoxManage clonemedium disk 947cadf1-edc7-4023-a311-d6cec2a8f41e "F:\VMs\juanLinux\juanLinuxRecover.vdi"
0%...10%...20%...30%...40%...50%...60%...70%...80%...90%...100%
Clone medium created in format 'VDI'. UUID: b56f13b1-86b5-4806-b42d-de7c46c10cdd
```
Attach that new hardisk and remove the old disk then reboot. 



