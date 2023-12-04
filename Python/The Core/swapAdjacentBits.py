#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n):
    # 2863311530 → 10101010... (32)
    # 1431655765 → 01010101... (32)
    return ((2863311530 & n) >> 1) | ((1431655765 & n) << 1)



def main():
    case = 13
    #expected = 14
    print(solution(case))

if __name__ == "__main__":
    main()

