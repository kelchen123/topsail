import os

import topsail
from topsail.repo_scripts.validate_role_files import main as role_files_main
from topsail.repo_scripts.validate_role_vars_used import main as role_vars_used_main

import topsail._ansible_default_config

class Repo:
    """
    Commands to perform consistency validations on this repo itself
    """
    @staticmethod
    def validate_role_files():
        """
        Ensures that all the Ansible variables defining a
        filepath (`roles/`) do point to an existing file.
        """
        exit(role_files_main())

    @staticmethod
    def validate_role_vars_used():
        """
        Ensure that all the Ansible variables defined are
        actually used in their role (with an exception for symlinks)
        """
        exit(role_vars_used_main())

    @staticmethod
    def validate_no_wip():
        """
        Ensures that none of the commits have the WIP flag in their
        message title.
        """
        exit(os.system("topsail/repo_scripts/validate_no_wip.sh"))


    @staticmethod
    def validate_no_broken_link():
        """
        Ensure that all the symlinks point to a file
        """

        has_broken_links = os.system("find . -type l -exec file {} \\; | grep 'broken symbolic link'") == 0
        exit(1 if has_broken_links else 0)

    @staticmethod
    def generate_ansible_default_settings():
        """
        Generate the 'defaults/main/config.yml' file of the Ansible roles, based on the Python definition.
        """
        topsail._ansible_default_config.generate_all(topsail.Toolbox())
        exit(0)
