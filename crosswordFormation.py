#!/usr/bin/env python
# -*- coding: utf-8 -*-

from itertools import permutations


def valid_crosswords_counter(words: tuple[str, str, str, str]) -> int:
    """Explore all positions of given words and count the valid ones.

    Starting position (overlapping):
      LT O  RP
      E     I
      F     G
      TB O  T  T  O  M
            H

    Movement order (inside out):
    1. Right. Vertical. Mov btm-top
    2. Right. Horizontal. Mov left-right
    3. Lower. Vertical. Mov top-btm
    4. Lower. Horizontal. Mov right-left
    5. Left. Vertical. Mov btm-top
    6. Upper. Horizontal. Mov right-left

    Args:
        words (tuple[str, str, str, str]): A tuple containing the 4 words to check.

    Returns:
        int: The count of valid crossword positions for the given words.

    """

    top, right, btm, left = words
    top_len, right_len, btm_len, left_len = [len(word) for word in words]
    valid_count = 0

    offset = 2
    limit_top_hor = top_len - offset
    limit_left_ver = left_len - offset
    limit_btm_hor = btm_len - offset

    for idx_top_left in range(limit_top_hor):
        char_top_left = top[idx_top_left]
        for idx_left_top in range(limit_left_ver):
            char_left_top = left[idx_left_top]
            if char_top_left != char_left_top:
                continue
            limit_btm_ver = min(left_len - idx_left_top, right_len)
            for idx_btm_left in range(limit_btm_hor):
                char_btm_left = btm[idx_btm_left]
                for position_btm_ver in range(offset, limit_btm_ver):
                    idx_left_btm = idx_left_top + position_btm_ver
                    char_left_btm = left[idx_left_btm]
                    if char_left_btm != char_btm_left:
                        continue
                    remaining_top_chars = top_len - idx_top_left - offset
                    remaining_btm_chars = btm_len - idx_btm_left - offset
                    limit_right_hor = min(remaining_top_chars, remaining_btm_chars)
                    limit_right_ver = right_len - position_btm_ver
                    for pos_right_hor in range(limit_right_hor):
                        idx_top_right = pos_right_hor + idx_top_left + offset
                        idx_btm_right = pos_right_hor + idx_btm_left + offset
                        char_top_right = top[idx_top_right]
                        char_btm_right = btm[idx_btm_right]
                        for idx_right_top in range(limit_right_ver):
                            idx_right_btm = position_btm_ver + idx_right_top
                            char_right_top = right[idx_right_top]
                            char_right_btm = right[idx_right_btm]
                            if char_top_right != char_right_top:
                                continue
                            if char_btm_right != char_right_btm:
                                continue
                            valid_count += 1
    return valid_count


def solution(words: list[str]) -> int:
    if len(words) != 4:
        raise ValueError("Error: Expected 4 words.")
    if any(len(word) < 3 for word in words):
        raise ValueError("Error: Word with less than 3 characters length.")

    valid_solutions = 0
    for permutation in permutations(words):
        valid_crosswords: int = valid_crosswords_counter(permutation)
        valid_solutions += valid_crosswords
    return valid_solutions


def main():
    case = ["crossword", "something", "square", "formation"]
    # expected = 6

    print(solution(case))


if __name__ == "__main__":
    main()
