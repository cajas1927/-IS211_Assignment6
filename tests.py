#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for conversions module"""

import unittest
import conversions
import decimal


class ConversionTests(unittest.TestCase):
    """
    Attributes: None
    """
    def test_celcius_to_kelvin(self):
        """ Tests conversion from Celcius to Kelvin.
        """
        expected = decimal.Decimal(273.15)
        returned = conversions.celcius_to_kelvin(0)
        self.assertEqual(returned, expected, msg='Error converting measures.')


    def test_celcius_to_fahrenheit(self):
        """ Tests conversion from Celcius to Fahrenheit.
        """
        expected = 14
        returned = conversions.celcius_to_fahrenheit(-10)
        self.assertEqual(returned, expected, msg='Error converting measures.')


    def test_fahrenheit_to_celcius(self):
        """ Tests conversion from Fahrenheit to Celcius.
        """
        expected = 35
        returned = conversions.fahrenheit_to_celcius(95)
        self.assertEqual(returned, expected, msg='Error converting measures.')


    def test_fahrenheit_to_kelvin(self):
        """ Tests conversion from Fahrenheit to Kelvin.
        """
        expected = decimal.Decimal(262.594)
        returned = conversions.fahrenheit_to_kelvin(13)
        self.assertEqual(returned, expected, msg='Error converting measures.')


    def test_kelvin_to_celcius(self):
        """ Tests conversion from Kelvin to Celcius.
        """
        expected = decimal.Decimal(-273.15)
        returned = conversions.kelvin_to_celcius(0)
        self.assertEqual(returned, expected, msg='Error converting measures.')


    def test_kelvin_to_fahrenheit(self):
        """ Tests conversion from Kelvin to Fahrenheit.
        """
        expected = decimal.Decimal(80.33)
        returned = conversions.kelvin_to_fahrenheit(300)
        self.assertEqual(returned, expected, msg='Error converting measures.')


if __name__ == '__main__':
    unittest.main()