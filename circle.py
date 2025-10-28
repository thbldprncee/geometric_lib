import math

def area(r):
    """
    Calculate the area of a circle.

    Args:
        r (float): Radius of the circle. Must be a positive number.

    Returns:
        float: Area of the circle calculated using the formula S = π * r²
    """
    return math.pi * r * r


def perimeter(r):
    """
    Calculate the circumference (perimeter) of a circle.

    Args:
        r (float): Radius of the circle. Must be a positive number.

    Returns:
        float: Circumference of the circle calculated using the formula P = 2 * π * r
    """
    return 2 * math.pi * r

