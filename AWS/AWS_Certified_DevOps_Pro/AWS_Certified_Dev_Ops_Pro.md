
## CodeCommit 

### Create web-page repository

When createing a CodeCommit Repository you must also create a user. 

In this case I created: 

**user04_dev**

I added this user to the Admin group, the credentials were downloaded to /home/user04/Downloads/user04_dev.csv on the WorkSpaces.


https://sandbox-user04.signin.aws.amazon.com/console

```bash
[user04@a-rl6w4qcyy2fr Downloads]$ pwd
/home/user04/Downloads
[user04@a-rl6w4qcyy2fr Downloads]$ ls user04_dev*
user04_dev_codecommit_credentials.csv  user04_dev.csv
```

### Clone from CodeCommit

Created a Https Git credentials:

**user04_dev_codecommit_credentials.csv**

From the 

```
[I have no name!@a-rl6w4qcyy2fr repo]$ python3 -m pip install git-remote-codecommit --user
Collecting git-remote-codecommit
Requirement already satisfied: botocore>=1.17.0 in /usr/local/lib/python3.7/site-packages (from git-remote-codecommit)
Requirement already satisfied: jmespath<1.0.0,>=0.7.1 in /usr/local/lib/python3.7/site-packages (from botocore>=1.17.0->git-remote-codecommit)
Requirement already satisfied: docutils<0.16,>=0.10 in /usr/local/lib/python3.7/site-packages (from botocore>=1.17.0->git-remote-codecommit)
Requirement already satisfied: urllib3<1.26,>=1.20; python_version != "3.4" in /usr/local/lib/python3.7/site-packages (from botocore>=1.17.0->git-remote-codecommit)
Requirement already satisfied: python-dateutil<3.0.0,>=2.1 in /usr/local/lib/python3.7/site-packages (from botocore>=1.17.0->git-remote-codecommit)
Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.7/site-packages (from python-dateutil<3.0.0,>=2.1->botocore>=1.17.0->git-remote-codecommit)
Installing collected packages: git-remote-codecommit
Successfully installed git-remote-codecommit-1.15.1
```

### Get the correct credentials
What is currently there:
```
[I have no name!@a-rl6w4qcyy2fr repo]$ cat ~/.gitconfig 
[user]
  email = email@email.com
  name = first_name last_name
[credential]
  helper =
  helper = !aws codecommit credential-helper --profile SomeProfile $@
  usehttppath = true
```

```bash
git clone https://git-codecommit.us-west-2.amazonaws.com/v1/repos/my-webpage
```

### To cnofirm you profile
```
 aws --profile sandbox-user04_Admin codecommit list-repositories

aws --profile sandbox-user04_Admin codecommit get-repository --repository-name my-webpage
```
