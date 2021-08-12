#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/12/2021
Purpose: Continue discussion on extended arguments
"""


def print_args(arg1, arg2, *args, kwarg1, kwarg2, **kwargs):
    """
    Print argument info
    :param arg1: First required position argument
    :param arg2: Second required position argument
    :param args: Optional list of positional arguments (LAST OF POSITIONAL)
    :param kwarg1: First required Keyword argument
    :param kwarg2: Second required Keyword argument
    :param kwargs: Optional list of Keyword argument (MUST BE LAST)
    :return:
    """
    print(arg1)
    print(arg2)
    print(args)
    print(kwarg1)
    print(kwarg2)
    print(kwargs)

# --------------------------------------------------
def main():
    """Make your noise here"""
    print_args(1, 2, kwarg1='hello', kwarg2='there')    # minimum to run
    print_args(1, 2, 3, 4, kwarg1='hello', kwarg2='there')    # two optional positional params
    print_args(1, 2, 3, 4,
               kwarg1='hello', kwarg2='there',
               fname='Waldo', lname='Weber')    # two optional positional and keyword params



# --------------------------------------------------
if __name__ == '__main__':
    main()
