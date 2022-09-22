#!/usr/bin/env python
# -*- coding: utf-8 -*-

def is_palindrome(input_str):
    # [::-1] reverse the string: get from 0 to length by -1 step
    for forward, backward in zip(input_str, input_str[::-1]):
        if forward != backward:
            return False
    return True

def solution(input_string):
    #for i in range(-2,-5,-1):
    #    print(i) # → -2, -3, -4
    #return  # → 123

    output = input_string
    step_backwards = -1
    down_to_zero = -1 # range backwards will limit the char_position to 0
    start_position = 0 # from zero so range will return 0 the first pass
    while not is_palindrome(output):
        output = input_string
        for char_position in range(start_position, down_to_zero, step_backwards):
            print(char_position)
            output += input_string[char_position]
        start_position += 1
    return output


def main():
    case = "abcd"
    # Expected → abcba
    #case = "abcd"
    print(solution(case))

if __name__ == "__main__":
    main()

