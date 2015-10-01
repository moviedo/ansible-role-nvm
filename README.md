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

  * `nvm_version: "v0.24.1"` NVM version to install on remote machine, it defaults to `v0.24.1`. You must specify a distinct NVM version, do NOT use wild cards (i.e. `v0.24.x`).
  * `nvm_node_version: "0.12.2"` Node version to install on the remote machine, it defaults to `0.12.2`. You must specify a distinct node version, do NOT use wild cards (i.e. `0.12.x`).
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
          nvm_version: "v0.24.1"
          nvm_node_version: "0.12.2"
          nvm_npm_pkgs:
            - pkg: bower
              version: 1.4.x
            - pkg: grunt-cli
              version: "*"
            - pkg: gulp
              version: "*"
        

License
-------

MIT

Author Information
------------------

Mauro Oviedo (aka moviedo)
