#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Args:
    matrix (list of lists): Matrix of integers or floats.
    div (int or float): Divisor.

    Returns:
    list of lists: New matrix with elements rounded to 2 decimal places.

    Raises:
    TypeError: If matrix is not a list of lists of integers or floats,
               or if div is not a number.
    ZeroDivisionError: If div is equal to 0.
    TypeError: If each row of the matrix doesn't have the same size.
    """

    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not matrix or not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
