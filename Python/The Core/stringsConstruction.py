#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(target_str, letters_to_use):
    letters_counter = {}
    for char in letters_to_use:
        letters_counter[char] = letters_counter.get(char, 0) + 1
    target_letters = {}
    for char in target_str:
        target_letters[char] = target_letters.get(char, 0) + 1

    constructed_targets_counter = 0

    while True:
        for char in target_str:
            if char not in letters_counter:
                return constructed_targets_counter
            letters_counter[char] -= 1
            if letters_counter[char] == 0:
                del letters_counter[char]
        constructed_targets_counter += 1


def main():
    a = "ab"
    b = "b"
    print(solution(a, b))


if __name__ == "__main__":
    main()
