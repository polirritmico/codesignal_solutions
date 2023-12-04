#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n, m):
    return ~(m ^ n) & -(~(m ^ n))


def main():
    n = 10
    m = 11
    #expected = 2
    print(solution(n, m))

if __name__ == "__main__":
    main()

