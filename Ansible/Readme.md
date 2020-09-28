## Start Vagrant server

```
$ cd server_vagrant/
$ vagrant up
```

## Delete the l-server
```
vagrant destroy
sed -ie "/l-server/d" ~/.ssh/known_hosts
```

## Edit Ansible Vault

Edit ansible vault
```
EDITOR='code --wait' ansible-vault create group_vars/local_vault.yml 

EDITOR='code --wait' ansible-vault edit group_vars/local_vault.yml 
```

## Run Ansible playbook

```
ansible-playbook -i hosts/local -vvv -K --ask-vault-pass installApp.yml 2>&1 | tee -a ../logs/`date +%Y-%m-%d__%H-%M-%S`_installApp.yml_LOCAL.log
```

## Debug Ansible missing variables
```
$ ansible app_server -i hosts/local --ask-vault-pass -m debug -a "msg={{ ssh_key }}"
```

## Vagrant snapshots

### Save snapshot
```
vagrant snapshot save before_adding_provisioning
```
### Restore snapshot
```
vagrant snapshot restore before_adding_provisioning
```