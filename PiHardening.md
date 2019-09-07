## How To Harden A Raspberry Pi

Here's a curated  some best practices how to secure a Raspberry Pi. We will also implement and enable the security features to make the Pi secure.

### Changing Default Password

Every Raspberry Pi that is running the Raspbian operating system has the default username *pi* and default password *raspberry*, which should be changed as soon as we boot up the Pi for the first time. If our Raspberry Pi is exposed to the internet and the default username and password has not been changed, then it becomes an easy target for hackers.

- Open Up A Terminal
- Type `sudo raspi-config` And Press Enter
- Select *Option 1*
- Enter New Password
- Re-Enter Password
- You're Done

### Changing The Username

All Raspberry Pis come with the default username *pi*, which should be changed to make it more secure. We create a new user and assign it all rights.

- Open Up A Terminal
- Type `sudo adduser brucewayne` And Press Enter
- Enter New Password
- Re-Enter Password
- Fill or Skip The Rest
- Enter *Y* When Prompted

Now, We Have Our User `brucewayne` Created. It's Time To Add It To The Group `sudo` By The following Command.
```
sudo adduser brucewayne sudo
```

### Deleting `pi` user

To delete the pi user, type the following:
```
sudo deluser pi
```
This command will delete the pi user but will leave the `home/pi` folder. If necessary, you can use the command below to remove the home folder for the `pi` user at the same time.
```
sudo deluser -remove-home pi
```
If You Directly Deleted User `pi` Without The `-remove-home` Tag And Are Stuck With The User's Home Directory, Run This Command.
```
sudo rm -r /home/pi
```

### Making `sudo` Require A Password

When a command is run with sudo as the prefix, then it’ll execute it with superuser privileges. By default, running a command with sudo doesn’t need a password, but this can cost dearly if a hacker gets access to Raspberry Pi and takes control of everything. To make sure that a password is required every time a command is run with superuser privileges, do the following.

- Open Up A Terminal
- Type `sudo nano /etc/sudoers.d/010_pi-nopasswd` And Press Enter
- Replace All With `pi ALL=(ALL) PASSWD: ALL`
- Save The File And Reboot Your Pi

### No Services Are Running as `root`

### Disable SSH Login as `root`

### Setting Up A Firewall

### Fail2Ban

### Improving SSH Security

SSH is one of the most common techniques to access Raspberry Pi over the network and it becomes necessary to use if you want to make it secure.

#### Username And Password Security

#### Key-Based Authentication
