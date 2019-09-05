## How To Harden A Raspberry Pi

Here's a curated  some best practices how to secure a Raspberry Pi. We will also implement and enable the security features to make the Pi secure.

#### Changing Default Password

#### Changing The Username

#### Deleting `pi` user

To delete the pi user, type the following:
```
sudo deluser pi
```
This command will delete the pi user but will leave the home/pi folder. If necessary, you can use the command below to remove the home folder for the pi user at the same time. Note the data in this folder will be permanently deleted, so make sure any required data is stored elsewhere.
```
sudo deluser -remove-home pi
```
#### Making `sudo` Require A Password

#### No Services Are Running as `root`

#### Disable SSH Login as `root`

#### Setting Up A Firewall

#### Fail2Ban

### Improving SSH Security

SSH is one of the most common techniques to access Raspberry Pi over the network and it becomes necessary to use if you want to make it secure.

#### Username And Password Security

#### Key-Based Authentication
