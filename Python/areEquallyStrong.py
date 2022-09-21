#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(yourLeft, yourRight, friendsLeft, friendsRight):
    yourStrength = max(yourLeft, yourRight)
    friendsStrength = max(friendsLeft, friendsRight)
    yourWeak= min(yourLeft, yourRight)
    friendsWeak = min(friendsLeft, friendsRight)

    if yourStrength == friendsStrength and yourWeak == friendsWeak:
        return True
    return False

def main():
    yourLeft = 10
    yourRight = 5
    friendsLeft = 5
    friendsRight = 10
    expected = True
    print(solution(yourLeft, yourRight, friendsLeft, friendsRight))

if __name__ == "__main__":
    main()

