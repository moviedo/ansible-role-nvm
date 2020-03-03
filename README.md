Ansible Role: NVM
=========

[![Join the chat at https://gitter.im/moviedo/ansible-role-nvm](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/moviedo/ansible-role-nvm?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Build Status](https://travis-ci.org/moviedo/ansible-role-nvm.svg?branch=develop)](https://travis-ci.org/moviedo/ansible-role-nvm)

This ansible role is used to install NVM, Node Version Manager, locally within a linux box.

Requirements
------------

This role requires git, curl, build-essential, libssl-dev. Requirements are installed by this role.

Role Variables
--------------

Required Variables

  * `nvm_user` This should be the remote user that will use NVM. This value defaults to 'vagrant'.

  * `nvm_group` This optional variable is the remote group that will be used to setup permissions. If undefined, will fallback to `nvm_user`.

Optional Variables

  * `nvm_version: "v0.35.2"` NVM version to install on remote machine, it defaults to `v0.35.2`. You must specify a distinct NVM version, do **NOT** use wild cards (i.e. `v0.24.x`).
  * `nvm_node_version: "12.14.1"` Node version to install on the remote machine, it defaults to `12.14.1`. You must specify a distinct node version, do **NOT** use wild cards (i.e. `12.14.x`).

Dependencies
------------

No dependencies.

Example Playbook
----------------

    - hosts: all
      roles:
      - role: moviedo.nvm
          nvm_user: vagrant
          nvm_version: "v0.35.2"
          nvm_node_version: "12.14.1"

Other Information
-----------------

This role will also run `nvm alias default` on the specified *nvm_node_version* to [set a default Node version to be used in any new shell](https://github.com/creationix/nvm).


Contributing
-----------------

Information on how to contribute to the project.

### Setup
How to setup the project for local development.

1. Install [docker](https://docs.docker.com/docker-for-mac/install/)
1. Install project dependencies with [pipenv](https://pipenv.readthedocs.io/en/latest/) and run `pipenv install`.

### Workflow

1. Fork the repo.
1. Make your desired changes.
1. Write your tests in the molecule/default/test/test_default.py file or add test in a different file if needed.
1. Test said desired changes using [molecule](https://molecule.readthedocs.io/en/latest/).

    Molecule is used to test again different OS platforms(i.e. ubuntu, centos, etc).

1. Test against multiple ansible versions with [tox](https://tox.readthedocs.io/en/latest/).
1. Make a merge request to the project.

Check the testing section for more info on commands to run for testing locally.

### Testing Locally

Information on what commands to run in order to test locally.

#### Molecule Cammnads

1. Run the `molecule test` command to test the all scenarios.
1. Run the `molecule verify` to test against the [testinfra](https://testinfra.readthedocs.io/en/latest/index.html) test. Used to verify that the role makes the desired changes against the docker images.

##### Tox Commands

Run `tox --parallel auto` to test changes against the different ansible version that this role supports.
**Warning**: taking a few minutes to run all tests.


License
-------

MIT

Author Information
------------------

Mauro Oviedo (aka moviedo)
