#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Court is in session. We got a group of witnesses who have all taken an oath to
tell the truth. The prosecutor is pointing at the defendants one by one and
asking each witnesses a simple question - "guilty or not?". The witnesses are
allowed to respond in one of the following three ways:

    I am sure he/she is guilty.
    I am sure he/she is innocent.
    I have no idea.

The prosecutor has a hunch that one of the witnesses might not be telling the
truth so she decides to cross-check all of their testimonies and see if the
information gathered is consistent, i.e. there are no two witnesses A and B and
a defendant C such that A says C is guilty while B says C is innocent.

Example

    For

    evidences = [[ 0, 1, 0, 1],
                 [-1, 1, 0, 0],
                 [-1, 0, 0, 1]]

    the output should be
    solution(evidences) = true;

    For

    evidences = [[ 1, 0],
                 [-1, 0],
                 [ 1, 1],
                 [ 1, 1]]

    the output should be
    solution(evidences) = false.

[input] array.array.integer evidences

-------------------------------------------------------------------------------

evidences: 2-dimensional array of integers representing the set of testimonials.
evidences[i][j] is the testimonial of the ith witness on the jth defendant. -1
means "innocent", 0 means "no idea", and 1 means "guilty".

"""


def solution(evidences: list[list[int]]) -> bool:
    for defendant in range(len(evidences[0])):
        searching_first_testimony = True
        for witness in range(len(evidences)):
            current = evidences[witness][defendant]
            if current == 0:
                continue
            if searching_first_testimony:
                searching_first_testimony = False
                testimony = current
            elif current != testimony:
                return False
    return True


def main():
    case = [[0, 1, 0, 1], [-1, 1, 0, 0], [-1, 0, 0, 1]]
    # expected = True
    print(solution(case))


if __name__ == "__main__":
    main()
