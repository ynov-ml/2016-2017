#!/usr/bin/python

"""Compute a permutation of an input file.

The input file contains one URL per line.

Output each URL followed by two URL's chosen at random without
replacement.

"""

from __future__ import print_function
import argparse
import numpy as np
import re

github_url_body_1 = re.compile(r'^https://github.com')
github_url_body_2 = re.compile(r'\.git$')

def url_body(url):
    """Return url without https://github.com/ and stripped of .git.
    """
    base = re.sub(github_url_body_1, '', url)
    return re.sub(github_url_body_2, '', base)

def print_permuted_file(filename):
    """Read the file, permute, and output permutation.

    The output format is suitable inclusion in a markdown file.
    """
    with open(filename, 'r') as f_ptr:
        lines = [s.strip() for s in f_ptr.readlines()]
    permuted_lines = np.random.permutation(lines)
    for triple in zip(permuted_lines,
                      np.roll(permuted_lines, 1),
                      np.roll(permuted_lines, 2)):
        format_string = '*[{reviewer}]({reviewer_url})*\n' + \
                        '* [{target1}]({target1_url})\n' +   \
                        '* [{target2}]({target2_url})\n\n'
        print(format_string.format(
            reviewer=url_body(triple[0]), reviewer_url=triple[0],
            target1_url=triple[1], target1=url_body(triple[1]),
            target2_url=triple[2], target2=url_body(triple[2])))

def main():
    """
    Parse args and do our stuff.
    """
    parser = argparse.ArgumentParser()
    named_args = parser.add_argument_group('arguments')
    named_args.add_argument('--filename', type=str, required=True,
                            help='input file')
    args = parser.parse_args()
    print_permuted_file(args.filename)

if __name__ == '__main__':
    main()
