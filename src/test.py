#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Any


class Test:
    name: str
    variables: dict[str, Any]
    expected: Any

    def __init__(
        self, name: str, case_variables: dict[str, Any], expected: Any
    ) -> None:
        assert len(case_variables) != 0
        self.name = name
        self.variables = case_variables
        self.expected = expected

    def generate_test(self, source_filename: str) -> str:
        self.check_variables()
        indent = " " * 4
        test: str = "# @pytest.mark.skip()\n"
        test += f"def {self.name}():\n"
        for var_name, var_value in self.variables.items():
            test += f"{indent}{var_name} = {var_value}\n"
        test += f"{indent}expected = {self.expected}\n"
        variables = ", ".join(self.variables.keys())
        test += f"{indent}output = solution({variables})\n"
        test += f"{indent}assert output == expected\n\n\n"

        return test

    def check_variables(self) -> None:
        msg = "Error generating the test string: "
        assert self.expected is not None, msg + "Missing expected"
        assert self.name != "", msg + "Missing name"
        assert self.variables is not None and self.variables != {}, msg + "No variables"
