#!/usr/bin/env python
# -*- coding: utf-8 -*-

def adjProduct(inputArray) -> int:
    max_value = sys.minint
    for i in range(0, len(inputArray) - 1):
        result = inputArray[i] * inputArray[i + 1]
        if result > max_value:
            max_value = result
        print(result)

    return max_value

def main():
    adjProduct([-23, 4, -3, 8, -12])

if __name__ == "__main__":
    main()
