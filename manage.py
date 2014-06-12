#!/usr/bin/env python

import os
import sys


__requires__ = ['Django >= 1.5,< 1.6']
import pkg_resources

from django.core.management import execute_from_command_line  # noqa

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE",
                          "openstack_dashboard.settings")
    execute_from_command_line(sys.argv)
