#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
You find yourself in Bananaland trying to buy a banana. You are super rich so
you have an unlimited supply of banana-coins, but you are trying to use as few
coins as possible.

The coin values available in Bananaland are stored in a sorted array coins.
coins[0] = 1, and for each i (0 < i < coins.length) coins[i] is divisible by
coins[i - 1]. Find the minimal number of banana-coins you'll have to spend to
buy a banana given the banana's price.

Example

For coins = [1, 2, 10] and price = 28, the output should be
solution(coins, price) = 6.

You have to use 10 twice, and 2 four times.
"""


def solution(coins: list[int], price: int) -> int:
    used_coins = 0
    remaining = price
    for coin_value in [*reversed(coins)]:
        current_coin_amount = remaining // coin_value
        used_coins += current_coin_amount
        remaining -= coin_value * current_coin_amount
        if remaining == 0:
            return used_coins


def main():
    coins = [1, 2, 10]
    price = 28
    # expected = 6
    print(solution(coins, price))


if __name__ == "__main__":
    main()
