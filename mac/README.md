
## Adding pffirewall.log to newsyslog


### Added log file to newsyslog

jdelat04@ITS-JDELAT04-1 ~
$ diff /etc/newsyslog.conf /etc/newsyslog.conf.bak.2019-10-16 
26d25
< /var/log/pffirewall.log                 640  20   1000 *    J


### Confirm the changes woke wihtout trimming

jdelat04@ITS-JDELAT04-1 ~
$ sudo newsyslog -nv
Password:
/var/log/ftp.log <5J>: does not exist, skipped.
/var/log/hwmond.log <5J>: does not exist, skipped.
/var/log/ipfw.log <5J>: does not exist, skipped.
/var/log/lpr.log <5J>: does not exist, skipped.
/var/log/ppp.log <5J>: does not exist, skipped.
/var/log/wtmp <3>: does not exist, skipped.
/var/log/pffirewall.log <20J>: size (Kb): 131076 [1000] --> trimming log....
	rm -f /var/log/pffirewall.log.20
	rm -f /var/log/pffirewall.log.20.gz
	rm -f /var/log/pffirewall.log.20.bz2
	ln /var/log/pffirewall.log /var/log/pffirewall.log.0
	chmod 640 /var/log/pffirewall.log.0
	chown 4294967295:80 /var/log/pffirewall.log.0
Start new log...
	mktemp /var/log/pffirewall.log.zXXXXXX
	chown 4294967295:80 /var/log/pffirewall.log.zXXXXXX
	chmod 640 /var/log/pffirewall.log.zXXXXXX
	mv /var/log/pffirewall.log.zXXXXXX /var/log/pffirewall.log
/Library/Logs/slapconfig.log <10J>: does not exist, skipped.
/var/log/slapd.log <10J>: does not exist, skipped.
/var/log/xscertd.log <5J>: does not exist, skipped.
/Library/Logs/named.log <5J>: does not exist, skipped.
/var/log/wifi.log <10J>: --> will trim at Thu Oct 17 00:00:00 2019
Signal all daemon process(es)...
	kill -1 44 		# /var/run/syslog.pid
	sleep 10
Compress all rotated log file(s)...
	bzip2 /var/log/pffirewall.log.0
	chmod 640 /var/log/pffirewall.log.0.bz2
	chown 4294967295:80 /var/log/pffirewall.log.0.bz2



## Execute newsyslog

jdelat04@ITS-JDELAT04-1 ~
$ sudo newsyslog -v
Password:
Sorry, try again.
Password:
/var/log/ftp.log <5J>: does not exist, skipped.
/var/log/hwmond.log <5J>: does not exist, skipped.
/var/log/ipfw.log <5J>: does not exist, skipped.
/var/log/lpr.log <5J>: does not exist, skipped.
/var/log/ppp.log <5J>: does not exist, skipped.
/var/log/wtmp <3>: does not exist, skipped.
/var/log/pffirewall.log <20J>: size (Kb): 131076 [1000] --> trimming log....
/Library/Logs/slapconfig.log <10J>: does not exist, skipped.
/var/log/slapd.log <10J>: does not exist, skipped.
/var/log/xscertd.log <5J>: does not exist, skipped.
/Library/Logs/named.log <5J>: does not exist, skipped.
/var/log/wifi.log <10J>: --> will trim at Thu Oct 17 00:00:00 2019
Signal all daemon process(es)...
Notified daemon pid 44 = /var/run/syslog.pid
Pause 10 seconds to allow daemon(s) to close log file(s)
Compress all rotated log file(s)...


## Before and after

jdelat04@ITS-JDELAT04-1 ~
$ du -sh /var/log/*
128M	/var/log/pffirewall.log		  


jdelat04@ITS-JDELAT04-1 ~
$ du -sh /var/log/*
8.0K	/var/log/pffirewall.log
4.0M	/var/log/pffirewall.log.0.bz2
