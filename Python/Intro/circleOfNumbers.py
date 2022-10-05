#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n, firstNumber):
    count = n // 2
    firstNumber += count
    if firstNumber >= n:
        return firstNumber - n
    return firstNumber


def main():
    n = 10
    firstNumber = 2
    # expected 7
    print(solution(n, firstNumber))

if __name__ == "__main__":
    main()

