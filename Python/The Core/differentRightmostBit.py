#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n, m):
    return (m ^ n) & -(m ^ n)
    # Get different bits → m ^ n
    # Get right most 1 bit → x & -x


def main():
    n = 11
    m = 13
    solution(m, n)

if __name__ == "__main__":
    main()

