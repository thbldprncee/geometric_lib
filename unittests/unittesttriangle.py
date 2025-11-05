import unittest
import math

from geometric_lib.triangle import area, perimeter


class TriangleAreaTestCases(unittest.TestCase):
    """Test cases for triangle area function"""

    def test_triangle_area_integer_sides(self):
        """Test area with integer base and height"""
        self.assertEqual(area(6, 4), 6 * 4 / 2)
        self.assertEqual(area(10, 5), 10 * 5 / 2)

    def test_triangle_area_large_integers(self):
        """Test area with large integer base and height"""
        self.assertEqual(area(1000, 500), 1000 * 500 / 2)

    def test_triangle_area_float_values(self):
        """Test area with float base and height"""
        self.assertAlmostEqual(area(5.5, 3.2), 5.5 * 3.2 / 2)
        self.assertAlmostEqual(area(7.25, 4.75), 7.25 * 4.75 / 2)

    def test_triangle_area_mixed_types(self):
        """Test area with mixed integer and float"""
        self.assertAlmostEqual(area(6, 3.5), 6 * 3.5 / 2)
        self.assertAlmostEqual(area(4.5, 8), 4.5 * 8 / 2)

    def test_triangle_area_string_base(self):
        """Test area with string as base"""
        with self.assertRaises(TypeError):
            area('6', 4)

    def test_triangle_area_string_height(self):
        """Test area with string as height"""
        with self.assertRaises(TypeError):
            area(6, '4')

    def test_triangle_area_both_strings(self):
        """Test area with both base and height as strings"""
        with self.assertRaises(TypeError):
            area('6', '4')

    def test_triangle_area_bool_base(self):
        """Test area with boolean as base"""
        with self.assertRaises(TypeError):
            area(True, 4)

    def test_triangle_area_bool_height(self):
        """Test area with boolean as height"""
        with self.assertRaises(TypeError):
            area(6, False)

    def test_triangle_area_zero_base(self):
        """Test area with zero base"""
        with self.assertRaises(ValueError):
            area(0, 4)

    def test_triangle_area_zero_height(self):
        """Test area with zero height"""
        with self.assertRaises(ValueError):
            area(6, 0)

    def test_triangle_area_both_zero(self):
        """Test area with both base and height zero"""
        with self.assertRaises(ValueError):
            area(0, 0)

    def test_triangle_area_negative_base(self):
        """Test area with negative base"""
        with self.assertRaises(ValueError):
            area(-6, 4)

    def test_triangle_area_negative_height(self):
        """Test area with negative height"""
        with self.assertRaises(ValueError):
            area(6, -4)

    def test_triangle_area_both_negative(self):
        """Test area with both base and height negative"""
        with self.assertRaises(ValueError):
            area(-6, -4)

    def test_triangle_area_negative_float(self):
        """Test area with negative float values"""
        with self.assertRaises(ValueError):
            area(-5.5, 3.2)
        with self.assertRaises(ValueError):
            area(5.5, -3.2)

    def test_triangle_area_none_base(self):
        """Test area with None as base"""
        with self.assertRaises(TypeError):
            area(None, 4)

    def test_triangle_area_none_height(self):
        """Test area with None as height"""
        with self.assertRaises(TypeError):
            area(6, None)

    def test_triangle_area_list_values(self):
        """Test area with list as values"""
        with self.assertRaises(TypeError):
            area([6], 4)
        with self.assertRaises(TypeError):
            area(6, [4])

    def test_triangle_area_right_triangle(self):
        """Test area with right triangle dimensions"""
        self.assertEqual(area(3, 4), 6.0)
        self.assertEqual(area(5, 12), 30.0)

    def test_triangle_area_small_values(self):
        """Test area with small positive values"""
        self.assertAlmostEqual(area(1, 1), 0.5)
        self.assertAlmostEqual(area(2, 3), 3.0)


class TrianglePerimeterTestCases(unittest.TestCase):
    """Test cases for triangle perimeter function"""

    def test_triangle_perimeter_integer_sides(self):
        """Test perimeter with integer sides"""
        self.assertEqual(perimeter(3, 4, 5), 3 + 4 + 5)
        self.assertEqual(perimeter(5, 12, 13), 5 + 12 + 13)

    def test_triangle_perimeter_large_integers(self):
        """Test perimeter with large integer sides"""
        self.assertEqual(perimeter(100, 200, 300), 100 + 200 + 300)

    def test_triangle_perimeter_float_sides(self):
        """Test perimeter with float sides"""
        self.assertAlmostEqual(perimeter(3.5, 4.2, 5.1), 3.5 + 4.2 + 5.1)
        self.assertAlmostEqual(perimeter(2.25, 3.75, 4.5), 2.25 + 3.75 + 4.5)

    def test_triangle_perimeter_mixed_types(self):
        """Test perimeter with mixed integer and float"""
        self.assertAlmostEqual(perimeter(3, 4.5, 5), 3 + 4.5 + 5)
        self.assertAlmostEqual(perimeter(2.5, 3, 4.5), 2.5 + 3 + 4.5)

    def test_triangle_perimeter_equilateral(self):
        """Test perimeter with equilateral triangle"""
        self.assertEqual(perimeter(5, 5, 5), 15)
        self.assertEqual(perimeter(7, 7, 7), 21)

    def test_triangle_perimeter_isosceles(self):
        """Test perimeter with isosceles triangle"""
        self.assertEqual(perimeter(5, 5, 3), 13)
        self.assertEqual(perimeter(6, 4, 6), 16)

    def test_triangle_perimeter_string_first_side(self):
        """Test perimeter with string as first side"""
        with self.assertRaises(TypeError):
            perimeter('3', 4, 5)

    def test_triangle_perimeter_string_second_side(self):
        """Test perimeter with string as second side"""
        with self.assertRaises(TypeError):
            perimeter(3, '4', 5)

    def test_triangle_perimeter_string_third_side(self):
        """Test perimeter with string as third side"""
        with self.assertRaises(TypeError):
            perimeter(3, 4, '5')

    def test_triangle_perimeter_all_strings(self):
        """Test perimeter with all sides as strings"""
        with self.assertRaises(TypeError):
            perimeter('3', '4', '5')

    def test_triangle_perimeter_bool_sides(self):
        """Test perimeter with boolean sides"""
        with self.assertRaises(TypeError):
            perimeter(True, 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, False, 5)

    def test_triangle_perimeter_zero_first_side(self):
        """Test perimeter with zero first side"""
        with self.assertRaises(ValueError):
            perimeter(0, 4, 5)

    def test_triangle_perimeter_zero_second_side(self):
        """Test perimeter with zero second side"""
        with self.assertRaises(ValueError):
            perimeter(3, 0, 5)

    def test_triangle_perimeter_zero_third_side(self):
        """Test perimeter with zero third side"""
        with self.assertRaises(ValueError):
            perimeter(3, 4, 0)

    def test_triangle_perimeter_all_sides_zero(self):
        """Test perimeter with all sides zero"""
        with self.assertRaises(ValueError):
            perimeter(0, 0, 0)

    def test_triangle_perimeter_negative_first_side(self):
        """Test perimeter with negative first side"""
        with self.assertRaises(ValueError):
            perimeter(-3, 4, 5)

    def test_triangle_perimeter_negative_second_side(self):
        """Test perimeter with negative second side"""
        with self.assertRaises(ValueError):
            perimeter(3, -4, 5)

    def test_triangle_perimeter_negative_third_side(self):
        """Test perimeter with negative third side"""
        with self.assertRaises(ValueError):
            perimeter(3, 4, -5)

    def test_triangle_perimeter_all_sides_negative(self):
        """Test perimeter with all sides negative"""
        with self.assertRaises(ValueError):
            perimeter(-3, -4, -5)

    def test_triangle_perimeter_negative_float(self):
        """Test perimeter with negative float sides"""
        with self.assertRaises(ValueError):
            perimeter(-3.5, 4.2, 5.1)
        with self.assertRaises(ValueError):
            perimeter(3.5, -4.2, 5.1)

    def test_triangle_perimeter_none_sides(self):
        """Test perimeter with None as sides"""
        with self.assertRaises(TypeError):
            perimeter(None, 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, None, 5)

    def test_triangle_perimeter_list_sides(self):
        """Test perimeter with list as sides"""
        with self.assertRaises(TypeError):
            perimeter([3], 4, 5)
        with self.assertRaises(TypeError):
            perimeter(3, [4], 5)

    def test_triangle_perimeter_commutative_property(self):
        """Test that perimeter is commutative (order doesn't matter)"""
        self.assertEqual(perimeter(3, 4, 5), perimeter(4, 3, 5))
        self.assertEqual(perimeter(3, 4, 5), perimeter(5, 4, 3))
        self.assertEqual(perimeter(3, 4, 5), perimeter(3, 5, 4))

    def test_triangle_perimeter_small_values(self):
        """Test perimeter with small positive values"""
        self.assertEqual(perimeter(1, 1, 1), 3)
        self.assertEqual(perimeter(2, 3, 4), 9)

    def test_triangle_perimeter_valid_triangle_inequality(self):
        """Test perimeter with sides that satisfy triangle inequality"""
        # Valid triangles: sum of any two sides > third side
        self.assertEqual(perimeter(3, 4, 5), 12)  # Right triangle
        self.assertEqual(perimeter(5, 5, 8), 18)  # Isosceles triangle


if __name__ == '__main__':
    unittest.main()