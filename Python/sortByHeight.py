#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(row) -> list:
    people = []
    output = []
    tree = -1
    for element in row:
        if element != tree:
            people.append(element)
    people.sort()

    for element in row:
        if element != tree:
            output.append(people.pop(0))
            continue
        output.append(element)
    return output


def main():
    a = [-1, 150, 190, 170, -1, -1, 160, 180]
    print(solution(a))

if __name__ == "__main__":
    main()

