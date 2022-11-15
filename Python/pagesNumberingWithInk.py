#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(current, number_of_digits):
    while number_of_digits >= 0:
        number_of_digits -= len(str(current))
        current += 1
    return current - 2


def main():
    current = 21
    number_of_digits = 5
    #expected = 22
    print(solution(current, number_of_digits))

if __name__ == "__main__":
    main()

