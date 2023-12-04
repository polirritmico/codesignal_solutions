#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(a, b, c) -> bool:
    if (a + b == c) or (a - b == c) or (a * b == c) or (a / b == c):
        return True
    return False


def main():
    a = 2
    b = 3
    c = 5
    #expected True
    print(solution(a, b, c))

if __name__ == "__main__":
    main()

