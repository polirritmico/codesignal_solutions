#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(value1, weight1, value2, weight2, maxW):
    both_weights = value1 + value2 if (weight1 + weight2 <= maxW) else 0
    value1 = value1 if weight1 <= maxW else 0
    value2 = value2 if weight2 <= maxW else 0

    return max(both_weights, value1, value2)


def main():
    value1 = 10
    weight1 = 5
    value2 = 6
    weight2 = 4
    maxW = 8
    print(solution(value1, weight1, value2, weight2, maxW))

if __name__ == "__main__":
    main()

