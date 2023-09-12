#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
There are some people and cats in a house. You are given the number of legs they
have all together. Your task is to return an array containing every possible
number of people that could be in the house sorted in ascending order. It's
guaranteed that each person has 2 legs and each cat has 4 legs.

Example

    For legs = 6, the output should be
    solution(legs) = [1, 3].

    There could be either 1 cat and 1 person (4 + 2 = 6) or 3 people (2 * 3 = 6).

    For legs = 2, the output should be
    solution(legs) = [1].

    There can be only 1 person.
"""


def solution(legs):
    people_legs = 2
    cat_legs = 4
    max_cats = legs // cat_legs
    supposed_people = [legs // people_legs]
    for supposed_cats in range(1, max_cats + 1):
        remaining_legs = legs - (supposed_cats * cat_legs)
        supposed_people.append(remaining_legs // people_legs)
    return sorted(supposed_people)


def main():
    case = 6
    # expected = [1, 3]
    print(solution(case))


if __name__ == "__main__":
    main()
