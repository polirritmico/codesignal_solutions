#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def solution(n):
    if n == 1:
        return True
    sqrt = int(math.sqrt(n))
    for x in range(2,sqrt + 1):
        y = 2
        p = x ** y
        while p <= n:
            if p == n:
                return True
            y += 1
            p = x ** y
    return False


def main():
    case = 125
    #expected = True
    print(solution(case))

if __name__ == "__main__":
    main()

