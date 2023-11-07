#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from pipesGame import Circuit, solution


@pytest.fixture(autouse=True)
def reset_circuit_class_variable_double_layer_counter():
    Circuit.counted_double_layer = []


# @pytest.mark.skip
def test_case1():
    case = [
        "a224C22300000",
        "0001643722B00",
        "0b27275100000",
        "00c7256500000",
        "0006A45000000",
    ]
    expected = 19
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case2():
    case = ["a000", "000A"]
    expected = 0
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case3():
    case = ["a727272777A"]
    expected = 9
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case4():
    case = ["a", "7", "1", "7", "7", "1", "1", "A"]
    expected = 6
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case5():
    case = [
        "A0000b0000",
        "0000000000",
        "0000000000",
        "0000a00000",
        "0000000000",
        "0c00000000",
        "01000000B0",
        "0C00000000",
    ]
    expected = 1
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case6():
    case = [
        "0000000000",
        "0000000000",
        "0000000000",
        "0000000000",
        "0000000000",
        "0000000000",
        "0000000000",
        "0000000000",
    ]
    expected = 0
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case7():
    case = [
        "0020400040",
        "1203300300",
        "7340000000",
        "2040100000",
        "7000500700",
        "0000200000",
        "0002303000",
        "0000000600",
    ]
    expected = 0
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case8():
    case = [
        "0002270003777z24",
        "3a40052001000101",
        "1064000001000101",
        "1006774001032501",
        "1000001001010001",
        "1010001001064035",
        "6227206A0622Z250",
    ]
    expected = -48
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case9():
    case = [
        "00p2400003777z24",
        "1a406P0001000101",
        "1064000001000101",
        "1006774001032501",
        "1000001001010001",
        "1000001001064035",
        "6227276A0622Z250",
    ]
    expected = 43
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case10():
    case = [
        "3277222400000000",
        "1000032A40000000",
        "1000010110000000",
        "1Q2227277q000000",
        "1000010110000000",
        "1000062a50000000",
        "6222222500000000",
    ]
    expected = 40
    output = solution(case)
    assert output == expected


# @pytest.mark.skip
def test_case11():
    case = [
        "3222222400000000",
        "1000032A40000000",
        "1000010110000000",
        "72q227277Q000000",
        "1000010110000000",
        "1000062a50000000",
        "6222222500000000",
    ]
    expected = -12
    output = solution(case)
    assert output == expected
