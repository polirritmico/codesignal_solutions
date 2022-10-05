#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(inputArray):
    moves_counter = 0
    previous = inputArray[0]
    for i in range(1, len(inputArray)):
        number = inputArray[i]
        diff = 0
        if number <= previous:
            diff = previous - number + 1
            moves_counter += diff
        previous = number + diff
    return moves_counter


def main():
    case = [1, 1, 1] # 3
    case = [-1000, 0, -2, 0] # 5
    print(solution(case))

if __name__ == "__main__":
    main()

