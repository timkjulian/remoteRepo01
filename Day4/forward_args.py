#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/12/2021
Purpose: Forward arguments
"""


def trace(f, *args, **kwargs):
    print(f'args={args}')
    print(f'kwargs={kwargs}')
    result = f(*args, **kwargs)
    print(f'result {result}')
    return result


def test_trace():
    print(int("ff", base=16))
    trace(int, "ff", base=16)


# --------------------------------------------------
def main():
    """Make your noise here"""
    test_trace()


# --------------------------------------------------
if __name__ == '__main__':
    main()
