#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Consider a string containing only letters and whitespaces. It is allowed to
replace some (possibly, none) whitespaces with newline symbols to obtain a
multiline text. Call a multiline text beautiful if and only if each of its lines
(i.e. substrings delimited by a newline character) contains an equal number of
characters (only letters and whitespaces should be taken into account when
counting the total while newline characters shouldn't). Call the length of the
line the text width.

Given a string and some integers l and r (l ≤ r), check if it's possible to
obtain a beautiful text from the string with a text width that's within the
range [l, r].

Example

    For inputString = "Look at this example of a correct text", l = 5, and
    r = 15, the output should be solution(inputString, l, r) = true.

    We can replace 13th and 26th characters with '\n', and obtain the following
    multiline text of width 12:

    Look at this
    example of a
    correct text

    For inputString = "abc def ghi", l = 4, and r = 10, the output should be
    solution(inputString, l, r) = false.

    There are two ways to obtain a text with lines of equal length from this
    input, one has width = 3 and another has width = 11 (this is a one-liner).
    Both of these values are not within our bounds. """


def solution(input_str: str, min_limit: int, max_limit: int) -> bool:
    len_input_str = len(input_str)
    for width in range(min_limit, max_limit + 1):
        newline_offset = 0
        for line in range(1, len_input_str):
            position = width * line + newline_offset
            if position >= len_input_str or input_str[position] != " ":
                break
            if len_input_str - position == width + 1:
                return True
            newline_offset += 1
    return False


def main():
    string = "Look at this example of a correct text"
    lf = 5
    r = 15
    # expected = True
    print(solution(string, lf, r))


if __name__ == "__main__":
    main()
