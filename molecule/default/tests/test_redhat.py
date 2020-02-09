import pytest
import re


@pytest.fixture(scope='module')
def is_redhat(host):
    data = host.ansible.get_variables()["inventory_hostname"]
    hostname = re.split(r"\d+", data)[0]
    if "centos" != hostname:
        pytest.skip('hostname is not redhat based')


@pytest.mark.usefixtures('is_redhat')
def test_pkg_installed(host):
    item = "openssl-devel"
    pkg = host.package(item)
    assert pkg.is_installed
