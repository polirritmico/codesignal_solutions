#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from roadsBuilding import solution


# @pytest.mark.skip()
def test_case1():
    cities = 4
    roads = [[0, 1], [1, 2], [2, 0]]
    expected = [[0, 3], [1, 3], [2, 3]]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case2():
    cities = 1
    roads = []
    expected = []
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case3():
    cities = 9
    roads = [
        [5, 8],
        [6, 0],
        [0, 5],
        [4, 1],
        [0, 1],
        [7, 0],
        [6, 8],
        [7, 3],
        [2, 6],
        [0, 2],
        [0, 3],
        [8, 7],
        [5, 4],
        [8, 4],
        [8, 2],
        [7, 1],
        [4, 6],
        [5, 6],
        [4, 2],
        [4, 7],
        [2, 7],
        [3, 6],
        [8, 0],
        [1, 6],
        [3, 2],
        [3, 4],
        [4, 0],
        [6, 7],
        [5, 7],
    ]
    expected = [[1, 2], [1, 3], [1, 5], [1, 8], [2, 5], [3, 5], [3, 8]]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case6():
    cities = 7
    roads = [
        [3, 1],
        [1, 6],
        [2, 5],
        [4, 2],
        [2, 0],
        [0, 1],
        [3, 5],
        [5, 1],
        [5, 4],
        [6, 3],
        [1, 2],
        [2, 6],
        [6, 0],
        [6, 5],
        [4, 3],
        [2, 3],
        [4, 6],
        [5, 0],
    ]
    expected = [[0, 3], [0, 4], [1, 4]]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case7():
    cities = 6
    roads = [
        [1, 2],
        [0, 2],
        [1, 4],
        [4, 2],
        [3, 5],
        [1, 0],
        [5, 0],
        [3, 1],
        [0, 4],
        [5, 1],
        [3, 2],
        [3, 0],
        [2, 5],
    ]
    expected = [[3, 4], [4, 5]]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case10():
    cities = 11
    roads = [
        [0, 2],
        [0, 9],
        [3, 8],
        [8, 10],
        [7, 8],
        [7, 6],
        [2, 9],
        [8, 4],
        [7, 0],
        [6, 10],
        [5, 6],
        [7, 10],
        [9, 8],
        [2, 7],
        [3, 2],
        [6, 8],
        [5, 4],
        [1, 9],
        [10, 5],
        [9, 5],
        [8, 5],
        [1, 8],
        [5, 3],
        [7, 1],
        [4, 2],
        [8, 0],
        [10, 3],
        [4, 6],
        [9, 7],
        [3, 1],
        [9, 3],
        [1, 10],
        [8, 2],
        [7, 4],
        [0, 6],
        [0, 5],
        [10, 9],
        [10, 0],
        [4, 9],
        [5, 7],
        [0, 1],
        [6, 1],
    ]
    expected = [
        [0, 3],
        [0, 4],
        [1, 2],
        [1, 4],
        [1, 5],
        [2, 5],
        [2, 6],
        [2, 10],
        [3, 4],
        [3, 6],
        [3, 7],
        [4, 10],
        [6, 9],
    ]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case12():
    cities = 7
    roads = [
        [5, 3],
        [4, 0],
        [0, 1],
        [6, 5],
        [3, 4],
        [0, 3],
        [2, 0],
        [2, 1],
        [2, 6],
        [5, 1],
        [3, 2],
        [0, 5],
        [1, 3],
        [1, 4],
        [6, 3],
    ]
    expected = [[0, 6], [1, 6], [2, 4], [2, 5], [4, 5], [4, 6]]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case4():
    cities = 17
    roads = [
        [5, 12],
        [3, 5],
        [10, 9],
        [3, 10],
        [6, 14],
        [6, 13],
        [7, 1],
        [14, 8],
        [9, 6],
        [14, 4],
        [6, 12],
        [3, 11],
        [11, 4],
        [0, 6],
        [13, 16],
        [12, 8],
        [7, 8],
        [16, 14],
        [0, 1],
        [14, 12],
        [11, 7],
        [4, 1],
        [13, 11],
        [14, 2],
        [9, 7],
        [0, 3],
        [3, 16],
        [8, 5],
        [4, 2],
        [1, 2],
        [11, 5],
        [14, 9],
        [6, 2],
        [10, 0],
        [16, 10],
        [15, 4],
        [15, 5],
        [6, 16],
        [1, 13],
        [15, 6],
        [12, 0],
        [1, 8],
        [16, 1],
        [16, 8],
        [5, 6],
        [3, 2],
        [0, 5],
        [10, 12],
        [15, 14],
        [8, 11],
        [13, 15],
        [7, 16],
        [16, 9],
        [15, 16],
        [10, 6],
        [8, 10],
        [7, 5],
        [8, 15],
        [11, 1],
        [6, 3],
        [0, 13],
        [11, 12],
        [2, 13],
        [13, 5],
        [14, 1],
        [9, 4],
        [11, 16],
        [11, 2],
        [5, 9],
        [1, 9],
        [12, 2],
        [6, 11],
        [2, 10],
        [0, 2],
        [10, 14],
        [3, 4],
        [4, 6],
        [13, 9],
        [15, 9],
        [7, 12],
        [11, 14],
        [0, 14],
        [3, 14],
        [16, 0],
        [14, 7],
        [12, 13],
        [6, 8],
        [10, 13],
        [1, 3],
        [8, 13],
        [4, 8],
        [3, 7],
        [4, 0],
        [10, 7],
        [1, 15],
        [12, 16],
        [0, 15],
        [15, 7],
        [11, 9],
    ]
    expected = [
        [0, 7],
        [0, 8],
        [0, 9],
        [0, 11],
        [1, 5],
        [1, 6],
        [1, 10],
        [1, 12],
        [2, 5],
        [2, 7],
        [2, 8],
        [2, 9],
        [2, 15],
        [2, 16],
        [3, 8],
        [3, 9],
        [3, 12],
        [3, 13],
        [3, 15],
        [4, 5],
        [4, 7],
        [4, 10],
        [4, 12],
        [4, 13],
        [4, 16],
        [5, 10],
        [5, 14],
        [5, 16],
        [6, 7],
        [7, 13],
        [8, 9],
        [9, 12],
        [10, 11],
        [10, 15],
        [11, 15],
        [12, 15],
        [13, 14],
    ]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case5():
    cities = 13
    roads = [
        [11, 0],
        [5, 3],
        [6, 2],
        [4, 0],
        [3, 7],
        [8, 9],
        [1, 4],
        [9, 0],
        [0, 8],
        [4, 9],
        [5, 7],
        [8, 6],
        [5, 2],
        [10, 7],
        [5, 11],
        [8, 2],
        [6, 0],
        [12, 0],
        [6, 12],
        [3, 6],
        [7, 1],
        [7, 12],
        [6, 9],
        [6, 11],
        [12, 8],
        [8, 5],
        [8, 11],
        [2, 12],
        [2, 1],
        [0, 3],
        [8, 3],
        [6, 1],
        [1, 10],
        [10, 12],
        [8, 7],
        [6, 10],
        [2, 4],
        [10, 3],
        [4, 5],
        [11, 2],
        [4, 11],
        [0, 7],
        [3, 11],
        [8, 10],
        [2, 9],
        [5, 1],
        [10, 11],
        [9, 3],
        [3, 4],
        [1, 9],
        [11, 12],
        [11, 9],
        [4, 12],
        [3, 2],
        [12, 3],
    ]
    expected = [
        [0, 1],
        [0, 2],
        [0, 5],
        [0, 10],
        [1, 3],
        [1, 8],
        [1, 11],
        [1, 12],
        [2, 7],
        [2, 10],
        [4, 6],
        [4, 7],
        [4, 8],
        [4, 10],
        [5, 6],
        [5, 9],
        [5, 10],
        [5, 12],
        [6, 7],
        [7, 9],
        [7, 11],
        [9, 10],
        [9, 12],
    ]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case8():
    cities = 18
    roads = [
        [3, 0],
        [0, 12],
        [5, 15],
        [10, 1],
        [0, 7],
        [8, 9],
        [17, 3],
        [1, 0],
        [8, 15],
        [14, 11],
        [7, 13],
        [14, 2],
        [1, 13],
        [2, 8],
        [15, 16],
        [2, 15],
        [10, 17],
        [11, 8],
        [14, 16],
        [17, 1],
        [4, 6],
        [16, 11],
        [12, 8],
        [11, 10],
        [14, 10],
        [16, 10],
        [2, 0],
        [14, 6],
        [3, 10],
        [7, 15],
        [5, 3],
        [7, 9],
        [15, 12],
        [1, 12],
        [9, 11],
        [7, 16],
        [8, 4],
        [12, 3],
        [8, 5],
        [0, 16],
        [7, 5],
        [10, 7],
        [12, 16],
        [15, 17],
        [10, 2],
        [6, 13],
        [5, 14],
        [9, 3],
        [7, 8],
        [15, 0],
        [15, 3],
        [17, 0],
        [14, 15],
        [14, 0],
        [14, 3],
        [11, 15],
        [6, 8],
        [2, 16],
        [3, 4],
        [4, 17],
        [4, 5],
        [13, 11],
        [9, 4],
        [10, 8],
        [10, 13],
        [4, 15],
        [2, 3],
        [12, 2],
        [13, 0],
        [10, 12],
        [16, 4],
        [13, 3],
        [17, 5],
        [8, 13],
        [13, 4],
        [12, 5],
        [2, 4],
        [1, 16],
        [1, 6],
        [17, 13],
        [16, 9],
        [17, 9],
        [9, 13],
        [5, 6],
        [13, 16],
        [0, 8],
        [6, 0],
        [16, 3],
        [0, 4],
        [5, 1],
        [6, 3],
        [3, 11],
        [7, 4],
        [6, 12],
        [16, 17],
        [5, 11],
        [9, 0],
        [1, 14],
        [15, 9],
        [9, 5],
        [2, 11],
        [4, 1],
        [8, 14],
        [13, 12],
        [1, 8],
        [0, 5],
    ]
    expected = [
        [0, 10],
        [0, 11],
        [1, 2],
        [1, 3],
        [1, 7],
        [1, 9],
        [1, 11],
        [1, 15],
        [2, 5],
        [2, 6],
        [2, 7],
        [2, 9],
        [2, 13],
        [2, 17],
        [3, 7],
        [3, 8],
        [4, 10],
        [4, 11],
        [4, 12],
        [4, 14],
        [5, 10],
        [5, 13],
        [5, 16],
        [6, 7],
        [6, 9],
        [6, 10],
        [6, 11],
        [6, 15],
        [6, 16],
        [6, 17],
        [7, 11],
        [7, 12],
        [7, 14],
        [7, 17],
        [8, 16],
        [8, 17],
        [9, 10],
        [9, 12],
        [9, 14],
        [10, 15],
        [11, 12],
        [11, 17],
        [12, 14],
        [12, 17],
        [13, 14],
        [13, 15],
        [14, 17],
    ]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case9():
    cities = 16
    roads = [
        [6, 7],
        [3, 6],
        [11, 14],
        [8, 7],
        [0, 2],
        [3, 11],
        [10, 4],
        [10, 7],
        [4, 0],
        [5, 4],
        [2, 14],
        [5, 8],
        [12, 13],
        [8, 14],
        [0, 12],
        [2, 3],
        [14, 7],
        [2, 12],
        [6, 2],
        [7, 9],
        [9, 6],
        [4, 15],
        [6, 10],
        [8, 12],
        [12, 15],
        [1, 0],
        [4, 14],
        [0, 5],
        [4, 6],
        [1, 3],
        [0, 7],
        [15, 2],
        [4, 8],
        [4, 11],
        [0, 6],
        [7, 12],
        [11, 2],
        [11, 13],
        [13, 6],
        [5, 6],
        [1, 7],
        [11, 15],
        [1, 8],
        [4, 2],
        [6, 11],
        [5, 3],
        [0, 13],
        [5, 1],
        [2, 8],
        [13, 2],
        [12, 1],
        [6, 15],
        [6, 1],
        [14, 9],
        [2, 10],
        [6, 14],
        [10, 11],
        [6, 8],
        [3, 7],
        [10, 1],
        [13, 9],
        [8, 9],
        [13, 4],
        [11, 9],
        [14, 0],
        [13, 7],
        [0, 9],
        [5, 14],
        [5, 15],
        [0, 10],
        [3, 13],
        [0, 11],
        [10, 14],
        [10, 12],
        [5, 11],
        [8, 3],
        [2, 9],
        [8, 15],
        [3, 10],
        [13, 10],
        [13, 14],
        [6, 12],
        [3, 0],
        [10, 15],
        [14, 3],
        [4, 12],
        [1, 14],
    ]
    expected = [
        [0, 8],
        [0, 15],
        [1, 2],
        [1, 4],
        [1, 9],
        [1, 11],
        [1, 13],
        [1, 15],
        [2, 5],
        [2, 7],
        [3, 4],
        [3, 9],
        [3, 12],
        [3, 15],
        [4, 7],
        [4, 9],
        [5, 7],
        [5, 9],
        [5, 10],
        [5, 12],
        [5, 13],
        [7, 11],
        [7, 15],
        [8, 10],
        [8, 11],
        [8, 13],
        [9, 10],
        [9, 12],
        [9, 15],
        [11, 12],
        [12, 14],
        [13, 15],
        [14, 15],
    ]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case11():
    cities = 13
    roads = [
        [7, 6],
        [1, 7],
        [2, 6],
        [6, 4],
        [4, 7],
        [3, 9],
        [12, 4],
        [0, 1],
        [8, 4],
        [1, 5],
        [6, 0],
        [6, 12],
        [0, 4],
        [10, 1],
        [2, 10],
        [7, 8],
        [1, 2],
        [4, 11],
        [12, 0],
        [7, 9],
        [5, 4],
        [8, 0],
        [11, 12],
        [11, 7],
        [5, 6],
        [5, 8],
        [7, 2],
        [3, 12],
        [10, 12],
        [10, 4],
        [11, 1],
        [10, 7],
        [9, 0],
        [0, 11],
        [9, 6],
        [10, 8],
        [1, 8],
        [9, 8],
        [8, 11],
        [6, 11],
        [12, 5],
        [2, 12],
        [9, 12],
        [9, 11],
        [3, 5],
        [7, 5],
        [10, 0],
        [10, 3],
        [11, 2],
        [12, 1],
        [3, 1],
        [1, 4],
        [10, 11],
        [10, 9],
        [11, 5],
        [2, 4],
        [7, 3],
        [5, 2],
        [12, 7],
        [1, 6],
    ]
    expected = [
        [0, 2],
        [0, 3],
        [0, 5],
        [0, 7],
        [1, 9],
        [2, 3],
        [2, 8],
        [2, 9],
        [3, 4],
        [3, 6],
        [3, 8],
        [3, 11],
        [4, 9],
        [5, 9],
        [5, 10],
        [6, 8],
        [6, 10],
        [8, 12],
    ]
    output = solution(cities, roads)
    assert output == expected


# @pytest.mark.skip()
def test_case13():
    cities = 13
    roads = [
        [11, 9],
        [6, 12],
        [2, 7],
        [6, 1],
        [1, 10],
        [4, 0],
        [10, 7],
        [5, 8],
        [8, 1],
        [12, 10],
        [9, 4],
        [7, 4],
        [11, 12],
        [2, 10],
        [10, 9],
        [1, 2],
        [10, 3],
        [4, 8],
        [3, 2],
        [3, 9],
        [6, 11],
        [5, 11],
        [0, 3],
        [1, 7],
        [5, 1],
        [6, 8],
        [0, 6],
        [12, 7],
        [5, 3],
        [1, 12],
        [7, 3],
        [2, 6],
        [8, 7],
        [9, 5],
        [11, 7],
        [3, 11],
        [2, 4],
        [0, 5],
        [2, 5],
        [10, 4],
        [6, 7],
        [4, 1],
        [5, 10],
        [2, 8],
        [4, 5],
        [2, 11],
        [8, 9],
        [3, 6],
        [0, 11],
        [0, 9],
        [8, 11],
        [9, 12],
        [8, 12],
        [6, 5],
        [1, 3],
        [11, 1],
        [1, 9],
        [11, 4],
    ]
    expected = [
        [0, 1],
        [0, 2],
        [0, 7],
        [0, 8],
        [0, 10],
        [0, 12],
        [2, 9],
        [2, 12],
        [3, 4],
        [3, 8],
        [3, 12],
        [4, 6],
        [4, 12],
        [5, 7],
        [5, 12],
        [6, 9],
        [6, 10],
        [7, 9],
        [8, 10],
        [10, 11],
    ]
    output = solution(cities, roads)
    assert output == expected
