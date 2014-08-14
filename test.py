#!/usr/bin/env python
#coding=utf-8

import unittest
from poland import infix2poland


class PolandTest(unittest.TestCase):
    def test_one(self):
        self.assertEqual(infix2poland('a+b'), 'ab+')
    def test_two(self):
        self.assertEqual(infix2poland('a+(b-c)*d'), 'abc-d*+')
    def test_three(self):
        self.assertEqual(infix2poland('a+b*(c*(d+e)-f)-h'), 'abcde+*f-*+h-')

if __name__ == "__main__":
    unittest.main()
