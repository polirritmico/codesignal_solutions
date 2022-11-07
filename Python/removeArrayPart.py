#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input, l, r):
    return input[0:l] + input[r+1:]


def main():
    case = [2, 4, 10, 1]
    l = 0
    r = 2
    #expected 1
    print(solution(case, l, r))

if __name__ == "__main__":
    main()

