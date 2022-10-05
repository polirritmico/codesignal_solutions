#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(names):
    renamed_files = []
    for name in names:
        original_name = name
        count = 0
        while name in renamed_files:
            count += 1
            name = original_name + "(" + str(count) + ")"
        renamed_files.append(name)
    return renamed_files


def main():
    case = ["doc", "doc", "image", "doc(1)", "doc"]
    #expected "doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"
    case = ["a(1)", "a(3)", "a", "a", "a", "a" ]    
    # expec: a(1), a(3), "a", "a(2)", "a(4)", "a(5)"
    print(solution(case))

if __name__ == "__main__":
    main()

