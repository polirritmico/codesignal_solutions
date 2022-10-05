#!/usr/bin/env python
# -*- coding: utf-8 -*-

def print_info(step, current_number, prev, re_prev, red_flags):
    print("Step: {}\n".format(step) +
          "Current number:  {}\n".format(current_number) +
          "Previous number: {}\n".format(prev) +
          "Reprev number:   {}\n".format(re_prev) +
          "Red_flags:       {}\n".format(red_flags) + "\n"
          )


def solution(sequence):
    print("Sequence: {}".format(sequence))
    length = len(sequence)
    red_flags = 0
    if length < 3:
        return True
    elif length == 3:
        if sequence[0] >= sequence[1]:
            red_flags += 1
        if sequence[0] >= sequence[2]:
            red_flags += 1
        if sequence[1] >= sequence [2]:
            red_flags += 1
        if red_flags > 2:
            return False
        return True

    prev = None
    re_prev = None
    current_step = 0
    red_flag_step = 0
    for current_number in sequence:
        current_step += 1
        if prev == None:
            prev = current_number
            continue
        elif re_prev == None:
            re_prev = prev
            prev = current_number
            continue

        if re_prev >= prev:
            red_flags += 1
            red_flag_step = current_step
        if re_prev >= current_number:
            red_flags += 1
            red_flag_step = current_step
        if current_step == length and prev >= current_number:
            red_flags += 1
            if current_step - red_flag_step > 2:
                return False

        print_info(current_step, current_number, prev, re_prev, red_flags)

        if red_flags > 2:
            return False

        re_prev = prev
        prev = current_number
    return True


def main():
    solution([1, 99, 2, 3])

if __name__ == "__main__":
    main()
