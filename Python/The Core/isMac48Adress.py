#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(input: str) -> bool:
    if len(input) != 17:
        return False
    if len(input.split("-")) != 6:
        return False
    for char in input.replace("-", ""):
        if char not in "0123456789ABCDEF":
            return False
    return True


def main():
    case = "00-1B-63-84-45-E6"
    print(solution(case))


if __name__ == "__main__":
    main()
