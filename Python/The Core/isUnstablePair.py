#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(filename_1: str, filename_2: str) -> bool:
    file1_before = filename_1 < filename_2
    file1_before_lower_case = filename_1.lower() < filename_2.lower()
    is_unstable = file1_before != file1_before_lower_case
    return is_unstable


def main():
    # filename_1 = "aa"
    # filename_2 = "AAB"
    # Expected True
    filename_1 = "za"
    filename_2 = "Z"
    # Expected False
    print(solution(filename_1, filename_2))


if __name__ == "__main__":
    main()
