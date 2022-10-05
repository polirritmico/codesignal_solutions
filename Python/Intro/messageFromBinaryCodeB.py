#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Documentation for bytes.decode(), int.to_bytes() and int() at:
- https://docs.python.org/3/library/stdtypes.html#bytes.decode
- https://docs.python.org/3/library/stdtypes.html?highlight=to_bytes#int.to_bytes
- https://docs.python.org/3/library/functions.html#int
"""

def solution(code):
    chars_in_code = len(code) // 8
    code_as_int = int(code, 2)
    code_as_bytes = code_as_int.to_bytes(chars_in_code, byteorder="big")
    decoded_message = code_as_bytes.decode(encoding="ascii")
    return decoded_message
    

def main():
    case = "010010000110010101101100011011000110111100100001"
    print(solution(case))

if __name__ == "__main__":
    main()

