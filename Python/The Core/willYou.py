#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(young, beautiful, loved) -> bool:
    contradicts = True
    not_contradicts = False
    if young and beautiful and not loved:
        return contradicts
    if loved and (not young or not beautiful):
        return contradicts
    return not_contradicts


def main():
    young = True
    beautiful = True
    loved = True
    print(solution(young, beautiful, loved))

if __name__ == "__main__":
    main()

