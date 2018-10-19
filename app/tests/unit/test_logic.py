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

    def test_div_with_two_positive_numbers(self):
        c = Calculator()
        assert c.div(50,10) == 5

    def test_div_with_a_possitive_and_negative_number(self):
        c = Calculator()
        assert c.div(50,-10) == -5

    def test_div_with_two_negative_numbers(self):
        c = Calculator()
        assert c.div(-50,-10) == 5

    def test_div_with_out_of_bounds_throws_e(self):
        with pytest.raises(ValueError):
            calculator = Calculator()
            calculator.div(-1001,100)

    def test_div_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            calculator = Calculator()
            calculator.div(50,0)
