#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
N candles are placed in a row, some of them are initially lit. For each candle
from the 1st to the Nth the following algorithm is applied: if the observed
candle is lit then states of this candle and all candles before it are changed
to the opposite. Which candles will remain lit after applying the algorithm to
all candles in the order they are placed in the line?

Example

    For a = [1, 1, 1, 1, 1], the output should be
    solution(a) = [0, 1, 0, 1, 0].

    Check out the image below for better understanding:
    https://codesignal.s3.amazonaws.com/uploads/1664318500/example.png?raw=true

    For a = [0, 0], the output should be
    solution(a) = [0, 0].

    The candles are not initially lit, so their states are not altered by the algorithm.

"""


def solution(candles: list[int]) -> list[int]:
    flips = 0
    for current_position in range(len(candles) - 1, -1, -1):
        if candles[current_position] == 1:
            flips += 1
        candles[current_position] = (candles[current_position] + flips) % 2
    return candles


def main():
    case = [1, 1, 1, 1, 1]
    # expected = [0, 1, 0, 1, 0]
    print(solution(case))


if __name__ == "__main__":
    main()
