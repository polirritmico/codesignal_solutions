#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(input: str) -> str:
    return input.split("@")[-1]


def main():
    case = "prettyandsimple@example.com"
    print(solution(case))


if __name__ == "__main__":
    main()
