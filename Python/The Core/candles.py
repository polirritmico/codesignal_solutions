#!/usr/bin/env python
# -*- coding: utf-8 -*-

def solution(candles, needed_wax):
    burned_candles = 0
    wax = 0
    while True:
        for candle in range(candles):
            burned_candles += 1
            wax += 1
            candles -= 1

        if wax >= needed_wax:
            candles += 1
            wax -= needed_wax
        elif candles == 0:
            return burned_candles


def main():
    candles_number = 3
    make_new = 2
    expected = 1
    #expected = 9
    print(solution(candles_number, make_new))

if __name__ == "__main__":
    main()

