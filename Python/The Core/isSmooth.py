#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input):
    size = len(input)
    is_odd = size % 2 != 0
    if is_odd:
        index = (size - 1) // 2
        middle = input[index]
    else:
        l = (size - 1) // 2
        r = l + 1
        middle = input[l] + input[r]

    return input[0] == input[-1] == middle



def main():
    # case = [7, 2, 2, 5, 10, 7]
    # case = [4, 2]
    case = [-12, 34, 40, -5, -12, 4, 0, 0, -12]
    #expected = True
    print(solution(case))

if __name__ == "__main__":
    main()

