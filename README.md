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

## Vagrant

### Adding personal ssh public key and current user
Vagrantfile
```
  config.vm.provision "shell" do |s|

    ssh_pub_key = File.readlines("#{Dir.home}/.ssh/id_rsa.pub").first.strip 
    s.inline = <<-SHELL
      sed -ie 's/^.*: history-search-backward/\"\\e[A\": history-search-backward/' /etc/inputrc
      sed -ie 's/^.*: history-search-forward/\"\\e[B\": history-search-forward/' /etc/inputrc

      echo #{ssh_pub_key} >> /home/vagrant/.ssh/authorized_keys

      useradd #{ENV['USER']}

      echo "%"#{ENV['USER']} " ALL=(ALL) ALL" > /etc/sudoers.d/#{ENV['USER']}

      mkdir -p /home/#{ENV['USER']}/.ssh/
      echo #{ssh_pub_key} >> /home/#{ENV['USER']}/.ssh/authorized_keys
      chown --recursive #{ENV['USER']}:#{ENV['USER']} /home/#{ENV['USER']}/.ssh
      chmod 700 /home/#{ENV['USER']}/.ssh/
      chmod 600 /home/#{ENV['USER']}/.ssh/authorized_keys
    SHELL
  end
```
