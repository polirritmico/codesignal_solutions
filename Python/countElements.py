#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You've been invited to a job interview at a famous company that tests
programming challenges. To evaluate your coding skills, they have asked you to
parse a given problem's input given as an inputString string, and count the
number of primitive type elements within it.

The inputString can be either a primitive type variable or an array (possibly
multidimensional) that contains elements of the primitive types. A primitive
type variable can be:

- an integer number;
- a string, which is surrounded by " characters (note that it may contain any
  character except ");
- a boolean, which is either true or false.

Return the total number of primitive type elements inside inputString.

Example

- For inputString = "[[0, 20], [33, 99]]", the output should be
  solution(inputString) = 4;
- For inputString = "[ "one", 2, "three" ]", the output should be
  solution(inputString) = 3;
- For inputString = "true", the output should be
  solution(inputString) = 1;
- For inputString = "[[1, 2, [3]], 4]", the output should be
  solution(inputString) = 4.

"""
import re


def solution(input_string: str) -> int:
    open_str = []
    close_str = []
    string_counter = 0
    for i, char in enumerate(input_string):
        if char == '"' and string_counter == 0:
            open_str.append(i)
            string_counter += 1
        elif char == '"':
            close_str.append(i)
            string_counter -= 1
    if len(open_str) != 0:
        strings = []
        for open_quote, close_quote in zip(open_str, close_str):
            strings.append(input_string[open_quote:close_quote])
        for sub_string in strings:
            input_string = input_string.replace(sub_string, "")
        strings = len(strings)
    else:
        strings = 0

    digits = len(re.findall(r"\d+", input_string))

    booleans = input_string.count("true") + input_string.count("false")

    return strings + booleans + digits


def main():
    # case = "[[0, 20], [33, 99]]"
    # case = '"try this!, [1, 2, 3, 32], false"'
    case = '["oh, no! kind, of, tricky", "test, case"]'
    print(solution(case))


if __name__ == "__main__":
    main()
