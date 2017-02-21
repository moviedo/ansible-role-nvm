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

  * `nvm_user` Remote user. This value defaults to 'vagrant'.

Optional Variables

  * `nvm_version: "v0.33.0"` NVM version to install on remote machine, it defaults to `v0.33.0`. You must specify a distinct NVM version, do NOT use wild cards (i.e. `v0.24.x`).
  * `nvm_node_version: "6.9.5"` Node version to install on the remote machine, it defaults to `6.9.5`. You must specify a distinct node version, do NOT use wild cards (i.e. `6.9.x`).
  * `nvm_npm_pkgs: []` A list of **global** npm packages to be installed on remote machine. It defaults to an empty list. Packages should be yaml dictionary with keys `pkg`, representing the package name, and `version`, representing the package version, as shown below.
  ```
  nvm_npm_pkgs:
    - pkg: bower
      version: 1.4.x
  ```

Dependencies
------------

No dependencies.

Example Playbook
----------------

    - hosts: server
      roles:
      - role: nvm
          nvm_user: vagrant
          nvm_version: "v0.33.0"
          nvm_node_version: "6.9.5"
          nvm_npm_pkgs:
            - pkg: bower
              version: 1.4.x
            - pkg: brunch
              version: "*"
            - pkg: yarn
              version: "*"

Other Information
-----------------

This role will also run `nvm alais default` on the specified *nvm_node_version* to [set a default Node version to be used in any new shell](https://github.com/creationix/nvm).

Testing
-------

This project comes with a Vagrantfile, this is a fast and easy way to test changes to the role, fire it up with `vagrant up`.

See [vagrant docs](https://docs.vagrantup.com/v2/) for getting setup with vagrant.

Once your VM is up, you can provision the VM using `vagrant provision` or `vagrant up --provision`.

If you want to toy with the test play, see [tests/playbook.yml](./tests/playbook.yml), and change the variables in [tests/vars.yml](./tests/vars.yml).

If you are contributing, please first test your changes within the vagrant environment, (using at least one of the targeted distribution(s) ubuntu/xenial64), and if possible, ensure your change is covered in the tests found in [.travis.yml](./.travis.yml) if applicable.

If you wish to change the Vagrant OS distribution, please update `config.vm.box`, this can be found in the accompanying [Vagrantfile](./Vagrantfile).

License
-------

Licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

Author Information
------------------

Mauro Oviedo (aka moviedo)
