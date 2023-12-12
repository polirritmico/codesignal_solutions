#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os
# import sys
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# import pytest

from src.codesignal_importer import CodesignalImporter


# @pytest.mark.skip()
def test_parse_json() -> None:
    case = ["tests/files/test-5.json"]
    expected_input_vars = ["cities", "roads"]
    expected_cities = 13
    expected_roads = [[11, 0], [5, 3], [6, 2], [12, 3]]
    expected = [[0, 1], [0, 2], [0, 5]]

    importer = CodesignalImporter()
    importer.import_json_testfiles(case)
    output = importer.tests.get("test_case5")
    assert output is not None

    out_vars = output.variables
    out_cities = out_vars.get("cities")
    out_roads = out_vars.get("roads")

    assert len(out_vars) == 2
    for expected_var in expected_input_vars:
        assert expected_var in out_vars

    assert out_cities == expected_cities
    assert out_roads == expected_roads
    assert output.expected == expected
