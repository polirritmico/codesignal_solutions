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


class AnalogClock:
    def __init__(self, threshold: float) -> None:
        self.drawing_char = "*"
        self.empty_char = "."
        self.size = 16
        self.threshold = threshold
        self.clock: list[list[str]] = [
            [self.empty_char for _ in range(17)] for _ in range(17)
        ]
        self.time24: tuple[int, int] = (0, 0)

    def convert_7_segment_to_int(self, led_grid: list[list[str]]) -> int:
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
            led_grid[0][1] == self.drawing_char,  # segment a
            led_grid[4][2] == self.drawing_char,  # segment b
            led_grid[12][2] == self.drawing_char,  # segment c
            led_grid[16][1] == self.drawing_char,  # segment d
            led_grid[12][0] == self.drawing_char,  # segment e
            led_grid[4][0] == self.drawing_char,  # segment f
            led_grid[8][1] == self.drawing_char,  # segment g
        ]
        key = int("".join("1" if segment else "0" for segment in current), 2)
        return seven_segment_numbers_map[key]

    def digital_7_segments_grid_importer(self, grid: list[list[str]]) -> None:
        hour_left = self.convert_7_segment_to_int([row[1:4] for row in grid])
        hour_right = self.convert_7_segment_to_int([row[5:8] for row in grid])
        minute_left = self.convert_7_segment_to_int([row[10:13] for row in grid])
        minute_right = self.convert_7_segment_to_int([row[14:17] for row in grid])
        hour = hour_left * 10 + hour_right
        minute = minute_left * 10 + minute_right
        self.time24 = (hour, minute)

    def draw(self, *shapes_to_draw: list[int, int]) -> None:
        for element in shapes_to_draw:
            for coord in element:
                self.clock[coord[0]][coord[1]] = self.drawing_char

    def time_angles(self, time: tuple[int, int] = None) -> tuple[float, float]:
        time = self.time24 if time is None else time
        hours_angle = (time[0] * 60 + time[1]) / 720
        minutes_angle = time[1] / 60
        return (hours_angle, minutes_angle)

    def generate_handle_coords(self, angle: float) -> list[tuple[int, int]]:
        coords = []
        size = 8
        sin = math.sin(angle * math.pi * 2)
        cos = math.cos(angle * math.pi * 2) * -1
        for step in range(0, size * 10 + 1, 2):
            step /= 10
            dist_row = size + cos * step
            dist_col = size + sin * step
            for row in range(int(dist_row) - 1, int(dist_row) + 2):
                if row < 0 or row >= size * 2:
                    continue
                for col in range(int(dist_col) - 1, int(dist_col) + 2):
                    if col < 0 or col >= size * 2:
                        continue
                    dist = math.sqrt((dist_row - row) ** 2 + (dist_col - col) ** 2)
                    if abs(dist) < self.threshold:
                        coords.append((row, col))
        return coords

    def generate_clock_frame(self) -> list[list[str]]:
        size = 8
        radius = size + 0.5
        coords: list[tuple[int, int]] = []
        for row in range(size * 2 + 1):
            for col in range(size * 2 + 1):
                distance = radius - math.sqrt((row - size) ** 2 + (col - size) ** 2)
                if distance < self.threshold and distance > self.threshold * -1:
                    coords.append((row, col))
        return coords

    def ascii_draw(self) -> list[list[str]]:
        handles_angles = self.time_angles()
        hours_handle = self.generate_handle_coords(handles_angles[0])
        minutes_handle = self.generate_handle_coords(handles_angles[1])
        clock_frame = self.generate_clock_frame()
        self.draw(hours_handle, minutes_handle, clock_frame)
        return self.clock


def solution(grid: list[list[str]]) -> list[list[str]]:
    threshold = math.sqrt(0.5)
    clock = AnalogClock(threshold)
    clock.digital_7_segments_grid_importer(grid)
    analog_ascii_clock = clock.ascii_draw()
    return analog_ascii_clock


def main():
    # fmt: off
    case = [  # 16:53
        [".", ".", "*", ".", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
        [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", "*", "*", ":", ".", "*", "*", "*", ".", "*", "*", "*"],
        [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", ".", "*", ".", ".", ".", ".", "*", ".", ".", ".", "*"],
        [".", ".", "*", ".", ".", "*", "*", "*", ".", ".", "*", "*", "*", ".", "*", "*", "*"],
    ]
    print()
    print(*["".join(line) for line in solution(case)], sep="\n")


if __name__ == "__main__":
    main()
