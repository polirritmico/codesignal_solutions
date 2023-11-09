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


# @pytest.mark.skip


def test_case12():
    case = [
        "1322222222222224",
        "1100003224024341",
        "110032a241011111",
        "1100101011011111",
        "110062A251011111",
        "1622222225011111",
        "2222222222256565",
    ]
    expected = -71
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case13():
    case = [
        "0p22400003777z24",
        "1a406P0001000101",
        "1064000001000101",
        "1006774001032501",
        "1000001001010001",
        "1000001001064035",
        "6227276A0622Z250",
    ]
    expected = 44
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case14():
    case = [
        "0p22400003777z24",
        "1a40600001000101",
        "1064P00001000101",
        "1006774001032501",
        "1000001001010001",
        "1000001001064035",
        "6227276A0622Z250",
    ]
    expected = -20
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case15():
    case = ["a010", "C01A", "101b", "101B", "c250"]
    expected = -8
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case16():
    case = ["1621544", "1141245", "7321534", "3214142"]
    expected = 0
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case17():
    case = [
        "003006660200000000",
        "030000200050001070",
        "000015002001004000",
        "000007002000020700",
        "003000002020001000",
        "000300010030400701",
        "050030002003040000",
        "001000030702001700",
        "000001030010030000",
        "000100010020200700",
        "000003000304003000",
        "001040010600102000",
        "000300020010000300",
        "002040020020001000",
        "005010020103060030",
        "004004000200001000",
        "000100200003000300",
        "040000010040010500",
        "000000100400030400",
        "000100460013004050",
        "000000100040010500",
    ]
    expected = 0
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case18():
    case = ["Aa7272727777"]
    expected = -10
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case19():
    case = [
        "a2222277272227772224",
        "100000064222B0000001",
        "1000b227500040000001",
        "10000000000000070001",
        "700030000d2400050001",
        "70020000000100000007",
        "70000000000100000007",
        "7000z40000062222D007",
        "70000640000000000007",
        "70000064000405000007",
        "70000006400000167007",
        "70037722500002323007",
        "70010000000000000007",
        "700100000000000003Z7",
        "70070322227727772507",
        "70062500000000000007",
        "70001234567005430007",
        "70004560000076020007",
        "70123000000000010007",
        "6227777772222722722A",
    ]
    expected = -34
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case20():
    case = [
        "a2222277272227772224",
        "100000063222B0000001",
        "1000b227500040000001",
        "10000000000000070001",
        "700030000d2400050001",
        "70020000000100000007",
        "70000000000100000007",
        "7000z40000062222D007",
        "70000640000000000007",
        "70000064000405000007",
        "70000006400000167007",
        "70037722500002323007",
        "70010000000000000007",
        "700100000000000003Z7",
        "70070322227727772507",
        "70062500000000000007",
        "70001234567005430007",
        "70004560000076020007",
        "70123000000000010007",
        "6227777772222722722A",
    ]
    expected = 124
    output = solution(case)
    assert output == expected


# @pytest.mark.skip


def test_case21():
    case = [
        "a1222277272227772224",
        "200000063222B0000001",
        "1000b227500040000001",
        "10000000000000070001",
        "700030000d2400050001",
        "70020000000100000007",
        "70000000000100000007",
        "7000z40000062222D007",
        "70000640000000000007",
        "70000064000405000007",
        "70000006400000167007",
        "70037722500002323007",
        "70010000000000000007",
        "700100000000000003Z7",
        "70070322227727772507",
        "70062500000000000007",
        "70001234567005430007",
        "70004560000076020007",
        "70123000000000010007",
        "6227777772222722722A",
    ]
    expected = 50
    output = solution(case)
    assert output == expected
