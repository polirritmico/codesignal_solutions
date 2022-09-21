#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(inputArray) -> list:
    longest = 0
    output = []
    for string in inputArray:
        length = len(string)
        if length > longest:
            longest = length
            output.clear()
            output.append(string)
        elif length == longest:
            output.append(string)
    return output



def main():
    array_string = ["aba", "aa", "ad", "vcd", "aba"]
    solution()


if __name__ == "__main__":
    main()
