#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def solution(n):
    factorial = 0
    i = 0
    while factorial < n:
        factorial = math.factorial(i)
        i += 1
    return factorial



def main():
    case = 17
    #expected = 24
    print(solution(case))

if __name__ == "__main__":
    main()

