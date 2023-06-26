#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools


def valid_crosswords_counter(words: tuple) -> int:
    top = words[0]
    right = words[1]
    btm = words[2]
    left = words[3]
    top_len = len(top)
    left_len = len(left)
    btm_len = len(btm)
    right_len = len(right)

    valid_count = 0

    # Start words position:
    # LT O  RP
    # E     I
    # F     G
    # TB O  T  T  O  M
    #       H
    #
    # Movement order:
    # 1. Right. Vertical. From top i=0 to top len(right_word) - 2
    # 2. Right. Horizontal. From left i=2 to right horizontal_limit
    # 3. Lower. Vertical. From top i=2 to bottom vertical_limit
    # 4. Lower. Horizontal. From left i=0 to right len(bottom_word) - 2
    # 5. Left. Vertical. From top i=0 to bottom len(left_word) - 2
    # 6. Upper. Horizontal. From left i=0 to right len(upper_word) - 2
    # Check where horizontal and vertical offset change

    #counter = 0
    #for idx_upper_hor in range(upper_len - 2):
    #    upper_left = upper[idx_upper_hor]
    #    for idx_left_ver in range(left_len - 2):
    #        left_top = left[idx_left_ver]
    #        if upper_left != left_top:
    #            continue
    #        vertical_limit = min(left_len - idx_left_ver, right_len) + 1  # +1 por range
    #        for idx_bottom_hor in range(bottom_len - 2):
    #            bottom_left = bottom[idx_bottom_hor]
    #            for idx_bottom_ver in range(idx_left_ver + 2, vertical_limit):
    #                left_btm = left[idx_bottom_ver]
    #                if left_btm != bottom_left:
    #                    continue
    #                horizontal_limit = min(upper_len - idx_upper_hor, bottom_len - idx_bottom_hor) + 1
    #                vertical_limit = min(left_len - idx_left_ver, right_len - )
    #                for idx_right_hor in range(idx_left_ver + 2, horizontal_limit):
    #                    upper_right = upper[idx_right_hor + idx_upper_hor - 1]  # -1 por 0-index
    #                    bottom_right = bottom[idx_right_hor + idx_bottom_hor - 1]
    #                    for idx_right_ver in range(vertical_limit):
    #                        right_top = right[idx_right_ver]
    #                        if upper_right != right_top:
    #                            continue
    #                        right_btm = right[idx_bottom_ver - 1]  # -1 por 0-index
    #                        if bottom_right != right_btm:
    #                            continue
    #                        counter += 1
    #                        coords = (
    #                            f"Step: {counter}\n"
    #                            f"UH: {idx_upper_hor}\tLfV: {idx_left_ver}\tBH: {idx_bottom_hor}\t"
    #                            f"BV: {idx_bottom_ver}\tRH: {idx_right_hor}\tRV: {idx_right_ver}"
    #                        )
    #                        letters = (
    #                            f"↑L: {upper_left}\t↑R: {upper_right}\t"
    #                            f"→T: {right_top}\t→B: {right_btm}\n"
    #                            f"↓L: {bottom_left}\t↓R: {bottom_right}\t"
    #                            f"←T: {left_top}\t←B: {left_btm}"
    #                        )
    #                        print(coords)
    #                        print(letters)
    #                        valid_count += 1
    counter = 0
    limit_top_hor = top_len - 2
    limit_left_ver = left_len - 2
    limit_btm_hor = btm_len - 2
    limit_right_ver = right_len - 2
    for idx_top_hor in range(limit_top_hor):
        top_left = top[idx_top_hor]
        for idx_left_ver in range(limit_left_ver):
            left_top = left[idx_left_ver]
            if top_left != left_top:
                continue
            limit_btm_ver = min()
            for idx_btm_hor in range(limit_btm_hor):
                btm_left = btm[idx_btm_hor]
                for idx_btm_ver in range(2, limit_btm_ver):
                    left_btm = left[idx_btm_ver + idx_left_ver]
                    if left_btm != btm_left:
                        continue
                    #limit_right_ver = min(left_len - idx_left_ver, right_len - idx_btm_ver)
                    #limit_right_hor = min(top_len - idx_top_hor, btm_len - idx_btm_ver)
                    #limit_right_hor = min(0, idx_btm_ver)
                    #for idx_right_hor in range(limit_right_hor):
                    #    top_right = top[idx_top_hor + idx_right_hor + 2]
                    #   top_right = top[idx_top_hor + idx_right_hor]
                    #    btm_right = btm[idx_right_hor + 2]
                    #    for idx_right_ver in range(limit_right_ver):
                    #        right_top = right[idx_right_ver]
                    #        right_btm = right[idx_btm_ver + idx_right_ver]
                    #        if top_right != right_top:
                    #            continue
                    #        if btm_right != right_btm:
                    #            continue
                    #        valid_count += 1

    return valid_count


def solution(words: list[str]) -> int:
    if len(words) != 4:
        raise ValueError("Error: Expected 4 words.")
    if any(len(word) < 3 for word in words):
        raise ValueError("Error: Word with less than 3 characters length.")

    valid_solutions = 0
    #words_chars = tuple(list(word) for word in words)
    for permutation in itertools.permutations(words):
        valid_crosswords: int = valid_crosswords_counter(permutation)
        valid_solutions += valid_crosswords
    return valid_solutions


def main():
    case = ["crossword", "square", "formation", "something"]
    # expected = 6
    # case = ["abc", "dee", "abd", "cde"]
    # case = ["abc", "cde", "dee", "abd"]

    print(solution(case))


if __name__ == "__main__":
    main()
