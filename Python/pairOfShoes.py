#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Yesterday you found some shoes in the back of your closet. Each shoe is
described by two values:

    type indicates if it's a left or a right shoe;
    size is the size of the shoe.

Your task is to check whether it is possible to pair the shoes you found in such
a way that each pair consists of a right and a left shoe of an equal size.

Example

    For

    shoes = [[0, 21],
             [1, 23],
             [1, 21],
             [0, 23]]

    the output should be
    solution(shoes) = true;

    For

    shoes = [[0, 21],
             [1, 23],
             [1, 21],
             [1, 23]]

    the output should be
    solution(shoes) = false.


"""


def solution(founded_shoes: list[list[int]]) -> bool:
    if len(founded_shoes) % 2 != 0:
        return False

    unpaired_shoes = {}
    for shoe in founded_shoes:
        # left shoes negative size, right shoes positive size
        size = shoe[1] if shoe[0] == 1 else shoe[1] * -1
        search_pair = size * -1
        if search_pair in unpaired_shoes:
            unpaired_shoes[search_pair] -= 1
            if unpaired_shoes[search_pair] < 1:
                del unpaired_shoes[search_pair]
        else:
            unpaired_shoes[size] = unpaired_shoes.get(size, 0) + 1
    return len(unpaired_shoes) == 0


def main():
    shoes = [[0, 21], [1, 23], [1, 21], [0, 23]]
    # expected = True
    print(solution(shoes))


if __name__ == "__main__":
    main()
