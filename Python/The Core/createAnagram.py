#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(base: str, target: str) -> int:
    if len(base) != len(target):
        raise ValueError()

    target_letters = {}
    for letter in target:
        target_letters[letter] = 1 + target_letters.get(letter, 0)

    needed_changes = 0
    for letter in base:
        if letter not in target_letters.keys():
            needed_changes += 1
            continue
        target_letters[letter] -= 1
        if target_letters[letter] == 0:
            del target_letters[letter]
    return needed_changes


def get_letters(word: str) -> dict[str, str]:
    output = {}
    for letter in word:
        output[letter] = output.get(letter, 0) + 1
    return output


def main():
    s = "AABAA"
    t = "BBAAA"
    # Expected 1
    print(solution(s, t))


if __name__ == "__main__":
    main()
