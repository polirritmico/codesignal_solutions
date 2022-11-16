#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(l, r):
    # Get valid confortable numbers for each number in range
    confortable_numbers = []
    for number in range(l, r + 1):
        digits_sum = sum([int(digit) for digit in str(number)])
        confortable_list = []
        for inner_number in range(number - digits_sum, (number + digits_sum + 1)):
            if inner_number <= r and inner_number >= l:
                confortable_list.append(inner_number)
        confortable_numbers.append((number, confortable_list))

    # Check valid pairs
    pairs = 0
    for i in range(len(confortable_numbers)):
        a = confortable_numbers[i][0]
        a_confortable_list = confortable_numbers[i][1]
        for k in range(i + 1, len(confortable_numbers)):
            b = confortable_numbers[k][0]
            b_confortable_list = confortable_numbers[k][1]
            if b in a_confortable_list and a in b_confortable_list:
                pairs += 1

    return pairs


def main():
    l = 1
    r = 9
    #expected = 20
    print(solution(l, r))

if __name__ == "__main__":
    main()

