import unittest
import math

from geometric_lib.rectangle import area, perimeter


class RectangleAreaTestCases(unittest.TestCase):
    """Test cases for rectangle area function"""

    def test_rectangle_integer_sides(self):
        """Test area with integer sides"""
        self.assertEqual(area(5, 3), 5 * 3)
        self.assertEqual(area(10, 7), 10 * 7)

    def test_rectangle_large_integers(self):
        """Test area with large integer sides"""
        self.assertEqual(area(65536, 32768), 65536 * 32768)

    def test_rectangle_float_sides(self):
        """Test area with float sides"""
        self.assertAlmostEqual(area(2.5, 3.7), 2.5 * 3.7)
        self.assertAlmostEqual(area(10.75, 4.25), 10.75 * 4.25)

    def test_rectangle_mixed_types(self):
        """Test area with mixed integer and float"""
        self.assertAlmostEqual(area(5, 3.5), 5 * 3.5)
        self.assertAlmostEqual(area(2.5, 4), 2.5 * 4)

    def test_rectangle_string_first_side(self):
        """Test area with string as first side"""
        with self.assertRaises(TypeError):
            area('23', 5)

    def test_rectangle_string_second_side(self):
        """Test area with string as second side"""
        with self.assertRaises(TypeError):
            area(5, '23')

    def test_rectangle_both_strings(self):
        """Test area with both sides as strings"""
        with self.assertRaises(TypeError):
            area('5', '3')

    def test_rectangle_bool_first_side(self):
        """Test area with boolean as first side"""
        with self.assertRaises(TypeError):
            area(True, 5)

    def test_rectangle_bool_second_side(self):
        """Test area with boolean as second side"""
        with self.assertRaises(TypeError):
            area(5, False)

    def test_rectangle_zero_first_side(self):
        """Test area with zero as first side"""
        with self.assertRaises(ValueError):
            area(0, 5)

    def test_rectangle_zero_second_side(self):
        """Test area with zero as second side"""
        with self.assertRaises(ValueError):
            area(5, 0)

    def test_rectangle_both_sides_zero(self):
        """Test area with both sides zero"""
        with self.assertRaises(ValueError):
            area(0, 0)

    def test_rectangle_negative_first_side(self):
        """Test area with negative first side"""
        with self.assertRaises(ValueError):
            area(-5, 3)

    def test_rectangle_negative_second_side(self):
        """Test area with negative second side"""
        with self.assertRaises(ValueError):
            area(5, -3)

    def test_rectangle_both_sides_negative(self):
        """Test area with both sides negative"""
        with self.assertRaises(ValueError):
            area(-5, -3)

    def test_rectangle_negative_float_sides(self):
        """Test area with negative float sides"""
        with self.assertRaises(ValueError):
            area(-2.5, 3.7)
        with self.assertRaises(ValueError):
            area(2.5, -3.7)

    def test_rectangle_none_first_side(self):
        """Test area with None as first side"""
        with self.assertRaises(TypeError):
            area(None, 5)

    def test_rectangle_none_second_side(self):
        """Test area with None as second side"""
        with self.assertRaises(TypeError):
            area(5, None)

    def test_rectangle_list_sides(self):
        """Test area with list as sides"""
        with self.assertRaises(TypeError):
            area([5], 3)
        with self.assertRaises(TypeError):
            area(5, [3])

    def test_rectangle_square_case(self):
        """Test area with equal sides (square)"""
        self.assertEqual(area(4, 4), 16)
        self.assertAlmostEqual(area(2.5, 2.5), 6.25)


class RectanglePerimeterTestCases(unittest.TestCase):
    """Test cases for rectangle perimeter function"""

    def test_perimeter_integer_sides(self):
        """Test perimeter with integer sides"""
        self.assertEqual(perimeter(5, 3), 2 * (5 + 3))
        self.assertEqual(perimeter(10, 7), 2 * (10 + 7))

    def test_perimeter_large_integers(self):
        """Test perimeter with large integer sides"""
        self.assertEqual(perimeter(65536, 32768), 2 * (65536 + 32768))

    def test_perimeter_float_sides(self):
        """Test perimeter with float sides"""
        self.assertAlmostEqual(perimeter(2.5, 3.7), 2 * (2.5 + 3.7))
        self.assertAlmostEqual(perimeter(10.75, 4.25), 2 * (10.75 + 4.25))

    def test_perimeter_mixed_types(self):
        """Test perimeter with mixed integer and float"""
        self.assertAlmostEqual(perimeter(5, 3.5), 2 * (5 + 3.5))
        self.assertAlmostEqual(perimeter(2.5, 4), 2 * (2.5 + 4))

    def test_perimeter_string_first_side(self):
        """Test perimeter with string as first side"""
        with self.assertRaises(TypeError):
            perimeter('23', 5)

    def test_perimeter_string_second_side(self):
        """Test perimeter with string as second side"""
        with self.assertRaises(TypeError):
            perimeter(5, '23')

    def test_perimeter_both_strings(self):
        """Test perimeter with both sides as strings"""
        with self.assertRaises(TypeError):
            perimeter('5', '3')

    def test_perimeter_bool_first_side(self):
        """Test perimeter with boolean as first side"""
        with self.assertRaises(TypeError):
            perimeter(True, 5)

    def test_perimeter_bool_second_side(self):
        """Test perimeter with boolean as second side"""
        with self.assertRaises(TypeError):
            perimeter(5, False)

    def test_perimeter_zero_first_side(self):
        """Test perimeter with zero as first side"""
        with self.assertRaises(ValueError):
            perimeter(0, 5)

    def test_perimeter_zero_second_side(self):
        """Test perimeter with zero as second side"""
        with self.assertRaises(ValueError):
            perimeter(5, 0)

    def test_perimeter_both_sides_zero(self):
        """Test perimeter with both sides zero"""
        with self.assertRaises(ValueError):
            perimeter(0, 0)

    def test_perimeter_negative_first_side(self):
        """Test perimeter with negative first side"""
        with self.assertRaises(ValueError):
            perimeter(-5, 3)

    def test_perimeter_negative_second_side(self):
        """Test perimeter with negative second side"""
        with self.assertRaises(ValueError):
            perimeter(5, -3)

    def test_perimeter_both_sides_negative(self):
        """Test perimeter with both sides negative"""
        with self.assertRaises(ValueError):
            perimeter(-5, -3)

    def test_perimeter_negative_float_sides(self):
        """Test perimeter with negative float sides"""
        with self.assertRaises(ValueError):
            perimeter(-2.5, 3.7)
        with self.assertRaises(ValueError):
            perimeter(2.5, -3.7)

    def test_perimeter_none_first_side(self):
        """Test perimeter with None as first side"""
        with self.assertRaises(TypeError):
            perimeter(None, 5)

    def test_perimeter_none_second_side(self):
        """Test perimeter with None as second side"""
        with self.assertRaises(TypeError):
            perimeter(5, None)

    def test_perimeter_list_sides(self):
        """Test perimeter with list as sides"""
        with self.assertRaises(TypeError):
            perimeter([5], 3)
        with self.assertRaises(TypeError):
            perimeter(5, [3])

    def test_perimeter_square_case(self):
        """Test perimeter with equal sides (square)"""
        self.assertEqual(perimeter(4, 4), 16)
        self.assertAlmostEqual(perimeter(2.5, 2.5), 10.0)

    def test_perimeter_commutative_property(self):
        """Test that perimeter(a, b) == perimeter(b, a)"""
        self.assertEqual(perimeter(5, 3), perimeter(3, 5))
        self.assertAlmostEqual(perimeter(2.5, 3.7), perimeter(3.7, 2.5))


if __name__ == '__main__':
    unittest.main()