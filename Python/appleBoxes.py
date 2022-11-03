#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(boxes):
    red_apples = 0
    yellow_apples = 0
    for i in range(1, boxes + 1):
        if i % 2:
            yellow_apples += i * i
        else:
            red_apples += i * i
    return red_apples - yellow_apples



def main():
    case = 5
    #expected = -15
    print(solution(case))

if __name__ == "__main__":
    main()

