#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input):
    max_weakness = 0
    max_weakness_matches = 0
    numbers_list = [number for number in range(1, input + 1)]
    for number in numbers_list:
        number_weakness = get_weakness(number)
        if max_weakness < number_weakness:
            max_weakness = number_weakness
            max_weakness_matches = 1
        elif max_weakness == number_weakness:
            max_weakness_matches += 1
    return [max_weakness, max_weakness_matches]


divisors_dict = {}

def get_divisors(number):
    if number in divisors_dict:
        return divisors_dict[number]
    divisors = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisors += 1
    divisors_dict[number] = divisors
    return divisors


def get_weakness(number):
    number_divisors = get_divisors(number)
    weakness = 0
    for i in range(1, number + 1):
        if number_divisors < get_divisors(i):
            weakness += 1
    return weakness


def main():
    case = 9
    #expected = [2, 2]
    print(solution(case))

if __name__ == "__main__":
    main()

