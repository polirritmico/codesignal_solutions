#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_array, step):
    removed_elements = 0
    for i in range(1, len(input_array) + 1):
        if i % step == 0:
            removed_elements += 1
            input_array.pop(i - removed_elements)
    return input_array
    

def main():
    case = [2, 4, 6, 8, 10]
    k = 2
    print(solution(case, k))

if __name__ == "__main__":
    main()

