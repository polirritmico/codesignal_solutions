#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(childrens, candies):
    eaten_pieces = candies // childrens
    return eaten_pieces * childrens


def main():
    n = 3
    m = 10
    print(solution(n, m))

if __name__ == "__main__":
    main()

