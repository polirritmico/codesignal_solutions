#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(number):
    if number < 10:
        return number
    remainder = number % 10
    number -= remainder
    if remainder > 4:
        number += 10
    return solution(number//10) * 10

        

def main():
    case = 124
    #expected = 20
    print(solution(case))

if __name__ == "__main__":
    main()

