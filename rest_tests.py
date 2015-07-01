#!/usr/bin/python2
# -*- coding: utf-8 -*-

import countries
import unittest
import json

class CountriesTestCase(unittest.TestCase):

    def setUp(self):
        self.app = countries.app.test_client()

    def test_finland(self):
        rv = self.app.get('/countries/FI')
        self.assertEqual(json.loads(rv.data)['capital'], 'Helsinki')

    def test_sweden(self):
        rv = self.app.get('/countries/SE')
        self.assertEqual(json.loads(rv.data)['capital'], 'Stockholm')

    def test_blah(self):
        rv = self.app.get('/countries/BLAH')
        self.assertEqual(rv.status_code, 404)


if __name__ == '__main__':
    unittest.main()
