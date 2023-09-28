#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Consider the following ciphering algorithm:

    For each character replace it with its code.
    Concatenate all of the obtained numbers.

Given a ciphered string, return the initial one if it is known that it consists
only of lowercase letters.

Note: here the character's code means its decimal ASCII code, the numerical
representation of a character used by most modern programming languages.

Example

For cipher = "10197115121", the output should be
solution(cipher) = "easy".

Explanation: charCode('e') = 101, charCode('a') = 97, charCode('s') = 115 and
charCode('y') = 121.
"""


def solution(encoded_msg: str) -> str:
    decoded_msg = ""
    current_letter_value = 0
    for char in encoded_msg:
        current_letter_value = (10 * current_letter_value) + ord(char) - 48
        if current_letter_value >= 97 and current_letter_value <= 122:
            decoded_msg += chr(current_letter_value)
            current_letter_value = 0
    return decoded_msg


def main():
    case = "10197115121"
    # expected = "easy"
    print(solution(case))


if __name__ == "__main__":
    main()
