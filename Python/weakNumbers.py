#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(base_number):
    divisors_list = []
    for number in range(1, base_number + 1):
        number_divisors = 0
        for sub_number in range(1, number + 1):
            if number % sub_number == 0:
                number_divisors += 1
        divisors_list.append(number_divisors)

    weakness_list = []
    for number in range(base_number):
        number_weakness = 0
        number_divisors = divisors_list[number]
        for sub_number in range(1, number + 1):
            if number_divisors < divisors_list[sub_number]:
                number_weakness += 1
        weakness_list.append(number_weakness)

    max_weakness = max(weakness_list)
    max_weakness_count = weakness_list.count(max_weakness)
    return [max_weakness, max_weakness_count]



def main():
    case = 9
    #expected = [2, 2]
    print(solution(case))

if __name__ == "__main__":
    main()

