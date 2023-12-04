#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement the missing code, denoted by ellipses. You may not modify the
pre-existing code.

A sentence is considered correct if:

    - it starts with a capital letter;
    - it ends with a full stop, question mark or exclamation point ('.', '?' or
      '!');
    - full stops, question marks and exclamation points don't appear anywhere
      else in the sentence.

Given a sentence, return true if it is correct and false otherwise.

Example

    For sentence = "This is an example of *correct* sentence.",
    the output should be
    solution(sentence) = true;

    For sentence = "!this sentence is TOTALLY incorrecT",
    the output should be
    solution(sentence) = false.


"""
import re


def solution(sentence):
    pattern = r"^[A-Z][^.?!]*[.?!]$"
    return re.match(pattern, sentence) is not None


def main():
    case = "This is an example of *correct* sentence."
    # expected = True
    print(solution(case))


if __name__ == "__main__":
    main()
