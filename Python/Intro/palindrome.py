#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(inputString):
    large = len(inputString)
    steps = large // 2
    if large == 1:
        return True
    if large % 2 != 0:
        steps += 1

    begin = 0
    end = large - 1

    for i in range(0, steps):
        if inputString[begin] != inputString[end]:
            return False
        begin += 1
        end -= 1
    return True



def main():
    #solution("zzzazzazz")
    solution("aba")


if __name__ == "__main__":
    main()
