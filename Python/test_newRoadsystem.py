#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from newRoadSystem import solution


# @pytest.mark.skip()
def test_case1():
    case = [
        [False, True, False, False],
        [False, False, True, False],
        [True, False, False, True],
        [False, False, True, False],
    ]
    expected = True
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case2():
    case = [
        [False, True, False, False, False, False, False],
        [True, False, False, False, False, False, False],
        [False, False, False, True, False, False, False],
        [False, False, True, False, False, False, False],
        [False, False, False, False, False, False, True],
        [False, False, False, False, True, False, False],
        [False, False, False, False, False, True, False],
    ]
    expected = True
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case3():
    case = [[False, True, False], [False, False, False], [True, False, False]]
    expected = False
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case4():
    case = [
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
        [False, False, False, False],
    ]
    expected = True
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case5():
    case = [[False]]
    expected = True
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case6():
    case = [
        [False, True, True, True, False],
        [True, False, True, True, True],
        [True, True, False, True, False],
        [True, True, True, False, True],
        [True, True, True, True, False],
    ]
    expected = False
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case7():
    case = [
        [False, True, True, True, True],
        [True, False, True, True, True],
        [True, True, False, True, True],
        [True, True, True, False, True],
        [True, True, True, True, False],
    ]
    expected = True
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case8():
    case = [
        [False, True, False, True, True],
        [False, False, False, False, True],
        [True, False, False, True, True],
        [True, True, True, False, False],
        [True, True, True, False, False],
    ]
    expected = False
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case9():
    case = [
        [False, True, True, False, True],
        [True, False, False, True, False],
        [False, True, False, True, False],
        [True, True, True, False, True],
        [True, True, False, False, False],
    ]
    expected = False
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case10():
    case = [
        [False, True, False, True, True],
        [True, False, True, True, True],
        [False, False, False, False, True],
        [False, False, True, False, True],
        [True, False, True, True, False],
    ]
    expected = False
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case11():
    case = [
        [False, False, False, False, True, True, False, True, False, True],
        [False, False, True, False, False, False, True, False, False, True],
        [False, False, False, True, False, False, False, True, False, True],
        [False, True, False, False, True, False, False, True, False, False],
        [False, True, False, True, False, False, False, True, False, False],
        [True, True, True, True, True, False, True, False, True, True],
        [False, False, True, True, True, True, False, False, False, True],
        [True, True, True, False, False, False, False, False, False, False],
        [False, False, False, True, False, True, True, True, False, False],
        [False, True, True, True, True, False, True, False, True, False],
    ]
    expected = False
    output = solution(case)
    assert output == expected


# @pytest.mark.skip()
def test_case12():
    case = [
        [
            False,
            False,
            False,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
        ],
        [
            True,
            False,
            True,
            True,
            False,
            True,
            True,
            True,
            True,
            False,
            False,
            True,
            False,
            False,
        ],
        [
            False,
            False,
            False,
            True,
            False,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            False,
        ],
        [
            True,
            True,
            False,
            False,
            True,
            True,
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            True,
        ],
        [
            False,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            False,
            False,
            True,
            False,
            True,
            False,
        ],
        [
            True,
            True,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            True,
            True,
            True,
            True,
        ],
        [
            True,
            False,
            True,
            True,
            False,
            True,
            False,
            False,
            False,
            False,
            True,
            True,
            True,
            True,
        ],
        [
            False,
            True,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
            True,
            True,
            True,
            False,
            False,
        ],
        [
            True,
            True,
            False,
            False,
            False,
            True,
            True,
            True,
            False,
            False,
            True,
            True,
            True,
            True,
        ],
        [
            True,
            False,
            True,
            False,
            False,
            True,
            False,
            True,
            True,
            False,
            True,
            False,
            True,
            True,
        ],
        [
            True,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            True,
            True,
            False,
            True,
            False,
            False,
        ],
        [
            True,
            True,
            False,
            False,
            True,
            True,
            False,
            False,
            True,
            True,
            True,
            False,
            True,
            True,
        ],
        [
            True,
            True,
            False,
            False,
            True,
            True,
            True,
            True,
            True,
            False,
            True,
            False,
            False,
            False,
        ],
        [
            False,
            False,
            True,
            True,
            True,
            True,
            False,
            False,
            True,
            True,
            True,
            False,
            False,
            False,
        ],
    ]
    expected = True
    output = solution(case)
    assert output == expected
