#!/usr/bin/env python
# -*- coding: utf-8 -*-
from textwrap import wrap

def solution(code):
    chars_encoded = wrap(code, 8)
    decoded_message = ""
    for char in chars_encoded:
        char_as_int = int(char, 2)
        decoded_message += chr(char_as_int)
    return decoded_message
    

def main():
    case = "010010000110010101101100011011000110111100100001"
    print(solution(case))

if __name__ == "__main__":
    main()

