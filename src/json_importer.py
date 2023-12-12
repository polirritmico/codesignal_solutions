#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import os

from src.test import Test


class JsonImporter:
    def read_file(self, filename: str) -> dict:
        try:
            with open(os.path.abspath(filename), "r", encoding="utf-8") as stream:
                data: dict = json.load(stream)
        except Exception as err:
            raise IOError(f"Error reading json file {filename}", err)
        return data

    def generate_name(self, filename: str) -> str:
        test_number = "".join(filter(str.isdigit, filename))
        name = f"test_case{test_number}"
        return name

    def import_json_file(self, filename: str) -> Test:
        data = self.read_file(filename)
        test_name = self.generate_name(filename)
        test_inputs = data.get("input", {})
        test_output = data.get("output")
        test = Test(test_name, test_inputs, test_output)
        return test
