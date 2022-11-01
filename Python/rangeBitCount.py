#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(a, b):
    count_of_1s = 0
    for number in range(a, b + 1):
        count_of_1s += bin(number).count("1")
    return count_of_1s


def main():
    a = 2
    b = 7
    #expected = 11
    print(solution(a, b))

if __name__ == "__main__":
    main()

