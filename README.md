# CynKed
Quick and easy 2-way localized file synchronization
(Currently for use with Linux - Working on MacOS and Windows implementation)

Keep a directory of files synchronized across your devices. Use it as a local github to test your code on different comptuers. Keep a copy of your photos backed up. Send your video project files from your editing machine to your rendering machine.

Copy a specified directory back and forth between 2 machines.

# Dependencies
Make sure you have Python3 installed on your machine.
Install openssh on your machine:

### Ubuntu:
```
	sudo apt install openssh-server
```

# Setup

### SSH
Set up ssh keys between machines:
1. Generate ssh key for first machine:
```
 	ssh-keygen -t rsa
```
  Then press enter to set defaults as a password with ssh key will break the program.
2. Transfer ssh key to other machine:
```
 	ssh-copy-id remote_host
```
  Where the remote_host is the user@ip_address of the dersired machine.
3. Log in via ssh
```
	ssh remote_host
```

Repeat for the other machine and connect it to the first machine

### TOML Files
Place relavent information in your toml files. Set up both toml files, home being the one you are currently using, and remote being the one you will connect to. The toml files should be the opposite on each maching you are using.

ip: Your ip address in your local network
user: The user name of the system you are using (before the @ in your terminal)
file: The path to the file that you will be synchronizing with the remote machine
ck: The path to this directory on your machine
os: Your operating system

# Usage
If you want to pull your files from the remote server go to the directory where you have cynked.py saved and run
```
	python3 cynked.py pull
```
If you want to push your files from to remote server go to the directory where you have cynked.py saved and run
```
	python3 cynked.py push
```

This program will overwrite every file in the directory with the same name.

# Notes
Working on Adding MacOS and Windows Support.
Working on making synchronizing possible across multiple systems.
