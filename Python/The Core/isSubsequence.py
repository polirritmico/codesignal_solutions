#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement the missing code, denoted by ellipses. You may not modify the
pre-existing code.

Given a string s, determine if it is a subsequence of a given string t.

Example

    For t = "CodeSignal" and s = "CoSi", the output should be
    solution(t, s) = true;

    For t = "CodeSignal" and s = "cosi", the output should be
    the output should be
    solution(t, s) = false.


"""
import re


def solution(t, s):
    pattern = ""
    for ch in s:
        pattern += re.escape(ch) + r".*"
    print(pattern)
    return re.search(pattern, t) is not None


def main():
    t = "he sd.f dsk e8.sd??l**23, 23,f.s++83+"
    s = "h  8.?*3+"
    # expected = True
    print(solution(t, s))


if __name__ == "__main__":
    main()
