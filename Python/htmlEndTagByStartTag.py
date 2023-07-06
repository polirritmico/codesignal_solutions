#!/usr/bin/env python
# -*- coding: utf-8 -*-


def solution(start_tag: str) -> str:
    tag = start_tag.split(" ")[0]
    if not tag.endswith(">"):
        tag += ">"
    return tag[:1] + "/" + tag[1:]


def main():
    case = "<button type='button' disabled>"
    print(solution(case))


if __name__ == "__main__":
    main()
