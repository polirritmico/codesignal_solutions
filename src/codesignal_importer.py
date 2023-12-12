#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import Namespace

from src.json_importer import JsonImporter
from src.test import Test


class CodesignalImporter:
    def __init__(self) -> None:
        self.tests: dict[str, Test] = {}

    def run(self, args: Namespace):
        if len(args.test_files) != 0:
            self.import_json_testfiles(args.test_files)

    def import_json_testfiles(self, test_files: list[str]) -> None:
        for filename in test_files:
            test = JsonImporter().import_json_file(filename)
            self.tests[test.name] = test
