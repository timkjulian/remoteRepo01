#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/31/2021
Purpose:
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('item',
                        metavar='str',
                        nargs='+',       # one or more arguments
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make your noise here"""
    args = get_args()
    items = args.item
    # check if the list needs to be sorted
    if args.sorted:
        items.sort()
    # prepare list to print, Hints: len(), join(), sort()
    num = len(items)
    bringing = ''
    # 1 Item, just print item
    if num == 1:
        bringing = items[0]
    # 2 Items: item1 and item2
    elif num == 2:
        bringing = ' and '.join(items)
    # 3 or more Items: item1, item2, itemX, and itemLast
    else:
        items[-1] = 'and ' + items[-1]
        bringing = ', '.join(items)
    # Print info
    print(f'You are bringing {bringing}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
