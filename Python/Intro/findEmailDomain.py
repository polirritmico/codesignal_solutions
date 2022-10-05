#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re

def solution(address):
    splitted = re.split("@", address)
    return splitted[-1]


def main():
    case = "John.Smith@example.com"
    print(solution(case))

if __name__ == "__main__":
    main()

