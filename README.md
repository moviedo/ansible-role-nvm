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

License
-------

MIT

Author Information
------------------

Mauro Oviedo (aka moviedo)
