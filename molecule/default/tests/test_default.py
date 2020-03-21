import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_sshd_conf(host):
    conf = host.file('/etc/ssh/sshd_config')

    assert conf.exists
    assert conf.user == 'root'
    assert conf.group == 'root'

def test_sshd_conf_content(host):
    conf = host.file('/etc/ssh/sshd_config')
    conf_content = conf.content

    expected = [
      b'Subsystem sftp internal-sftp',
      b'AuthorizedKeysFile /etc/ssh/authorized_keys/%u %h/.ssh/authorized_keys',
      b'Match LocalAddress 127.0.0.1\n  AllowUsers test\n  AuthorizedKeysCommand /bin/true',
      b'Match Group sftponly\n  AuthorizedKeysFile /etc/ssh/authorized_keys/%u\n  ChrootDirectory %h\n  X11Forwarding no',
    ]

    for line in expected:
        assert line in conf_content
