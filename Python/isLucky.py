#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(n):
    string = str(n)
    length = len(string)
    half = length // 2
    first_half = 0
    second_half = 0
    for i in range(0, half):
        first_half += int(string[i])
    for i in range(half, length):
        second_half += int(string[i])
    if first_half == second_half:
        return True
    return False






def main():
    print(solution(1230))

if __name__ == "__main__":
    main()

