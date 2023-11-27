#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Generator

import pytest

from fractal import Fractal


@pytest.fixture
def fractal() -> Generator[Fractal, None, None]:
    fractal = Fractal()
    yield fractal
    del fractal


# @pytest.mark.skip()
def test_rotate90(fractal: Fractal):
    expected = [
        [" ", " ", " "],
        ["|", " ", "|"],
        [" ", "_", " "],
    ]
    output = fractal.rotate_clockwise()
    assert output == expected


# @pytest.mark.skip()
def test_rotate180(fractal: Fractal):
    expected = [
        [" ", "_", " "],
        ["|", " ", " "],
        [" ", "_", " "],
    ]
    output = fractal.rotate_clockwise(turns=2)
    assert output == expected


# @pytest.mark.skip()
def test_rotate270(fractal: Fractal):
    expected = [
        [" ", "_", " "],
        ["|", " ", "|"],
        [" ", " ", " "],
    ]
    output = fractal.rotate_clockwise(turns=3)
    assert output == expected


# @pytest.mark.skip()
def test_case1(fractal: Fractal):
    case = 1
    expected = [[" ", "_", " "], [" ", "_", "|"]]
    fractal.generate_fractal_iterations(case)
    output = fractal.generate_drawing()
    assert output == expected


# @pytest.mark.skip()
def test_case2(fractal: Fractal):
    case = 2
    expected = [
        [" ", "_", " ", " ", " ", "_", " "],
        [" ", "_", "|", " ", "|", "_", " "],
        ["|", " ", " ", "_", " ", " ", "|"],
        ["|", "_", "|", " ", "|", "_", "|"],
    ]
    fractal.generate_fractal_iterations(case)
    output = fractal.generate_drawing()
    assert output == expected


# @pytest.mark.skip()
def test_case3(fractal: Fractal):
    case = 3
    expected = [
        [" ", "_", " ", " ", " ", "_", "_", "_", " ", " ", " ", "_", "_", "_", " "],
        [" ", "_", "|", " ", "|", "_", " ", " ", "|", "_", "|", " ", " ", "_", "|"],
        ["|", " ", " ", "_", " ", " ", "|", " ", " ", "_", " ", " ", "|", "_", " "],
        ["|", "_", "|", " ", "|", "_", "|", " ", "|", " ", "|", "_", "_", "_", "|"],
        [" ", "_", " ", " ", " ", "_", " ", " ", "|", " ", " ", "_", "_", "_", " "],
        ["|", " ", "|", "_", "|", " ", "|", " ", "|", "_", "|", " ", " ", "_", "|"],
        ["|", "_", " ", " ", " ", "_", "|", " ", " ", "_", " ", " ", "|", "_", " "],
        [" ", "_", "|", " ", "|", "_", "_", "_", "|", " ", "|", "_", "_", "_", "|"],
    ]
    fractal.generate_fractal_iterations(case)
    output = fractal.generate_drawing()
    assert output == expected
