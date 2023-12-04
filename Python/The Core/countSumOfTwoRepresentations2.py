#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n, l, r):
    permutations = 0
    for i in range(l, r + 1):
        A = i
        B = n - i
        if l <= A and A <= B and B <= r:
            permutations += 1
    return permutations


def main():
    n = 6
    l = 2
    r = 4
    # expected = 2
    print(solution(n, l, r))

if __name__ == "__main__":
    main()

