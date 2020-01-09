"""distutils.command.install_headers

Implements the Distutils 'install_headers' command, to install C/C++ header
files to the Python include directory."""

# created 2000/05/26, Greg Ward

__revision__ = "$Id: install_headers.py 24580 2001-12-06 21:01:19Z fdrake $"

import os
from distutils.core import Command


class install_headers (Command):

    description = "install C/C++ header files"

    user_options = [('install-dir=', 'd',
                     "directory to install header files to"),
                    ('force', 'f',
                     "force installation (overwrite existing files)"),
                   ]

    boolean_options = ['force']

    def initialize_options (self):
        self.install_dir = None
        self.force = 0
        self.outfiles = []

    def finalize_options (self):
        self.set_undefined_options('install',
                                   ('install_headers', 'install_dir'),
                                   ('force', 'force'))


    def run (self):
        headers = self.distribution.headers
        if not headers:
            return

        self.mkpath(self.install_dir)
        for header in headers:
            (out, _) = self.copy_file(header, self.install_dir)
            self.outfiles.append(out)

    def get_inputs (self):
        return self.distribution.headers or []

    def get_outputs (self):
        return self.outfiles

# class install_headers
