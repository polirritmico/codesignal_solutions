#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_cost = 0

    map = []
    for x in range(0, cols):
        for y in range(0, rows):
            cost = matrix[y][x]
            if cost == 0:
                break
            total_cost += cost
    return total_cost

def main():
    matrix = [[0, 1, 1, 2],
              [0, 5, 0, 0],
              [2, 0, 3, 3]]
    print(solution(matrix))

if __name__ == "__main__":
    main()
