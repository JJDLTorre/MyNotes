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



