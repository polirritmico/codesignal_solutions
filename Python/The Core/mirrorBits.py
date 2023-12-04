#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(number):
    string_binary = format(number, "16b")
    reversed_string = string_binary[::-1]
    reversed_binary = int(reversed_string, 2)
    return reversed_binary
    

def main():
    case = 97
    #expected = 67
    print(solution(case))

if __name__ == "__main__":
    main()

