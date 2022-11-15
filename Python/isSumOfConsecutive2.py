#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n):
    consecutives_sum = 0
    numbers = [1, 2]

    while True:
        total = sum(numbers)
        if total > n:
            return consecutives_sum
        while total <= n:
            if total == n:
                consecutives_sum += 1
            next(numbers)
            total = sum(numbers)
        add_number(numbers)


def next(array):
    for i in range(len(array)):
        array[i] += 1


def add_number(array):
    current_size = len(array)
    array.clear()
    for i in range(current_size + 1):
        array.append(i + 1)


def main():
    case = 9
    #expected = 2; 4+5, 2+3+4
    print(solution(case))


if __name__ == "__main__":
    main()

