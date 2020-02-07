import os
import pytest
import testinfra.utils.ansible_runner as ansible_runner

testinfra_hosts = ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

NVM_DEST = "/home/ansible/.nvm"


@pytest.mark.parametrize("item", ["git", "curl", "libssl-dev"])
def test_pkg_installed(host, item):
    pkg = host.package(item)
    assert pkg.is_installed


def test_nvm_dirctory_created(host):
    f = host.file(NVM_DEST)

    assert f.is_directory


def test_nvm_dirctory_correct_permissions(host):
    f = host.file(NVM_DEST)

    assert f.user == 'ansible'
    assert f.group == 'ansible'
    assert f.mode == 0o755


def test_nvm_file_exists(host):
    nvm_file = NVM_DEST + '/nvm.sh'
    f = host.file(nvm_file)

    assert f.is_file


def test_nvm_file_has_correct_permissions(host):
    nvm_file = NVM_DEST + '/nvm.sh'
    f = host.file(nvm_file)

    assert f.user == 'ansible'
    assert f.group == 'ansible'
    assert f.mode == 0o755
