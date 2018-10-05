#!/usr/bin/python3
""" define lazy_matrix_mul using numpy module"""


def lazy_matrix_mul(m_a, m_b):
    """ matrix mul using numpy module """
    __check_input(m_a, m_b)
    import numpy as np
    return np.matmul(m_a, m_b)


def __check_input(m_a, m_b):
    """ check input for lazy_matrix_mul """
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    if not all(isinstance(r, list) for r in m_a):
        raise TypeError('m_a must be a list of lists')
    if not all(isinstance(r, list) for r in m_b):
        raise TypeError('m_b must be a list of lists')
    if len(m_a) == 0 or any(len(r) == 0 for r in m_a):
        raise ValueError('m_a can\'t be empty')
    if len(m_a) == 0 or any(len(r) == 0 for r in m_b):
        raise ValueError('m_b can\'t be empty')
    if not all(isinstance(e, (int, float)) for r in m_a for e in r):
        raise TypeError('m_a should contain only integers or floats')
    if not all(isinstance(e, (int, float)) for r in m_b for e in r):
        raise TypeError('m_b should contain only integers or floats')
    if len(set([len(row) for row in m_a])) != 1:
        raise TypeError('each row of m_a must should be of the same size')
    if len(set([len(row) for row in m_b])) != 1:
        raise TypeError('each row of m_b must should be of the same size')
    if len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can\'t be multiplied')
