#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n, k):
    return n & ~(2 ** (k - 1))


def main():
    n = 37
    k = 3
    print(solution(n, k))

if __name__ == "__main__":
    main()

