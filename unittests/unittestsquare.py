import unittest
import math

from geometric_lib.square import area, perimeter


class SquareAreaTestCases(unittest.TestCase):
    """Test cases for square area function"""

    def test_square_integer_side(self):
        """Test area with integer side"""
        self.assertEqual(area(5), 5 * 5)
        self.assertEqual(area(10), 10 * 10)

    def test_square_large_integer(self):
        """Test area with large integer side"""
        self.assertEqual(area(65536), 65536 * 65536)

    def test_square_float_side(self):
        """Test area with float side"""
        self.assertAlmostEqual(area(2.5), 2.5 * 2.5)
        self.assertAlmostEqual(area(10.75), 10.75 * 10.75)

    def test_square_string_side(self):
        """Test area with string input"""
        with self.assertRaises(TypeError):
            area('23')

    def test_square_another_string(self):
        """Test area with another string input"""
        with self.assertRaises(TypeError):
            area('123')

    def test_square_bool_true(self):
        """Test area with boolean True"""
        with self.assertRaises(TypeError):
            area(True)

    def test_square_bool_false(self):
        """Test area with boolean False"""
        with self.assertRaises(TypeError):
            area(False)

    def test_square_zero_side(self):
        """Test area with zero side"""
        with self.assertRaises(ValueError):
            area(0)

    def test_square_negative_integer(self):
        """Test area with negative integer"""
        with self.assertRaises(ValueError):
            area(-5)

    def test_square_large_negative_integer(self):
        """Test area with large negative integer"""
        with self.assertRaises(ValueError):
            area(-65536)

    def test_square_negative_float(self):
        """Test area with negative float"""
        with self.assertRaises(ValueError):
            area(-3.14)
        with self.assertRaises(ValueError):
            area(-2.5)

    def test_square_none_value(self):
        """Test area with None value"""
        with self.assertRaises(TypeError):
            area(None)

    def test_square_list_value(self):
        """Test area with list input"""
        with self.assertRaises(TypeError):
            area([5])

    def test_square_dict_value(self):
        """Test area with dictionary input"""
        with self.assertRaises(TypeError):
            area({'side': 5})

    def test_square_tuple_value(self):
        """Test area with tuple input"""
        with self.assertRaises(TypeError):
            area((5,))

    def test_square_small_positive_float(self):
        """Test area with small positive float"""
        self.assertAlmostEqual(area(0.5), 0.25)
        self.assertAlmostEqual(area(0.1), 0.01)

    def test_square_one_side(self):
        """Test area with side = 1"""
        self.assertEqual(area(1), 1)


class SquarePerimeterTestCases(unittest.TestCase):
    """Test cases for square perimeter function"""

    def test_perimeter_integer_side(self):
        """Test perimeter with integer side"""
        self.assertEqual(perimeter(5), 4 * 5)
        self.assertEqual(perimeter(10), 4 * 10)

    def test_perimeter_large_integer(self):
        """Test perimeter with large integer side"""
        self.assertEqual(perimeter(65536), 4 * 65536)

    def test_perimeter_float_side(self):
        """Test perimeter with float side"""
        self.assertAlmostEqual(perimeter(2.5), 4 * 2.5)
        self.assertAlmostEqual(perimeter(10.75), 4 * 10.75)

    def test_perimeter_string_side(self):
        """Test perimeter with string input"""
        with self.assertRaises(TypeError):
            perimeter('23')

    def test_perimeter_another_string(self):
        """Test perimeter with another string input"""
        with self.assertRaises(TypeError):
            perimeter('123')

    def test_perimeter_bool_true(self):
        """Test perimeter with boolean True"""
        with self.assertRaises(TypeError):
            perimeter(True)

    def test_perimeter_bool_false(self):
        """Test perimeter with boolean False"""
        with self.assertRaises(TypeError):
            perimeter(False)

    def test_perimeter_zero_side(self):
        """Test perimeter with zero side"""
        with self.assertRaises(ValueError):
            perimeter(0)

    def test_perimeter_negative_integer(self):
        """Test perimeter with negative integer"""
        with self.assertRaises(ValueError):
            perimeter(-5)

    def test_perimeter_large_negative_integer(self):
        """Test perimeter with large negative integer"""
        with self.assertRaises(ValueError):
            perimeter(-65536)

    def test_perimeter_negative_float(self):
        """Test perimeter with negative float"""
        with self.assertRaises(ValueError):
            perimeter(-3.14)
        with self.assertRaises(ValueError):
            perimeter(-2.5)

    def test_perimeter_none_value(self):
        """Test perimeter with None value"""
        with self.assertRaises(TypeError):
            perimeter(None)

    def test_perimeter_list_value(self):
        """Test perimeter with list input"""
        with self.assertRaises(TypeError):
            perimeter([5])

    def test_perimeter_dict_value(self):
        """Test perimeter with dictionary input"""
        with self.assertRaises(TypeError):
            perimeter({'side': 5})

    def test_perimeter_tuple_value(self):
        """Test perimeter with tuple input"""
        with self.assertRaises(TypeError):
            perimeter((5,))

    def test_perimeter_small_positive_float(self):
        """Test perimeter with small positive float"""
        self.assertAlmostEqual(perimeter(0.5), 2.0)
        self.assertAlmostEqual(perimeter(0.1), 0.4)

    def test_perimeter_one_side(self):
        """Test perimeter with side = 1"""
        self.assertEqual(perimeter(1), 4)

    def test_perimeter_relationship_with_area(self):
        """Test mathematical relationship between perimeter and area"""
        side = 4
        # For square: perimeter = 4 * side, area = side²
        # So: perimeter = 4 * sqrt(area)
        calculated_perimeter = 4 * math.sqrt(area(side))
        self.assertAlmostEqual(perimeter(side), calculated_perimeter)


if __name__ == '__main__':
    unittest.main()