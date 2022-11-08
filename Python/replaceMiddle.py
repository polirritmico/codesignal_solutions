#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(arr):
    size = len(arr)
    if size % 2 == 0:
        l = (size - 1) // 2
        r = l + 1
        arr[l] = arr[l] + arr[r]
        arr.pop(r)
    return arr





def main():
    case = [7, 2, 2, 5, 10, 7]
    #expected = [7, 2, 7, 10, 7]
    print(solution(case))

if __name__ == "__main__":
    main()

