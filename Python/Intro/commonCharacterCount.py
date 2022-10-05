#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(s1, s2):
    grp1 = dict()
    grp2 = dict()
    output = 0
    for char in s1:
        grp1[char] = grp1.get(char, 0) + 1
    for char in s2:
        grp2[char] = grp2.get(char, 0) + 1
    for char in grp1:
        if char in grp2:
            output += min(grp1[char], grp2[char])
    return output


def main():
    s1 = "aabcc"
    s2 = "adcaa"
    print(solution(s1, s2))

if __name__ == "__main__":
    main()

