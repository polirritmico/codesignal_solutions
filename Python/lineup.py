#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(commands):
    same_direction = True
    counter = 0
    for command in commands:
        if command == 'L' or command == 'R':
            same_direction = not same_direction
        if same_direction:
            counter += 1
    return counter



def main():
    case = "LLARL"
    #expected = 3
    print(solution(case))

if __name__ == "__main__":
    main()

