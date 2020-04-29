# cython: language_level=3

from libc.math cimport pow

cdef double sum_powers (double x, int exp):
    """Compute x^exp + x^(exp-1) + ... + 1 as a double.

    cdef functions CANNOT be called from Python.
    """
    cdef double sum = 0.0
    cdef int i = 0

    for i in range(exp + 1):
        sum += pow(x, i)

    return sum

cpdef double sum_powers_cythonized (double x, int exp):
    """cpdef functions CAN be called from Python."""
    return sum_powers(x, exp)

cpdef double sum_powers_formula_cythonized (double x, int exp):
    return ( pow(x, exp + 1) - 1 ) / ( x - 1 )