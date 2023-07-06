#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(input: str) -> bool:
    return input.lower() == input.lower()[::-1]


def main():
    case = "AaBaa"
    print(solution(case))


if __name__ == "__main__":
    main()
