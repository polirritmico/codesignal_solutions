#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(statues):
    # smallest = min(statues)
    # biggest = max(statues)
    # current_amount = len(statues) 
    # expected_amount = biggest - smallest + 1
    # return expected_amount - current_amount
    return (max(statues) - min(statues) + 1) - len(statues)


def main():
    case = [6, 2, 3, 8]
    #expected = 3
    print(solution(case))

if __name__ == "__main__":
    main()

