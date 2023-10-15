#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You are given n rectangular boxes, the ith box has the length lengthi, the width
widthi and the height heighti. Your task is to check if it is possible to pack
all boxes into one so that inside each box there is no more than one another box
(which, in turn, can contain at most one another box, and so on). More formally,
your task is to check whether there is such sequence of n different numbers pi
(1 ≤ pi ≤ n) that for each 1 ≤ i < n the box number pi can be put into the box
number pi+1.
A box can be put into another box if all sides of the first one are
less than the respective ones of the second one. You can rotate each box as you
wish, i.e. you can swap its length, width and height if necessary.

Example

    - For length = [1, 3, 2], width = [1, 3, 2], and height = [1, 3, 2], the
    output should be solution(length, width, height) = true;
    - For length = [1, 1], width = [1, 1], and height = [1, 1], the output
    should be solution(length, width, height) = false;
    - For length = [3, 1, 2], width = [3, 1, 2], and height = [3, 2, 1], the
    output should be solution(length, width, height) = false.

"""


def solution(length: list[int], width: list[int], height: list[int]) -> bool:
    sorted_boxes = sorted(list(zip(length, width, height)), key=lambda x: sum(x))
    previous_box = sorted(sorted_boxes.pop(0))
    for current_box in sorted_boxes:
        current_box = sorted(current_box)
        if any(current <= prev for current, prev in zip(current_box, previous_box)):
            return False
        previous_box = current_box
    return True


def main():
    length = [3, 1, 2]
    width = [3, 1, 2]
    height = [3, 2, 1]
    # expected = False
    print(solution(length, width, height))


if __name__ == "__main__":
    main()
