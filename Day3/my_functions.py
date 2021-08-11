#!/usr/bin/env python3
"""
Author : hvalle <me@wsu.com>
Date   : 8/11/2021
Purpose: Discuss callable objects, callable instances and lambdas
"""
import socket


class Resolver:
    def __init__(self):
        self._cache = {}

    def __call__(self, host):
        if host not in self._cache:
            self._cache[host] = socket.gethostbyname(host)
        return self._cache

    def clear(self):
        self._cache.clear()

    def has_host(self, host):
        return host in self._cache

def test_Resolver():
    resolve = Resolver()
    print(resolve('weber.edu'))
    print(resolve('google.com'))
    print(resolve.has_host('weber.edu'))
    resolve.clear()
    print(resolve('google.com'))
    print(resolve.__call__('yahoo.com'))
    # Call the class itself
    print(Resolver)
    # Call the instance
    print(resolve)


def sequence_class(immutable):
    # if immutable:
    #     cls = tuple
    # else:
    #     cls = list
    # return cls
    return tuple if immutable else list


def test_sequence_class():
    seq = sequence_class(immutable=True)
    t = seq('Ogden')
    print(t)
    print(type(t))
    seq = sequence_class(immutable=False)
    t = seq('Ogden')
    print(t)
    print(type(t))


# --------------------------------------------------
def main():
    """Make your noise here"""
    # test_Resolver()

    test_sequence_class()





# --------------------------------------------------
if __name__ == '__main__':
    main()
