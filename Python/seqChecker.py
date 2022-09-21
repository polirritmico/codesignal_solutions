#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(sequence):
    before_previous = (-10 ** 5) - 1
    previous = (-10 ** 5) - 1
    decreased_flag = False
    for current_number in sequence:
        if current_number <= previous:
            if decreased_flag:
                return False
            decreased_flag = True
            if before_previous < current_number:
                previous = current_number
        else:
            before_previous = previous
            previous = current_number
    return True

