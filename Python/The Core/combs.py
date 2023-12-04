#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Miss X has only two combs in her possession, both of which are old and miss a
tooth or two. She also has many purses of different length, in which she carries
the combs. The only way they fit is horizontally and without overlapping. Given
teeth' positions on both combs, find the minimum length of the purse she needs
to take them with her.

It is guaranteed that there is at least one tooth at each end of the comb.
It is also guaranteed that the total length of two strings is smaller than 32.
Note, that the combs can not be rotated/reversed.

Example

For comb1 = "*..*" and comb2 = "*.*", the output should be
solution(comb1, comb2) = 5.

Although it is possible to place the combs like on the first picture, the best
way to do this is either picture 2 or picture 3.

https://codesignal.s3.amazonaws.com/uploads/1664318500/cbs.png?raw=true

"""


def solution(comb1: str, comb2: str) -> int:
    len_comb1 = len(comb1)
    len_comb2 = len(comb2)
    min_len = len_comb1 + len_comb2
    for offset in range(2 - len_comb2, len_comb1):
        for idx_1 in range(len_comb1):
            if offset < 0:
                idx_2 = idx_1 + 1
            else:
                idx_2 = idx_1
                idx_1 += offset

            if comb1[idx_1] == "*" and comb2[idx_2] == "*":
                break
            if idx_2 == len_comb2 - 1:
                offset = abs(offset)
                if offset + len_comb2 >= len_comb1:
                    current_len = len_comb1 + offset
                else:
                    current_len = len_comb1
                min_len = min(min_len, current_len)
                break
            if idx_1 == len_comb1 - 1:
                current_len = offset + len_comb2
                min_len = min(min_len, current_len)
                break
    return min_len


def main():
    comb1 = "*..*"
    comb2 = "*.*"
    # expected = 5
    print(solution(comb1, comb2))


if __name__ == "__main__":
    main()
