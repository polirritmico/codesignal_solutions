#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(inputString) -> str:
    length = len(inputString)
    open_bracket_pos = 0
    close_bracket_pos = 0
    bracket_level = 0
    need_reverse = False
    for i in range(length):
        current_char = inputString[i]
        if not need_reverse and current_char == '(':
            need_reverse = True
            open_bracket_pos = i
            bracket_level += 1
        elif current_char == '(':
            bracket_level += 1
        elif current_char == ')':
            close_bracket_pos = i
            bracket_level -= 1
            if bracket_level == 0:
                break
    if not need_reverse:
        return inputString

    reverse_section = inputString[open_bracket_pos+1:close_bracket_pos]
    reverse_section = solution(reverse_section)
    reverse_section = reverse_section[::-1]

    before = ""
    after = ""
    if open_bracket_pos > 0:
        before = inputString[0:open_bracket_pos]
    if close_bracket_pos+1 != length:
        after = inputString[close_bracket_pos+1:]
    if after != "":
        after = solution(after)

    return before + reverse_section + after


def main():
    #inputString = "bar"
    #inputString = "(bar)"
    #inputString = "(bar)baz"
    #inputString = "foo(bar)"
    #inputString = "foo(bar)baz"
    #inputString = "((buz)a)baz"
    #inputString = "foo(bar(buz))baz"
    inputString = "foo(bar(buz)test)baz"
    print(solution(inputString))

if __name__ == "__main__":
    main()

