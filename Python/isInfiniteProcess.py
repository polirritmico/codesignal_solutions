#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(a, b):
    # while a != b
    #     a += 1
    #     b -= 1
    return (a > b) or ((a - b) % 2 != 0)

def main():
    a = 2
    b = 6
    print(solution(a, b))
    #expected false

if __name__ == "__main__":
    main()

