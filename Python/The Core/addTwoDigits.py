#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input):
    numbers = [str(char) for char in str(input)]
    sum = 0
    for char in numbers:
        sum += int(char)
    return sum


def main():
    case = 29
    print(solution(case))

if __name__ == "__main__":
    main()

