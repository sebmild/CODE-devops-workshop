from unittest import TestCase
from calculator.logic import Calculator
import pytest


class CalculatorTests(TestCase):
    def test_mul_with_two_positive_numbers(self):
        c = Calculator()
        assert c.mul(5, 10) == 50

    def test_mul_with_two_negative_numbers(self):
        c = Calculator()
        assert c.mul(-5,-10) == 50

    def test_mul_with_out_of_bounds_throws_e(self):
        with pytest.raises(ValueError):
            calculator = Calculator()
            calculator.mul(-1001,100)

    def test_div(self):
        pass
