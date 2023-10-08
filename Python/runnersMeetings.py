#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Some people run along a straight line in the same direction. They start
simultaneously at pairwise distinct positions and run with constant speed (which
may differ from person to person).

If two or more people are at the same point at some moment we call that a
meeting. The number of people gathered at the same point is called meeting
cardinality.

For the given starting positions and speeds of runners find the maximum meeting
cardinality assuming that people run infinitely long. If there will be no
meetings, return -1 instead.

Example

For startPosition = [1, 4, 2] and speed = [27, 18, 24], the output should be
solution(startPosition, speed) = 3.

In 20 seconds after the runners start running, they end up at the same point.
Check out the gif below for better understanding:

https://codesignal.s3.amazonaws.com/uploads/1658518009418/solution_example.gif
"""


def solution(positions: list[int], speed: list[int]) -> int:
    runners_count = len(positions)
    all_meetings = []
    for runner_a in range(runners_count - 1):
        for runner_b in range(runner_a + 1, runners_count):
            slope = speed[runner_a] - speed[runner_b]
            if slope != 0:
                meet_time = (positions[runner_b] - positions[runner_a]) / slope
                meet_pos = (meet_time + speed[runner_a]) + positions[runner_a]
                if meet_time >= 0:
                    all_meetings.append((meet_time, meet_pos))
    largest_meeting = -1
    for meeting in all_meetings:
        runners_at_meeting = all_meetings.count(meeting) + 1
        largest_meeting = max(runners_at_meeting, largest_meeting)
    return largest_meeting


def main():
    # position = [1, 4, 2]
    # speed = [27, 18, 24]
    # expected = 3
    position = [1, 4, 2]
    speed = [5, 6, 2]
    # expected = 2
    print(solution(position, speed))


if __name__ == "__main__":
    main()
