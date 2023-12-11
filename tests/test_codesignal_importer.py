#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from src.codesignal_importer import CodesignalImporter


def test_foo() -> None:
    foo = CodesignalImporter()
    assert foo.foo == "working"
