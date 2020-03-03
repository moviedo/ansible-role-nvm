import os
import re
import testinfra.utils.ansible_runner as ansible_runner

testinfra_hosts = ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

NVM_DEST = "/home/ansible/.nvm"


def test_nvm_dirctory_created(host):
    f = host.file(NVM_DEST)

    assert f.is_directory


def test_nvm_dirctory_correct_permissions(host):
    f = host.file(NVM_DEST)

    assert f.user == 'ansible'
    assert f.group == 'not_ansible'
    assert f.mode == 0o755


def test_nvm_file_exists(host):
    nvm_file = NVM_DEST + '/nvm.sh'
    f = host.file(nvm_file)

    assert f.is_file


def test_nvm_file_has_correct_permissions(host):
    nvm_file = NVM_DEST + '/nvm.sh'
    f = host.file(nvm_file)

    assert f.user == 'ansible'
    assert f.group == 'not_ansible'
    assert f.mode == 0o755


def test_profile_lines_exists(host):
    f = host.file('/home/ansible/.bashrc')

    regex = r"\[ -s \"\$NVM_DIR/nvm\.sh\" ] && \\\. \"\$NVM_DIR/nvm\.sh\""
    result = re.search(regex, f.content_string)
    assert result is not None

    regex = r'export NVM_DIR=\"\$\(\[ -z \"\${XDG_CONFIG_HOME-}\" ] && printf %s \"\${HOME}/\.nvm\" \|\| printf %s \"\${XDG_CONFIG_HOME}/nvm\"\)\"'
    result = re.search(regex, f.content_string)
    assert result is not None


def test_node_version_installed(host):
    f = host.file("/home/ansible/.nvm/versions/node/v11.15.0")

    assert f.exists
    assert f.is_directory

    f = host.file("/home/ansible/.nvm/versions/node/v11.15.0/bin/node")

    assert f.exists
    assert f.is_file
