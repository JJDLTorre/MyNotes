# MyNotes

## Command Line Union, Intersection, and Difference
### Files: 
```bash
Juan@Juan-XPS-2011 ~/tmp
$ cat File1.txt
A
B
C
Juan@Juan-XPS-2011 ~/tmp
$ cat File2.txt
A
D
F
```
### Union: sort -u files...
```bash
Juan@Juan-XPS-2011 ~/tmp
$ sort -u File1.txt File2.txt
A
B
C
D
F
```

### Intersection: sort files... | uniq -d
```bash
Juan@Juan-XPS-2011 ~/tmp
$ sort File1.txt File2.txt | uniq -d
A
```

### Difference: sort files... | uniq -u
```bash
Juan@Juan-XPS-2011 ~/tmp
$ sort File1.txt File2.txt | uniq -u
B
C
D
F
```

### Tee to a log file
```
$ command | tee -a logs/`date +%Y-%m-%d_%H-%M-%S`_command.log
```
