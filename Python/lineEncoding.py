#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    output = ""
    prev_char = input_string[0]
    prev_char_count = 1
    for i in range(1, len(input_string)):
        current_char = input_string[i]
        if current_char == prev_char:
            prev_char_count += 1
        elif prev_char_count > 1:
            output += str(prev_char_count) + prev_char
            prev_char_count = 1
        else:
            output += prev_char
        prev_char = current_char

    if prev_char_count == 1:
        output += prev_char
    else:
        output += str(prev_char_count) + prev_char
    return output


def main():
    case = "aab"
    print(solution(case))

if __name__ == "__main__":
    main()

