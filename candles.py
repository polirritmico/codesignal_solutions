#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(candles, make_new):
    burns = candles
    extra_candles = (burns // make_new)
    extra_wax = burns % make_new
    while extra_candles != 0:
        burns += extra_candles

        pass



def main():
    candles_number = 3
    make_new = 2
    expected = 1
    #expected = 9
    print(solution(candles_number, make_new))

if __name__ == "__main__":
    main()

