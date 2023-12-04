#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Implement the missing code, denoted by ellipses. You may not modify the
pre-existing code.

An eye rhyme is a rhyme in which two words are spelled similarly but pronounced
differently. An example is the pair cough and bough; although they look similar,
when they are spoken there is no rhyming quality.

You are writing a thesis on the eye rhyme, and you thought it would be cool to
make the text itself eye rhymed. This brilliant idea came to your mind a little
too late: the text is already written. Now you want to check if a given pair of
lines in your text have an eye rhyme. More specifically, you want to make sure
that the last three characters of each pair of lines coincide.

You have already split your text into pairs of lines. Now all that's left is to
check that the last three characters of the lines in each pairOfLines coincide.
Implement a function that will do this job.


Example

    For pairOfLines = "cough\tbough", the output should be
    solution(pairOfLines) = true.

    Both lines end with ugh.

    For pairOfLines = "CodeFig!ht\tWith all your might", the output should be
    solution(pairOfLines) = false.

    The first line ends with !ht, and the second one ends with ght.


Input/Output

string pairOfLines

A string in the format "<line1>\t<line2>", where <linei> consists of at least 3
characters and may contain any character except '\t' (tabulation character). The
lines are separated by '\t' (tabulation character).

"""
import re


def solution(pairOfLines):
    pattern = r".*(.{3})\t.*(.{3})"
    match = re.match(pattern, pairOfLines)
    return match.group(1) == match.group(2)


def main():
    case = "CodeFig!ht\tWith all your might"
    # expected = False
    print(solution(case))


if __name__ == "__main__":
    main()
