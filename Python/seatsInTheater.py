#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(nCols, nRows, col, row):
    return (nCols - col + 1) * (nRows - row)


def main():
    nCols = 16
    nRows = 11
    col = 5
    row = 3
    print(solution(nCols, nRows, col, row))

if __name__ == "__main__":
    main()

