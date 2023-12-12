#!/usr/bin/env python
# -*- coding: utf-8 -*-

__version__ = "0.1"

import sys

from src.cli import get_args
from src.codesignal_importer import CodesignalImporter


def main(argv=None):
    parsed_args = get_args(__version__, argv)
    importer = CodesignalImporter()
    importer.run(parsed_args)


if __name__ == "__main__":
    main(sys.argv[1:])
    sys.exit()
