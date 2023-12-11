#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1"

import argparse
import json
import os
import sys
from typing import Any


def get_args(argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        add_help=True,
        description="Test importer. A script to import Codesignal html and json tests into a working pytest file.",
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
        "code_file",
        # nargs=1,
        help="File with the code to test.",
        metavar="SOURCE_FILE",
        type=str,
    )
    parser.add_argument(
        "filename",
        nargs="+",  # one or more files
        help="Json filename with the test case variables and expected output.",
        metavar="JSON_FILE",
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
    parser.add_argument(
        "-i",
        "--insert",
        action="store_true",
        default=False,
        help="Append the tests into a the test file without removing its content.",
    )
    parser.add_argument(
        "-p",
        "--page",
        default="",
        help="Import tests from html downloaded page.",
    )

    return parser.parse_args(argv)


class Test:
    def __init__(
        self, name: str, case_variables: dict[str, type], expected: Any
    ) -> None:
        self.name: str = name
        self.variables: dict[str, Any] = case_variables
        self.expected: Any = expected

    def generate_test(self) -> str:
        test_str = "# @pytest.mark.skip()\n"
        test_str += f"def {self.name}():\n"
        indent = "    "
        assert self.name != ""
        assert self.variables is not None and self.variables != {}
        assert self.expected is not None
        for var_name, var_value in self.variables.items():
            test_str += f"{indent}{var_name} = {var_value}\n"
        test_str += f"{indent}expected = {self.expected}\n"
        variables = ", ".join(self.variables.keys())
        test_str += f"{indent}output = solution({variables})\n"
        test_str += f"{indent}assert output == expected\n\n\n"

        return test_str


class JsonTestImporter:
    def __init__(
        self, source_code_name: str, test_files: list[str], insert_mode: bool
    ) -> None:
        self.source_code_file: str = source_code_name
        self.json_test_files: list[str] = test_files
        self.raw_data: dict[str, dict] = {}
        self.test_collection: dict[str, Test] = {}
        self.insert_mode: bool = insert_mode
        self.output_data: str = ""

    def read_file(self, filename):
        try:
            with open(os.path.abspath(filename), "r", encoding="utf-8") as stream:
                raw_data = json.load(stream)
        except Exception as err:
            raise IOError(f"Error reading json file {filename}", err)
        return raw_data

    def read_files(self) -> None:
        self.json_test_files.sort(key=lambda c: int("".join(filter(str.isdigit, c))))
        for file in self.json_test_files:
            self.raw_data[file] = self.read_file(file)

    def write_output_data_to_file(self, target_file: str) -> None:
        write_mode = "a" if self.insert_mode else "w"
        try:
            with open(target_file, write_mode, encoding="utf-8") as file:
                file.write(self.output_data)
        except Exception as err:
            IOError("Error writing to the output file", err)

    def get_header(self) -> str:
        header = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nimport pytest\n\n"
        source_code_file = self.source_code_file
        if source_code_file.endswith(".py"):
            source_code_file = source_code_file[:-3]
        source_import = f"from {source_code_file} import solution\n\n\n"
        return header + source_import

    def generate_test_file_data(self) -> None:
        self.test_collection = self.populate_test_collection(self.raw_data)
        output_file: str = "\n\n" if self.insert_mode else self.get_header()
        for name, test in self.test_collection.items():
            output_file += test.generate_test()
        self.output_data = output_file

    def populate_test_collection(self, raw_data: dict) -> dict[str, Test]:
        assert raw_data is not None or len(raw_data) != 0
        test_collection = {}
        for test_filename, test_data in raw_data.items():
            # Good enough. Maybe provide a more robust way.
            test_number = int("".join(filter(str.isdigit, test_filename)))
            name = f"test_case{test_number}"
            expected_output = test_data.get("output")
            variables: dict[str, Any] = test_data.get("input")
            assert expected_output is not None, "Missing output data"
            assert variables is not None, "Missing input data"
            test_collection[test_filename] = Test(name, variables, expected_output)
        return test_collection

    def export_test_file(self, output_file: str) -> None:
        assert self.output_data != "", "Error: empty output_data."
        if output_file == "":
            output_file = f"test_{self.source_code_file}"
        self.write_output_data_to_file(output_file)


class HtmlTestImporter:
    def __init__(self, filename: str) -> None:
        self.filename = filename


def main(argv: argparse.Namespace) -> None:
    if argv.page != "":
        html_importer = HtmlTestImporter(argv.page)
    importer = JsonTestImporter(argv.code_file, argv.filename, argv.insert)
    importer.read_files()
    importer.generate_test_file_data()
    importer.export_test_file(argv.output)


if __name__ == "__main__":
    main(get_args(["roadsBuilding.py", "-p", "sample.html", "test-5.json"]))
    # main(get_args(sys.argv[1:]))
    sys.exit()
