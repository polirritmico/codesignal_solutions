#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse


def get_args(version: str, argv=None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        add_help=True,
        description="Codesignal Test Importer: A script to quickly integrate Codesignal tests into a working pytest file. The pytest test file is generated from the downloaded HTML, JSON test files, or both.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        prog="importer-test",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"{parser.prog} v{version}",
    )
    parser.add_argument(
        "-s",
        "--source",
        help="File with the python code to test.",
        required=True,
        type=str,
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-t",
        "--test-files",
        nargs="+",  # zero or more files
        help="Json filename(s) with the test case variables and expected output.",
        type=str,
    )
    group.add_argument(
        "-p",
        "--html-page",
        help="HTML source of the Codesignal challenge page to extract the tests.",
        type=str,
    )
    parser.add_argument(
        "-o",
        "--output",
        default="",
        help="The filename of the output python test file.",
        type=str,
    )
    parser.add_argument(
        "-i",
        "--insert-mode",
        action="store_true",
        default=False,
        help="Append the tests into a the test file without removing its content.",
    )

    if len(argv) == 0:
        parser.print_help()
        parser.exit()

    return parser.parse_args(argv)
