#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(param1, param2):
    digits1 = [int(num) for num in str(max(param1, param2))]
    digits2 = [int(num) for num in str(min(param1, param2)).zfill(len(digits1))]
    output = ""
    for i in range(len(digits1)):
        output += str(digits1[i] + digits2[i])[-1]
    return int(output)



def main():
    param1 = 456
    param2 = 1734
    print(solution(param1, param2))

if __name__ == "__main__":
    main()

