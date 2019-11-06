#!/usr/bin/env python3

import sys
import os

num_arg = len(sys.argv)
arguments = sys.argv[1:]


def get_name_ext_of_file(s):
    """Returns the name of a file with its extension"""
    pieces = s.split(os.path.sep)
    name_of_file = pieces[len(pieces)-1]
    return name_of_file


def get_name_and_extension(s):
    """Returns the name and extension of a filename as a tuple. It takes a string with a path to a file."""
    f_name_ext = get_name_ext_of_file(s)
    pieces = f_name_ext.split('.')
    if len(pieces) == 1:  # No extension
        fname = pieces[0]
        extension = ''
        return fname, extension
    extension = pieces[len(pieces)-1]
    if len(pieces) > 2:  # Dot in the middle of filename
        fname = '.'.join(pieces[:len(pieces)-1])
    else:
        fname = pieces[0]
    return fname, extension


def check_arguments(lenarg):
    """Verifies that the number of arguments is correct"""
    if lenarg < 2:
        print("Missing arguments. You must provide a file to copy. Received {} arguments".format(lenarg - 1))
        raise ValueError
    elif lenarg > 2:
        print("Too many arguments. You must provide a file path to copy. Received {} arguments".format(lenarg - 1))
        raise ValueError
    elif lenarg == 2:
        print("Opening file {} to copy...".format(arguments[0]))


def copy(file_path):
    file_name, file_extension = get_name_and_extension(file_path)
    infile = open(file_path, 'rb')
    outfile = open(file_name + '-copy' + '.' + file_extension, 'wb')

    print('Copying...')
    while True:
        buff = infile.read(32768)
        if buff:
            outfile.write(buff)
        else:
            print('Completed successfully!')
            break


def main():
    check_arguments(num_arg)
    copy(arguments[0])


if __name__ == '__main__':
    main()