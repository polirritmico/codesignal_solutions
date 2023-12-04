#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(a, b):
    for n in b:
        a.append(n)
    return a


def main():
    a = [1, 2]
    b = [3, 1, 2]
    print(solution(a, b))

if __name__ == "__main__":
    main()

