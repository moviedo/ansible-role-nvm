import pytest
import re


@pytest.fixture(scope='module')
def is_debian(host):
    data = host.ansible.get_variables()["inventory_hostname"]
    hostname = re.split(r"\d+", data)[0]
    if "ubuntu" != hostname:
        pytest.skip('hostname is not debian based')


@pytest.mark.usefixtures('is_debian')
def test_pkg_installed(host):
    item = "libssl-dev"
    pkg = host.package(item)
    assert pkg.is_installed
