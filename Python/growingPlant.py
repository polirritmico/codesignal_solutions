#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(up_speed, down_speed, desired_height):
    current_height = 0
    days = 0
    while current_height < desired_height:
        days += 1
        current_height += up_speed
        if current_height >= desired_height:
            return days
        current_height -= down_speed

def main():
    upSpeed = 10
    downSpeed = 9
    desiredHeight = 4
    expected = 10
    print(solution(upSpeed, downSpeed, desiredHeight))

if __name__ == "__main__":
    main()

