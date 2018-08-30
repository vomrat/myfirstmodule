# coding=utf-8

from unittest import TestCase

import myfirstmodule


class TestMyFirstModule(TestCase):
    def test_is_string(self):
        s = myfirstmodule.joke()
        self.assertTrue(isinstance(s, basestring))

