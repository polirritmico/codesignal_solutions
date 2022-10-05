#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(digits):
    output = 9
    for i in range(1, digits):
        output += 9 * 10 ** i
    return output
        

def main():
    case = 0
    print(solution(case))

if __name__ == "__main__":
    main()

