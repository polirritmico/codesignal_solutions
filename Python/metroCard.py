#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(last_number_of_days):
    # February, April, June, September and November
    if last_number_of_days == 28 or last_number_of_days == 30: 
        return [31]
    # Other number of days could be any month
    return [28, 30, 31]


def main():
    case = 31
    print(solution(case))

if __name__ == "__main__":
    main()

