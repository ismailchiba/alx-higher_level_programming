#!/usr/bin/python3
"""This module contain a function that multiplies two matrix"""


def matrix_mul(m_a, m_b):
    """matrix_mul function that multiplies two matrix
    Args:
        m_a (list of lists): first matrix
        m_b (list of lists): second matrix
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # variables to verify if both m_a and m_b can be multiplied
    num_colum1 = 0
    num_row2 = 0

    # Check requirements for matrix m_a
    if m_a == []:
        raise ValueError("m_a can't be empty")
    for row1 in m_a:
        if not isinstance(row1, list):
            raise TypeError("m_a must be a list of lists")
        len1 = len(m_a[0])
        if row1 == []:
            raise ValueError("m_a can't be empty")
        if len1 != len(row1):
            raise TypeError("each row of m_a must be of the same size")
        num_colum1 = len(row1)
        for column1 in row1:
            if not isinstance(column1, int) and not isinstance(column1, float):
                raise TypeError("m_a should contain only integers or floats")

    # Check requirements for matrix m_b
    if m_b == []:
        raise ValueError("m_b can't be empty")
    for row2 in m_b:
        if not isinstance(row2, list):
            raise TypeError("m_b must be a list of lists")
        len2 = len(m_b[0])
        if row2 == []:
            raise ValueError("m_b can't be empty")
        if len2 != len(row2):
            raise TypeError("each row of m_b must be of the same size")
        num_row2 += 1
        for column2 in row2:
            if not isinstance(column2, int) and not isinstance(column2, float):
                raise TypeError("m_b should contain only integers or floats")

    # Check if the multiplication is posible
    if num_colum1 != num_row2:
        raise ValueError("m_a and m_b can't be multiplied")

    mul_matrix = []

    for row_1 in m_a:
        len_0 = 0
        l_row = []
        while len_0 < len(m_b[0]):
            result = 0
            k = 0
            for column_1 in row_1:
                result += column_1 * m_b[k][len_0]
                k += 1
            l_row.append(result)
            len_0 += 1
        mul_matrix.append(l_row)

    return mul_matrix
