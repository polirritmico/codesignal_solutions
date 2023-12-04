#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(input: str) -> bool:
    input_len = len(input)
    if input_len % 2 != 0:
        return False
    middle = input_len // 2
    for left in range(middle):
        right = left + middle
        if input[left] != input[right]:
            return False
    return True


def main():
    case = "tandemtandem"
    print(solution(case))


if __name__ == "__main__":
    main()
