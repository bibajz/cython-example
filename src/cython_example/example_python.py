from functools import reduce
from operator import add

from cython_example.cythonized_ext import sum_powers_cythonized


def sum_powers_reduce_add(x: float, exp: int) -> float:
    """Compute x^exp + x^(exp-1) + ... + 1

    Use `functools.reduce` and `operator.add`.
    """
    return reduce(add, (x ** i for i in range(exp + 1)))


def sum_powers_reduce_lambda(x: float, exp: int) -> float:
    """Compute x^exp + x^(exp-1) + ... + 1

    Use `functools.reduce` and `lambda`.
    """
    return reduce(lambda a, b: a + b, (x ** i for i in range(exp + 1)))


def sum_powers_dumb(x: float, exp: int) -> float:
    """Compute x^exp + x^(exp-1) + ... + 1

    Use dumb for loop. :)
    """
    res = 0.0
    for i in range(exp + 1):
        res += x ** i

    return res


def sum_powers_formula(x: float, exp: int) -> float:
    """Compute x^exp + x^(exp-1) + ... + 1

    Be smart and realize there exists a formula for this operation. :)
    """
    return (x ** (exp + 1) - 1) / (x - 1)


def sum_powers_wrapped(x: float, exp: int) -> float:
    """Compute x^exp + x^(exp-1) + ... + 1

    Just call the cythonized function.
    """
    return sum_powers_cythonized(x, exp)
