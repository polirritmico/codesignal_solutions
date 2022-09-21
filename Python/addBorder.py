#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(picture) -> list:
    out_width = len(picture[0]) + 2
    border = ""
    output = []
    for i in range(out_width):
        border += "*"
    output.append(border)
    for row in picture:
        row = "*" + row +"*"
        output.append(row)
    output.append(border)
    return output


def main():
    case = ["abc", "ded"]
    print(solution(case))

if __name__ == "__main__":
    main()

