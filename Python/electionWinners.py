#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(votes, missing_votes):
    votes.sort(reverse=True)
    if missing_votes == 0 and votes[0] != votes[1]:
        return 1

    eligible_candidates = 0
    for candidate_votes in votes:
        if candidate_votes + missing_votes > votes[0]:
            eligible_candidates += 1
    return eligible_candidates


def main():
    votes = [2, 3, 5, 2]
    votes = [4, 1, 3, 4, 1]
    k = 0
    print(solution(votes, k))

if __name__ == "__main__":
    main()

