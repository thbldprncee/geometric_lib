import unittest
import math

from geometric_lib.circle import area, perimeter


class CircleAreaTestCases(unittest.TestCase):
    """Test cases for circle area function"""

    def test_circle_integer_first(self):
        """Test area with small positive integer"""
        self.assertEqual(area(5), math.pi * 5 * 5)

    def test_circle_integer_second(self):
        """Test area with large positive integer"""
        self.assertEqual(area(65536), math.pi * 65536 * 65536)

    def test_circle_float_first(self):
        """Test area with float value"""
        self.assertAlmostEqual(area(2.5), math.pi * 2.5 * 2.5)

    def test_circle_float_second(self):
        """Test area with another float value"""
        self.assertAlmostEqual(area(10.75), math.pi * 10.75 * 10.75)

    def test_circle_string_first(self):
        """Test area with string input"""
        with self.assertRaises(TypeError):
            area('23')

    def test_circle_string_second(self):
        """Test area with another string input"""
        with self.assertRaises(TypeError):
            area('123')

    def test_circle_bool_first(self):
        """Test area with boolean True"""
        with self.assertRaises(TypeError):
            area(True)

    def test_circle_bool_second(self):
        """Test area with boolean False"""
        with self.assertRaises(TypeError):
            area(False)

    def test_circle_zero_integer(self):
        """Test area with zero radius"""
        with self.assertRaises(ValueError):
            area(0)

    def test_circle_negative_integer_first(self):
        """Test area with small negative integer"""
        with self.assertRaises(ValueError):
            area(-1)

    def test_circle_negative_integer_second(self):
        """Test area with large negative integer"""
        with self.assertRaises(ValueError):
            area(-65536)

    def test_circle_negative_float(self):
        """Test area with negative float"""
        with self.assertRaises(ValueError):
            area(-3.14)

    def test_circle_none_value(self):
        """Test area with None value"""
        with self.assertRaises(TypeError):
            area(None)

    def test_circle_list_value(self):
        """Test area with list input"""
        with self.assertRaises(TypeError):
            area([5])


class CirclePerimeterTestCases(unittest.TestCase):
    """Test cases for circle perimeter function"""

    def test_perimeter_integer_first(self):
        """Test perimeter with small positive integer"""
        self.assertEqual(perimeter(5), 2 * math.pi * 5)

    def test_perimeter_integer_second(self):
        """Test perimeter with large positive integer"""
        self.assertEqual(perimeter(65536), 2 * math.pi * 65536)

    def test_perimeter_float_first(self):
        """Test perimeter with float value"""
        self.assertAlmostEqual(perimeter(2.5), 2 * math.pi * 2.5)

    def test_perimeter_float_second(self):
        """Test perimeter with another float value"""
        self.assertAlmostEqual(perimeter(10.75), 2 * math.pi * 10.75)

    def test_perimeter_string_first(self):
        """Test perimeter with string input"""
        with self.assertRaises(TypeError):
            perimeter('23')

    def test_perimeter_string_second(self):
        """Test perimeter with another string input"""
        with self.assertRaises(TypeError):
            perimeter('123')

    def test_perimeter_bool_first(self):
        """Test perimeter with boolean True"""
        with self.assertRaises(TypeError):
            perimeter(True)

    def test_perimeter_bool_second(self):
        """Test perimeter with boolean False"""
        with self.assertRaises(TypeError):
            perimeter(False)

    def test_perimeter_zero_integer(self):
        """Test perimeter with zero radius"""
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_integer_first(self):
        """Test perimeter with small negative integer"""
        with self.assertRaises(ValueError):
            perimeter(-1)

    def test_perimeter_negative_integer_second(self):
        """Test perimeter with large negative integer"""
        with self.assertRaises(ValueError):
            perimeter(-65536)

    def test_perimeter_negative_float(self):
        """Test perimeter with negative float"""
        with self.assertRaises(ValueError):
            perimeter(-3.14)

    def test_perimeter_none_value(self):
        """Test perimeter with None value"""
        with self.assertRaises(TypeError):
            perimeter(None)


if __name__ == '__main__':
    unittest.main()