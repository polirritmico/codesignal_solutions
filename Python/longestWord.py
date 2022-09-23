#!/usr/bin/env python
# -*- coding: utf-8 -*-

def not_a_letter(char):
    if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return False
    return True


def solution(text):
    max_count = 0
    max_string = ""
    count = 0
    string = ""
    for char in text:
        if not_a_letter(char):
            count = 0
            string = ""
            continue

        string += char
        count += 1
        if count > max_count:
            max_string = string
            max_count = count

    return max_string
        

def main():
    case = "4a aa aaa"
    print(solution(case))

if __name__ == "__main__":
    main()

