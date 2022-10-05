#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(time_string):
    time_list = time_string.split(':')
    if len(time_list) != 2:
        return False
    hour = int(time_list[0])
    minutes = int(time_list[1])
    if hour > 23 or minutes > 59:
        return False
    return True
    

def main():
    case = "01:59"
    print(solution(case))

if __name__ == "__main__":
    main()

