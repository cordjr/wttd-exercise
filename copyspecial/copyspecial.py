#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import sys
import re
import os
import shutil
import subprocess

"""Copy Special exercise

"""


# +++your code here+++
# Write functions and modify main() to call them
def copy_to_dir(dir_name, archives):
    cp_comand = ['cp' ]
    cp_comand.extend(archives)
    cp_comand.append(dir_name)
    subprocess.call(cp_comand)


def copy_to_zip(zip_file, archives):
    zip_comand = ['zip', '-r', zip_file]
    zip_comand.extend(archives)
    subprocess.call(zip_comand)


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)
    if todir:
        copy_to_dir(todir, args)

    if tozip:
        copy_to_zip(tozip, args)

        # +++your code here+++
        # Call your functions


if __name__ == "__main__":
    main()
