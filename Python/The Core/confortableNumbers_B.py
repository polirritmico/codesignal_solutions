#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(l, r):
    pairs = 0
    for a in range(l, r):
        a_sum = sum([int(digit) for digit in str(a)])
        for b in range(a + 1, r + 1):
            b_sum = sum([int(digit) for digit in str(b)])
            if ((a - a_sum <= b) and (b <= a + a_sum) and
                (b - b_sum <= a) and (a <= b + b_sum)):
                   pairs += 1
    return pairs


def main():
    l = 1
    r = 9
    #expected = 20
    print(solution(l, r))

if __name__ == "__main__":
    main()

