#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(score1, score2) -> bool:
    if score1 == score2:
        return False

    winning = max(score1, score2)
    lossing = min(score1, score2)
    if winning == 7 and lossing >= 5:
        return True
    if winning == 6 and lossing < 5:
        return True
    return False



def main():
    score1 = 3
    score2 = 6
    # Expected: True
    print(solution(score1, score2))

if __name__ == "__main__":
    main()

