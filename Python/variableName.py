#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(name):
    if name[0].isdecimal():
        return False
    valid = "0123456789_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in name:
        if char not in valid:
            return False
    return True

def main():
    case = "qq-qa"
    #case = "var_1__Int"
    print(solution(case))

if __name__ == "__main__":
    main()

