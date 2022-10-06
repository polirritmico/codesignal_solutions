#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(divisor, bound):
    for number in range(bound, 0, -1):
        if number % divisor == 0:
            return number


def main():
    divisor = 7
    bound = 100
    # expected 98
    print(solution(divisor, bound))

if __name__ == "__main__":
    main()

