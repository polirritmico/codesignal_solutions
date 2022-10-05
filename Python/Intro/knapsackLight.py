#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(value1, weight1, value2, weight2, maxW):
    both_weights = value1 + value2 if (weight1 + weight2 <= maxW) else 0
    value1 = value1 if weight1 <= maxW else 0
    value2 = value2 if weight2 <= maxW else 0

    return max(both_weights, value1, value2)

    ## if False = 0; if True = 1
    #both_weights = (value1 + value2) * (weight1 + weight2 <= maxW)
    #weight1 = value1 * (weight1 <= maxW)
    #weight2 = value2 * (weight2 <= maxW)
    
    #return max(both_weights, weight1, weight2)

    #if weight1 + weight2 <= maxW:
    #    return value1 + value2
    #if weight1 <= maxW and weight2 > maxW:
    #    return value1
    #if weight2 <= maxW:
    #    return max(value1, value2)
    #return 0


def main():
    value1 = 10
    weight1 = 5
    value2 = 6
    weight2 = 4
    maxW = 8
    print(solution(value1, weight1, value2, weight2, maxW))

if __name__ == "__main__":
    main()

