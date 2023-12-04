#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
def solution(n, m):
    return n + m + math.gcd(n, m) - 2


def main():
    n = 3
    m = 4
    #expected = 6
    print(solution(n, m))

if __name__ == "__main__":
    main()

