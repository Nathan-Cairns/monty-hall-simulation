#!/usr/bin/env python3

from .context import mhall

import unittest

class BasicTestSuite(unittest.TestCase):
    """Basic Test Cases"""

    def test(self):
        assert True

if __name__ == '__main__':
    unittest.main()
