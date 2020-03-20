Ansible Role SSH server
=========

[![Build Status](https://travis-ci.com/Turgon37/ansible-ssh-server.svg?branch=master)](https://travis-ci.com/Turgon37/ansible-ssh-server)
[![License](https://img.shields.io/badge/license-MIT%20License-brightgreen.svg)](https://opensource.org/licenses/MIT)
[![Ansible Role](https://img.shields.io/badge/ansible%20role-Turgon37.ssh_server-blue.svg)](https://galaxy.ansible.com/Turgon37/ssh_server/)

## Description

:grey_exclamation: Before using this role, please know that all my Ansible roles are fully written and accustomed to my IT infrastructure. So, even if they are as generic as possible they will not necessarily fill your needs, I advice you to carrefully analyse what they do and evaluate their capability to be installed securely on your servers.

This roles allow configuration of ssh server.


## Requirements

Require Ansible >= 2.4

### Dependencies

## OS Family

This role is available for Debian and CentOS

## Features

At this day the role can be used to :

  * install sshd
  * configure sshd
  * filter the initial moduli to remove weak prime numbers
  * [local facts](#facts)

## Role Variables

All variables which can be overridden are stored in [defaults/main.yml](defaults/main.yml) file as well as in table below. To see default values please refer to this file.

Most of the variables refers to the pure sshd config parameter. Please fetch informations from the man page.

| Name                                                   | Types/Values   | Description                                                       |
| ------------------------------------------------------ | ---------------|------------------------------------------------------------------ |
| `ssh_server__facts`                                    | Boolean        | Install the local fact script                                     |
| `ssh_server__moduli_minimum`                           | Integer        | The minimum size of primes to keep in moduli file                 |
| `ssh_server__service_enabled`                          | Boolean        | Enable or not the service                                         |
| `ssh_server__protocol`                                 | String         | See manpage                                                       |
| `ssh_server__privilege_separation`                     | String         | See manpage                                                       |
| `ssh_server__pidfile`                                  | String         | See manpage                                                       |
| `ssh_server__log_facility`                             | String         | See manpage                                                       |
| `ssh_server__log_level`                                | String         | See manpage                                                       |
| `ssh_server__ports`                                    | List of integer| See manpage                                                       |
| `ssh_server__listen`                                   | List of ip     | See manpage                                                       |
| `ssh_server__address_family`                           | String         | See manpage                                                       |
| `ssh_server__use_dns`                                  | Boolean        | See manpage                                                       |
| `ssh_server__tcp_keepalive`                            | Boolean        | See manpage                                                       |
| `ssh_server__allow_agent_forwarding`                   | Boolean        | See manpage                                                       |
| `ssh_server__allow_tcp_forwarding`                     | Boolean        | See manpage                                                       |
| `ssh_server__permit_open`                              | String         | See manpage                                                       |
| `ssh_server__gateway_ports`                            | String         | See manpage                                                       |
| `ssh_server__allow_stream_local_forwarding`            | Boolean        | See manpage                                                       |
| `ssh_server__permit_tunnel`                            | Boolean        | See manpage                                                       |
| `ssh_server__compression`                              | String         | See manpage                                                       |
| `ssh_server__ip_qos`                                   | Tuple          | See manpage                                                       |
| `ssh_server__kex_algorithms`                           | List of string | See manpage                                                       |
| `ssh_server__kex_algorithms_additional`                | List of string | See manpage                                                       |
| `ssh_server__ciphers`                                  | List of string | See manpage                                                       |
| `ssh_server__ciphers_additional`                       | List of string | See manpage                                                       |
| `ssh_server__macs`                                     | List of string | See manpage                                                       |
| `ssh_server__macs_additional`                          | List of string | See manpage                                                       |
| `ssh_server__server_key_bits`                          | Integer        | See manpage                                                       |
| `ssh_server__key_regeneration_interval`                | Integer        | See manpage                                                       |
| `ssh_server__authentication_methods`                   | String         | See manpage                                                       |
| `ssh_server__use_pam`                                  | Boolean        | See manpage                                                       |
| `ssh_server__use_login`                                | Boolean        | See manpage                                                       |
| `ssh_server__password_authentication`                  | Boolean        | See manpage                                                       |
| `ssh_server__permit_empty_passwords`                   | Boolean        | See manpage                                                       |
| `ssh_server__challenge_response_authentication`        | Boolean        | See manpage                                                       |
| `ssh_server__keyboard_interactive_authentication`      | Boolean        | See manpage                                                       |
| `ssh_server__pubkey_authentication`                    | Boolean        | See manpage                                                       |
| `ssh_server__authorized_keys`                          | List of string | See manpage AuthorizedKeysFile                                    |
| `ssh_server__authorized_keys_system`                   | List of string | Contains the path to the global system authorized keys file       |
| `ssh_server__authorized_keys_user`                     | String         | Contains the path to the per user authorized keys file            |
| `ssh_server__authorized_keys_command`                  | String         | See manpage                                                       |
| `ssh_server__authorized_keys_command_user`             | List of string | See manpage                                                       |
| `ssh_server__permit_blacklisted_keys`                  |                | See manpage                                                       |
| `ssh_server__rsa_authentication`                       | Boolean        | See manpage                                                       |
| `ssh_server__rhosts_rsa_authentication`                | Boolean        | See manpage                                                       |
| `ssh_server__host_based_authentication`                | Boolean        | See manpage                                                       |
| `ssh_server__host_based_uses_name_from_packet_only`    | Boolean        | See manpage                                                       |
| `ssh_server__ignore_user_known_hosts`                  | Boolean        | See manpage                                                       |
| `ssh_server__ignore_rhosts`                            | Boolean        | See manpage                                                       |
| `ssh_server__kerberos_authentication`                  | Boolean        | See manpage                                                       |
| `ssh_server__kerberos_get_afs_token`                   | Boolean        | See manpage                                                       |
| `ssh_server__kerberos_or_local_passwd`                 | Boolean        | See manpage                                                       |
| `ssh_server__kerberos_ticket_cleanup`                  | Boolean        | See manpage                                                       |
| `ssh_server__kerberos_use_kuserok`                     | Boolean        | See manpage                                                       |
| `ssh_server__gssapi_authentication`                    | Boolean        | See manpage                                                       |
| `ssh_server__gssapi_key_exchange`                      | Boolean        | See manpage                                                       |
| `ssh_server__gssapi_cleanup_credentials`               | Boolean        | See manpage                                                       |
| `ssh_server__gssapi_strict_acceptor_check`             | Boolean        | See manpage                                                       |
| `ssh_server__gssapi_store_credentials_on_rekey`        | Boolean        | See manpage                                                       |
| `ssh_server__gssapi_enable_k5_users`                   | Boolean        | See manpage                                                       |
| `ssh_server__deny_users`                               | List of string | See manpage                                                       |
| `ssh_server__allow_users`                              | List of string | See manpage                                                       |
| `ssh_server__deny_groups`                              | List of string | See manpage                                                       |
| `ssh_server__allow_groups`                             | List of string | See manpage                                                       |
| `ssh_server__permit_root_login`                        | String         | See manpage                                                       |
| `ssh_server__login_grace_time`                         | String         | See manpage                                                       |
| `ssh_server__max_auth_tries`                           | Integer        | See manpage                                                       |
| `ssh_server__max_sessions`                             | Integer        | See manpage                                                       |
| `ssh_server__max_startups`                             | Specific dict  | This dict must have the keys 'start', 'rate', 'full' (See manpage)|
| `ssh_server__accept_env`                               | List of string | See manpage                                                       |
| `ssh_server__permit_user_environment`                  | Boolean        | See manpage                                                       |
| `ssh_server__permit_user_rc`                           | Boolean        | See manpage                                                       |
| `ssh_server__permit_tty`                               | Boolean        | See manpage                                                       |
| `ssh_server__strict_modes`                             | Boolean        | See manpage                                                       |
| `ssh_server__version_addendum`                         | String         | See manpage                                                       |
| `ssh_server__banner`                                   | String         | See manpage                                                       |
| `ssh_server__debian_banner`                            | Boolean        | See manpage                                                       |
| `ssh_server__print_motd`                               | Boolean        | See manpage                                                       |
| `ssh_server__print_last_log`                           | Boolean        | See manpage                                                       |
| `ssh_server__force_command`                            | String         | See manpage                                                       |
| `ssh_server__chroot_directory`                         | String         | See manpage                                                       |
| `ssh_server__client_alive_interval`                    | Integer        | See manpage                                                       |
| `ssh_server__client_alive_count_max`                   | Integer        | See manpage                                                       |
| `ssh_server__x11_forwarding`                           | Boolean        | See manpage                                                       |
| `ssh_server__x11_display_offset`                       | Integer        | See manpage                                                       |
| `ssh_server__x11_use_localhost`                        | Boolean        | See manpage                                                       |
| `ssh_server__subsystems_global/group/host`             | Dict           | Mapping of subsystem name and subsystem command                   |
| `ssh_server__match_list_global/group/host`             |                |                                                                   |


### Matchs

You can configure the available match using the `ssh_server__match_list_global/group/host` variables availables.
Theses variable takes list of dict. Each dict must have the following form :

```
ssh_server__match_list_global
  - match: "match criterias"
    options:                                     # options that apply if "match" matches
      - AllowUsers test                          # a simple string option
      # a dict with version conditioned options
      # according to the current sshd version, the higher version condition win and it's options are applied
      - 8.2: AuthorizedKeysCommand /bin/true     # (string version)
        7.6:                                     # (list version)
          - AuthenticationMethods publickey
          - AllowUsers root
    state: absent               # optional state (default to present)
```

The available match criterias and options that you can apply depends on your current sshd version.


An example of group only allowed to run sftp is given, if you want to enable it you can use this bloc in inventory :

```
ssh_server__match_list_global:
  - '{{ ssh_server__match_group_sftponly }}'
```

## Facts

By default the local fact are installed and expose the following variables :


```
ansible_local.ssh_server:
  version_full: '7.9p1'
  version_major: '7'
```


## Example

### Playbook

Use it in a playbook as follows:

```yaml
- hosts: all
  roles:
    - turgon37.ssh_server
```

### Inventory

To use this role create or update your playbook according the following example :

```
ssh_server__allow_agent_forwarding: false
ssh_server__allow_tcp_forwarding: false
ssh_server__allow_stream_local_forwarding: false
ssh_server__permit_tunnel: false
ssh_server__compression: true

ssh_server__allow_groups:
  - ssh
  - ssh-admins
ssh_server__permit_root_login: false
ssh_server__max_startups:
  start: 5
  rate: 80
  full: 10

ssh_server__match_list_global:
  - match: "LocalAddress 127.0.0.1"
    options:
      - AuthenticationMethods publickey,password
    state: present

  - match: "LocalAddress 10.0.0.1 Group ssh-admins"
    options:
    - AuthenticationMethods publickey password gssapi-with-mic

  - match: "LocalAddress 10.0.0.1 User root"
    options:
      - DenyUsers
      - AllowUsers root
      - DenyGroups
      - AllowGroups root
      - 7.0: 'PermitRootLogin prohibit-password'
        4.9: 'PermitRootLogin without-password'
      - AuthenticationMethods publickey
      - AuthorizedKeysFile /root/.ssh/authorized_keys
      - AuthorizedKeysCommand /bin/true

ssh_client__known_hosts_additionals:
  - '[gitlab]:7999 ssh-rsa XXXXX'
```

#### Example of FreeIPA configuration

```
ssh_server__authorized_keys: '/dev/null'
ssh_server__authorized_keys_lookup: true
ssh_server__authorized_keys_lookup_command: /usr/bin/sss_ssh_authorizedkeys
ssh_server__pubkey_authentication: true
ssh_server__gssapi_authentication: true
```
