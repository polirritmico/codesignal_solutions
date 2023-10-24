#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You have been watching a video for some time. Knowing the total video duration
find out what portion of the video you have already watched.

Example

For part = "02:20:00" and total = "07:00:00", the output should be
solution(part, total) = [1, 3].

You have watched 1 / 3 of the whole video.

Input/Output

string part
A string of the following format "hh:mm:ss" representing the time you have been
watching the video.

array.integer
An array of the following format [a, b] (where a / b is a reduced fraction).


"""

from fractions import Fraction


def time_string_to_seconds(time: str) -> int:
    hours, minutes, seconds = time.split(":")
    return int(seconds) + int(minutes) * 60 + int(hours) * 3600


def solution(part: str, total: str) -> list[int]:
    part_seconds = time_string_to_seconds(part)
    total_seconds = time_string_to_seconds(total)
    fraction = Fraction(part_seconds, total_seconds)
    return [fraction.numerator, fraction.denominator]


def main():
    part = "02:20:00"
    total = "07:00:00"
    # expected = [1, 3]
    print(solution(part, total))


if __name__ == "__main__":
    main()
