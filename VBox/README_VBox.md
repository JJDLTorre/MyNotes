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



