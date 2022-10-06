#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n, firstNumber):
    output = firstNumber + n // 2
    if output >= n:
        return output - n
    return output


def main():
    n = 6
    firstNumber = 3
    #expected 0
    print(solution(n, firstNumber))

if __name__ == "__main__":
    main()

