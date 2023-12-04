#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
An alphanumeric ordering of strings is defined as follows: each string is
considered as a sequence of tokens, where each token is a letter or a number
(as opposed to an isolated digit, as is the case in lexicographic ordering). For
example, the tokens of the string "ab01c004" are [a, b, 01, c, 004]. In
order to compare two strings, we'll first break them down into tokens and then
compare the corresponding pairs of tokens with each other (i.e. compare the
first token of the first string with the first token of the second string, etc).

Here is how tokens are compared:

    If a letter is compared with another letter, the usual alphabetical order
    applies. A number is always considered less than a letter.
    When two numbers are compared, their values are compared. Leading zeros, if
    any, are ignored.

If at some point one string has no more tokens left while the other one still
does, the one with fewer tokens is considered smaller.

If the two strings s1 and s2 appear to be equal, consider the smallest index i
such that tokens(s1)[i] and tokens(s2)[i] (where tokens(s)[i] is the ith token
of string s) differ only by the number of leading zeros. If no such i exists,
the strings are indeed equal. Otherwise, the string whose ith token has more
leading zeros is considered smaller.

Here are some examples of comparing strings using alphanumeric ordering.

"a" < "a1" < "ab"
"ab42" < "ab000144" < "ab00144" < "ab144" < "ab000144x"
"x11y012" < "x011y13"

Your task is to return true if s1 is strictly less than s2, and false otherwise.

Example

    - For s1 = "a" and s2 = "a1", the output should be solution(s1, s2) = true;
    These strings have equal first tokens, but since s1 has fewer tokens than
    s2, it's considered smaller.

    - For s1 = "ab" and s2 = "a1", the output should be solution(s1, s2) = false;
    These strings also have equal first tokens, but since numbers are considered
    less than letters, s1 is larger.

    - For s1 = "b" and s2 = "a1", the output should be solution(s1, s2) = false.
    Since b is greater than a, s1 is larger.
"""


def tokens_generator(string):
    number = ""
    for char in string:
        if char.isdigit():
            number += char
        elif number != "":
            yield number
            yield char
            number = ""
        else:
            yield char
    if number != "":
        yield number
    yield None


def solution(raw_str1: str, raw_str2: str) -> bool:
    str1_tokens = tokens_generator(raw_str1)
    str2_tokens = tokens_generator(raw_str2)
    equal_numbers = []
    for token_str1, token_str2 in zip(str1_tokens, str2_tokens):
        if token_str1 is None and token_str2 is None:
            break
        elif token_str1 is None:
            return True
        elif token_str2 is None:
            return False

        if not token_str1.isdigit() and token_str1 != token_str2:
            return token_str1 < token_str2
        if not token_str1.isdigit():
            continue
        if not token_str2.isdigit():
            return True
        if int(token_str1) != int(token_str2):
            return int(token_str1) < int(token_str2)
        equal_numbers.append((token_str1, token_str2))

    if equal_numbers != []:
        for comparation in equal_numbers:
            if len(comparation[0]) != len(comparation[1]):
                return len(comparation[0]) > len(comparation[1])

    return False


def main():
    str1 = "b"
    str2 = "a1"
    # expected = True
    print(solution(str1, str2))


if __name__ == "__main__":
    main()
