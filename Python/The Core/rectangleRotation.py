#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

def solution(a, b):
    point_a = int(math.sqrt(a * a / 2))
    point_b = int(math.sqrt(b * b / 2))
    result = (point_a * point_b) + ((point_a + point_b) // 2)
    result = (result * 2) + 1
    return result

def main():
    a = 6
    b = 4
    # expected = 26
    print(solution(a, b))

if __name__ == "__main__":
    main()

