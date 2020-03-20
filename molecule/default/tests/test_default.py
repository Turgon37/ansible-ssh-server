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
        b'AuthorizedKeysCommand /bin/true'
    ]

    for line in expected:
        assert line in conf_content
