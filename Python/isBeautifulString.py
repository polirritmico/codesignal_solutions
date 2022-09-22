#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    # get a dict with char count and sort
    char_collection = {}
    for char in input_string:
        char_collection[char] = char_collection.get(char, 0) + 1
    char_collection = dict(sorted(char_collection.items()))

    previous_char = 'a'
    previous_char_count = char_collection.get('a', 0)
    for char in char_collection:
        if ord(char) - ord(previous_char) > 1:
            return False
        if char_collection[char] > previous_char_count:
            return False
        previous_char = char
        previous_char_count = char_collection[char]
    return True


def main():
    case = "bbc"
    # expected False
    case = "bbbaacdafe"
    print(solution(case))

if __name__ == "__main__":
    main()

