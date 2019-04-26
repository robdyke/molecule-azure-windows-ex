import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_chocolatey(host):
    f = host.file('C:\\ProgramData\\Chocolatey')

    assert f.exists
