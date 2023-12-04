#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(a, b, marbles):
    money = 0
    for marble in range(marbles):
        money += a * b
        a += 1
        b += 1
    return money



def main():
    a = 1
    b = 2
    n = 2
    #expected = 8
    print(solution(a, b, n))

if __name__ == "__main__":
    main()

