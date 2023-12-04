#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(a):
    binary = ""
    for i in range(len(a)):
        binary = format(a[i], "08b") + binary
    return int(binary, 2)


def main():
    case = [187, 99, 42, 43]
    #expected = 724198331
    print(solution(case))

if __name__ == "__main__":
    main()

