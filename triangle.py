def area(a, h):
    """
    Calculate the area of a triangle.

    Parameters:
    a (int): base of the triangle
    h (int): height of the triangle

    Returns:
    float: area of the triangle calculated as (a * h) / 2
    """
    return a * h / 2

def perimeter(a, b, c):
    """
    Calculate the perimeter of a triangle.

    Parameters:
    a (int): first side of the triangle
    b (int): second side of the triangle
    c (int): third side of the triangle

    Returns:
    int: perimeter of the triangle calculated as a + b + c
    """
    return a + b + c