#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
John has always liked analog clocks more than digital ones. He's been dreaming
about turning his digital clock into an analog one for as long as he can
remember, and now he met you, a great programmer, so his dream is about to come
true.

The screen of his digital clock is a simple 17 × 17 rectangle of pixels. It
always shows four digits: the first two stand for hours and second two for
minutes (John's clock uses the 24-hour format). Each digit is located in a 17 ×
4 rectangle, with the leftmost column always empty, and the other three columns
filled according to this pattern with the proper scaling:

https://codesignal.s3.amazonaws.com/uploads/1664318507/digits.png?raw=true

After the first two digits there is a separating column containing one symbol
':' at its center.

Now John asks you to make his clock show time in the format similar to analog
clocks. Here's how: an analog clock can be represented as a circle (the clock's
borders) and two segments (the clock's hands). To show it on the 17 × 17 screen,
you should light the pixels on it so that the pixel with coordinates (x, y) is
enabled if and only if the minimal distance to the circle or one of the segments
is less than sqrt(0.5).

John wants you to implement the function that changes the digital representation
to the analog one as described above. Given a 17 × 17 rectangle dtime
representing digital time representation, return the analog representation of
the same time.

Please note that for the early prototype you have to develop, both of the
clock's hands should have the same length.

Example

For


dtime = [
  ['.', '*', '*', '*', '.', '.', '*', '.', '.', '.', '*', '*', '*', '.', '*', '*', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', ':', '.', '*', '*', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '.', '*', '.', '.', '*', '.', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
  ['.', '*', '*', '*', '.', '.', '*', '.', '.', '.', '*', '*', '*', '.', '*', '*', '*']
]

the output should be


solution(dtime) = [
  ['.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.'],
  ['.', '.', '.', '*', '*', '.', '.', '.', '.', '.', '.', '.', '*', '*', '.', '.', '.'],
  ['.', '.', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '.', '.'],
  ['.', '*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '*', '*', '.'],
  ['*', '*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '*', '*'],
  ['*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '*'],
  ['*', '.', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '*'],
  ['*', '.', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '*'],
  ['*', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
  ['*', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
  ['*', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
  ['*', '.', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '.', '*'],
  ['*', '*', '.', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '.', '*', '*'],
  ['.', '*', '*', '.', '.', '.', '.', '.', '*', '.', '.', '.', '.', '.', '*', '*', '.'],
  ['.', '.', '*', '*', '.', '.', '.', '.', '*', '.', '.', '.', '.', '*', '*', '.', '.'],
  ['.', '.', '.', '*', '*', '.', '.', '.', '*', '.', '.', '.', '*', '*', '.', '.', '.'],
  ['.', '.', '.', '.', '*', '*', '*', '*', '*', '*', '*', '*', '*', '.', '.', '.', '.']
]

(Enabled pixels are painted red to make them more visible).

Here is the geometrical representation of an analog clock showing time 01:30.
Enabled pixel are painted red.

https://codesignal.s3.amazonaws.com/uploads/1667239937815/example.png?raw=true

Input/Output

[input] array.array.char dtime

Digital time representation, where dtime[x][y] is equal to '*' if the pixel with
coordinates (x, y) is enabled and '.' otherwise. It is guaranteed that the given
time is correct, and that dtime[8][8] = ':'.

Guaranteed constraints:
dtime.length = 17,
dtime[i].length = 17.

[output] array.array.char

Representation of the same time on the same rectangle, but in an analog clock
format.


"""

import math


def overwrite_clock_frame(clock: list[list[str]]) -> None:
    # fmt: off
    frame = [
        [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
        [".", ".", ".", "*", "*", " ", " ", " ", " ", " ", " ", " ", "*", "*", ".", ".", "."],
        [".", ".", "*", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", "*", ".", "."],
        [".", "*", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", "*", "."],
        ["*", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*"],
        ["*", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", "*"],
        [".", "*", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", "*", "."],
        [".", ".", "*", "*", " ", " ", " ", " ", " ", " ", " ", " ", " ", "*", "*", ".", "."],
        [".", ".", ".", "*", "*", " ", " ", " ", " ", " ", " ", " ", "*", "*", ".", ".", "."],
        [".", ".", ".", ".", "*", "*", "*", "*", "*", "*", "*", "*", "*", ".", ".", ".", "."],
    ]
    for row in range(17):
        for col in range(17):
            if frame[row][col] != " ":
                clock[row][col] = frame[row][col]


def convert_7_segment_to_int(grid: list[list[str]]) -> int:
    """
    Segments:
      a
    f   b
      g
    e   c
      d
    """
    seven_segment_numbers_map = {
        # abcdefg
        0b1111110: 0,
        0b1001001: 1,
        0b1101101: 2,
        0b1111001: 3,
        0b0110011: 4,
        0b1011011: 5,
        0b1011111: 6,
        0b1110000: 7,
        0b1111111: 8,
        0b1111011: 9,
    }
    current = [
        grid[0][1] == "*",  # segment a
        grid[4][2] == "*",  # segment b
        grid[12][2] == "*",  # segment c
        grid[16][1] == "*",  # segment d
        grid[12][0] == "*",  # segment e
        grid[4][0] == "*",  # segment f
        grid[8][1] == "*",  # segment g
    ]
    key = int("".join("1" if segment else "0" for segment in current), 2)
    return seven_segment_numbers_map[key]


def hour_and_minutes_from_7_segment_grid(grid) -> tuple[int, int]:
    hour_left = convert_7_segment_to_int([row[1:4] for row in grid])
    hour_right = convert_7_segment_to_int([row[5:8] for row in grid])
    minute_left = convert_7_segment_to_int([row[10:13] for row in grid])
    minute_right = convert_7_segment_to_int([row[14:17] for row in grid])
    hour = hour_left * 10 + hour_right
    minute = minute_left * 10 + minute_right
    return (hour, minute)


def line_coords(angle):
    coords = []
    threshold = math.sqrt(0.5)
    sin = math.sin(angle * math.pi * 2)
    cos = -math.cos(angle * math.pi * 2)
    for i in range(0, 81, 2):
        i /= 10
        yd = 8 + cos * i
        xd = 8 + sin * i
        for y in range(int(yd) - 1, int(yd) + 2):
            if y < 0 or y > 17:
                continue
            for x in range(int(xd) - 1, int(xd) + 2):
                if x < 0 or x > 17:
                    continue
                dist = abs(math.sqrt((yd - y) * (yd - y) + (xd - x) * (xd - x)))
                if dist < threshold:
                    coords.append((y, x))
    return coords


def draw_handles(clock, hours, minutes):
    char = "*"
    for coord in hours:
        clock[coord[0]][coord[1]] = char
    for coord in minutes:
        clock[coord[0]][coord[1]] = char
    return clock


def solution(grid: list[list[str]]) -> list[list[str]]:
    time: tuple[int, int] = hour_and_minutes_from_7_segment_grid(grid)
    hours_angle = (time[0] * 60 + time[1]) / 720
    minutes_angle = time[1] / 60
    clock = [["." for _ in range(17)] for _ in range(17)]
    hours_hand = line_coords(hours_angle)
    minutes_hand = line_coords(minutes_angle)
    clock = draw_handles(clock, hours_hand, minutes_hand)
    overwrite_clock_frame(clock)
    return clock


def main():
    # fmt: off
    case = [
        ['.', '.', '*', '.', '.', '*', '*', '*', '.', '.', '*', '*', '*', '.', '*', '*', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '*', '*', ':', '.', '*', '*', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '.', '*', '.', '.', '.', '.', '*', '.', '*', '.', '*'],
        ['.', '.', '*', '.', '.', '*', '*', '*', '.', '.', '*', '*', '*', '.', '*', '*', '*'],
    ]
    print()
    print(*solution(case), sep="\n")


if __name__ == "__main__":
    main()
