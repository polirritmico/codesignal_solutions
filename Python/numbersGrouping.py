#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(numbers: list[int]) -> int:
    headers = []
    for number in numbers:
        header_level = (number - 1) // (10**4)
        headers.append(header_level)
    return len(numbers) + len(set(headers))


def main():
    case = [239, 10000, 10001, 20000, 20566, 29999, 999999]
    # expected = 11
    print(solution(case))


if __name__ == "__main__":
    main()
