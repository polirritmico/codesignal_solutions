#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(deposit, rate, threshold):
    years_to_wait = 0
    current_money = deposit
    while current_money < threshold:
        current_money *= (rate / 100) + 1
        years_to_wait += 1
    return years_to_wait


def main():
    deposit = 100
    rate = 20
    threshold = 170
    print(solution(deposit, rate, threshold))

if __name__ == "__main__":
    main()

