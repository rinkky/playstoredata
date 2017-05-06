#!python2
# coding=utf8

import unittest
import sys
import os

sys.path.append(os.path.join(sys.path[0],os.pardir))
from datagetter import appmonsta

class TestAppmonsta(unittest.TestCase):

    def test_get_detail_by_uniqname(self):
        uniq_name = "com.Ricky.ShadowRun"
        app = appmonsta.get_detail_by_uniqname(uniq_name)
        self.assertEqual(uniq_name, app["uniq_name"])
        self.assertRegexpMatches(app["name"], r"\w+")
        self.assertRegexpMatches(app["price"], r"Free|(\d+(\.\d+)?)")
