#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some people are standing in a row in a park. There are trees between them which
cannot be moved. Your task is to rearrange the people by their heights in a
non-descending order without moving the trees. People can be very tall!

Example

For a = [-1, 150, 190, 170, -1, -1, 160, 180], the output should be
solution(a) = [-1, 150, 160, 170, -1, -1, 180, 190].

"""


def solution(queue: list[int]):
    tree = -1
    people = iter(sorted([int(people) for people in queue if people != tree]))
    for position in range(len(queue)):
        if queue[position] != tree:
            queue[position] = next(people)
    return queue


def main():
    case = [-1, 150, 190, 170, -1, -1, 160, 180]
    # expected = [-1, 150, 160, 170, -1, -1, 180, 190]
    print(solution(case))


if __name__ == "__main__":
    main()
