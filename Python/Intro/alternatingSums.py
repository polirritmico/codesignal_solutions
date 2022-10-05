#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(row):
    team1 = 0
    team2 = 0
    for i in range(len(row)):
        if i % 2 == 0:
            team1 += row[i]
        else:
            team2 += row[i]
    return [team1, team2]


def main():
    case = [50, 60, 60, 45, 70]
    solution(case)


if __name__ == "__main__":
    main()
