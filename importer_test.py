#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1"

import argparse
import json
import os
import sys


def get_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        add_help=True,
        description="Json test importer. A script to import Codesignal json tests into a working pytest file.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog="importer-test",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{parser.prog} v{__version__}",
    )
    parser.add_argument(
        "filename",
        nargs="+",  # one or more files
        help="Json filename",
        metavar="FILE",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="",
        help="The filename of the output python test file.",
        metavar="FILE",
        type=str,
    )

    return parser.parse_args(argv)


class JsonTest:
    def __init__(
        self, name: str, case_variables: dict[str, any], expected: any
    ) -> None:
        self.name = name
        self.variables = case_variables
        self.expected = expected

    def generate_test(self, name):
        pass


class JsonTestImporter:
    def __init__(self, file_list: list[str]) -> None:
        self.json_test_files: list[str] = file_list
        self.raw_data: dict[str, json] = {}
        self.test_collection: list[JsonTest] = []

    def read_file(self, filename):
        try:
            with open(os.path.abspath(filename), "r", encoding="utf-8") as stream:
                raw_data = json.load(stream)
        except Exception as err:
            raise IOError(f"Error reading json file {filename}", err)

        return raw_data

    def read_files(self) -> None:
        for file in self.json_test_files:
            self.raw_data[file] = self.read_file(file)

    def get_vars_names(self, file_data: str) -> list[str]:
        vars_names = []
        pass

    def generate_tests_from_input_data(self) -> None:
        self.test_collection = self.populate_test_collection(self.raw_data)

        for test in self.test_collection:
            test_string = test.generate_test()

    def populate_test_collection(self, raw_data: dict) -> list[JsonTest]:
        assert raw_data is not None or len(raw_data) != 0
        test_collection = []
        for test_number, test_filename in enumerate(self.raw_data):
            name = f"test_case{test_number + 1}"
            data: dict[str, str] = self.raw_data[test_filename]
            expected_output = data.get("output")
            variables: dict[str, any] = data.get("input")
            assert expected_output is not None, "Missing output data"
            assert variables is not None, "Missing input data"
            test_collection.append(JsonTest(name, variables, expected_output))
        return test_collection

    def generate_test_file(self, output_file: str) -> None:
        pass


def main(argv: argparse.Namespace) -> None:
    importer = JsonTestImporter(argv.filename)
    importer.read_files()
    importer.generate_tests_from_input_data()
    # importer.generate_test_file(args.output)


if __name__ == "__main__":
    sys.exit(main(get_args(["test-5.json"])))
    # sys.exit(main(get_args(sys.argv[1:])))
