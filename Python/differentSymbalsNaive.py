#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    letters_collection = []
    for char in input_string:
        if char not in letters_collection:
            letters_collection.append(char)
    return len(letters_collection)

def main():
    case = "abb"
    print(solution(case))

if __name__ == "__main__":
    main()

