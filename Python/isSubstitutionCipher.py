#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(string1: str, string2: str) -> bool:
    cipher_alphabet = {}
    for char1, char2 in zip(string1, string2):
        if char1 in cipher_alphabet:
            if cipher_alphabet[char1] != char2:
                return False
        else:
            if char2 in cipher_alphabet.values():
                return False
            cipher_alphabet[char1] = char2
    return True


def main():
    string1 = "aaxyaa"
    string2 = "aazzaa"
    # expected = False
    print(solution(string1, string2))


if __name__ == "__main__":
    main()
