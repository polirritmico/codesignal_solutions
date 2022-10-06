#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(min1, min2_10, min11, money):
    current_rate = min1
    call = 0
    while True:
        money -= current_rate
        if money < 0:
            return call
        call += 1

        if call == 1:
            current_rate = min2_10
        if call == 10:
            current_rate = min11


def main():
    min1 = 2 # 2
    min2_10 = 1 # 9; 11
    min11 = 10 # 11; 21
    s = 21
    # expected 14
    print(solution(min1, min2_10, min11, s))

if __name__ == "__main__":
    main()

