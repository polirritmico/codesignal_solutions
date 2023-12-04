#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You're given a substring s of some cyclic string. What's the length of the
smallest possible string that can be concatenated to itself many times to obtain
this cyclic string?

Example

For s = "cabca", the output should be
solution(s) = 3.

"cabca" is a substring of a cycle string "abcabcabcabc..." that can be obtained
by concatenating "abc" to itself. Thus, the answer is 3. """


def solution(substring: str) -> int:
    len_substring = len(substring)
    pattern = ""
    current_len = 0
    for char in substring:
        current_pattern = pattern + char
        current_len += 1
        repetitions = len_substring // current_len + 1
        if substring in current_pattern * repetitions:
            return len(current_pattern)
        pattern += char
    return len_substring


def main():
    case = "cabca"
    # expected = 3
    print(solution(case))


if __name__ == "__main__":
    main()
