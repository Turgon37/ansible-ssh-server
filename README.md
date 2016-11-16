Ansible Role SSH server
========

This roles allow configuration of ssh server

## OS Family

This role is available for Debian and CentOS

## Features

At this day the role can be used to configure :

  * SSHD server

## Configuration

All available variables are put in the defaults/main.yml.
As an overview, the following variable are theses that are the most commonly used

| Name                            | Description                                                          |
| --------------------------------| -------------------------------------------------------------------- |
| sshd__ports                     | The list of ports on whose the daemon will listen for incoming client|
| sshd__permit_root_login         | Enable or not the login for root user                                |
| sshd__password_authentication   | Enable or not password authentication                                |
| sshd__pubkey_authentication     | Enable or not the authentication with private keys                   |
| sshd__allow_groups              | The list of UNIX group that are allowed to connect with SSH          |

### Example of configuration

  * The set of parameter specific to a FreeIPA client :

```
sshd__authorized_keys: '/dev/null'
sshd__authorized_keys_lookup: True
sshd__authorized_keys_lookup_command: '/usr/bin/sss_ssh_authorizedkeys'
sshd__pubkey_authentication: True
sshd__gssapi_authentication: True
```