#!/usr/bin/env python
# -*- coding: utf-8 -*-

# You are given an array of integers that you want distribute between several
# groups. The first group should contain numbers from 1 to 10^4, the second
# should contain those from 10^4 + 1 to 2 * 10^4, ..., the 100th one should
# contain numbers from 99 * 10^4 + 1 to 10^6 and so on.
#
# All the numbers will then be written down in groups to the text file in such
# a way that:
#
#     the groups go one after another;
#     each non-empty group has a header which occupies one line;
#     each number in a group occupies one line.
#
# Calculate how many lines the resulting text file will have.
#
# Example
#
# For a = [20000, 239, 10001, 999999, 10000, 20566, 29999], the output should
# be solution(a) = 11.
#
# The numbers can be divided into 4 groups:
#
#     239 and 10000 go to the 1st group (1 ... 10^4);
#     10001 and 20000 go to the second 2nd (10^4 + 1 ... 2 * 10^4);
#     20566 and 29999 go to the 3rd group (2 * 10^4 + 1 ... 3 * 10^4);
#     groups from 4 to 99 are empty;
#     999999 goes to the 100th group (99 * 10^4 + 1 ... 10^6).
#
# Thus, there will be 4 groups (i.e. four headers) and 7 numbers, so the file
# will occupy 4 + 7 = 11 lines.


def solution(numbers: list[int]) -> int:
    numbers.sort()
    numbers_count = len(numbers)
    headers = []
    for number in numbers:
        for header_level in range(100):
            low_limit = (header_level * (10**4)) + 1
            high_limit = (header_level + 1) * (10**4)
            if number >= low_limit and number <= high_limit:
                headers.append(number + 1)
                break
    return numbers_count + len(set(headers))


def main():
    case = [20000, 239, 10001, 999999, 10000, 20566, 29999]
    # expected = 11
    print(solution(case))


if __name__ == "__main__":
    main()
