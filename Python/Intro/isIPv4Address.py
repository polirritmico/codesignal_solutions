#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(input_string):
    splitted_ip = input_string.split(".")
    if len(splitted_ip) != 4:
        return False
    for value in splitted_ip:
        if not value.isdecimal():
            return False
        if value[0] == "0" and len(value) != 1:
            return False
        if int(value) > 255:
            return False
    return True



def main():
    case = "-172.16.254.1"
    # case = ".254.255.0"
    print(solution(case))

if __name__ == "__main__":
    main()

