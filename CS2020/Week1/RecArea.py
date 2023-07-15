#!/usr/bin/env python3
"""
Author : Zaki Rucker <zakirucker@mac.com>
Date   : 2023-07-15
Purpose: calculate the area of a rectangle
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='calculate the area of a rectangle',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    print('Height: ')
    h = input()
    height = int(h)
    print('Length: ')
    l = input()
    length = int(l)
    print('The area of the rectangle is',length * height)


# --------------------------------------------------
if __name__ == '__main__':
    main()
