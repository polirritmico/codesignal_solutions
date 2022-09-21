#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(obstacle_list):
    last_obstacle = max(obstacle_list)
    jump_size = 2
    current_position = 0
    while current_position < last_obstacle:
        current_position += jump_size
        if current_position in obstacle_list:
            jump_size += 1
            current_position = 0
    return jump_size


def main():
    case = [3, 5, 6, 7, 9]
    print(solution(case))

if __name__ == "__main__":
    main()

