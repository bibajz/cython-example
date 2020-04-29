import pytest
from cython_example.cythonized_ext import (
    sum_powers_cythonized,
    sum_powers_formula_cythonized,
)
from cython_example.example_python import sum_powers_dumb, sum_powers_reduce_add


def test_import_cdef_function_is_invalid():
    """Show that cdef functions cannot be imported into Python."""
    with pytest.raises(ImportError):
        from cython_example.cythonized_ext import sum_powers


def test_function_versions_are_valid():
    """Provide a sanity check that cy/python versions produce same results."""
    assert isinstance(sum_powers_cythonized(10, 3), float)

    # Even though Cython version always produces float, Python implementations vary
    assert isinstance(sum_powers_dumb(10, 3), float)
    assert isinstance(sum_powers_reduce_add(10, 3), int)

    assert sum_powers_cythonized(10, 3) == sum_powers_formula_cythonized(10, 3) == 1111
    assert sum_powers_cythonized(10, 3) == sum_powers_dumb(10, 3)


IMPORTS_FOR_TIMEIT_SETUP = """\
from functools import reduce
from operator import add

from cython_example.cythonized_ext import (
    sum_powers_formula_cythonized,
    sum_powers_cythonized
)

from cython_example.example_python import (
    sum_powers_reduce_add,
    sum_powers_reduce_lambda,
    sum_powers_dumb,
    sum_powers_formula,
    sum_powers_wrapped
)
"""


@pytest.mark.performance
def test_compare_function_performance():
    """
    Compare performances of various implementations of the function. Sample output:

    Cython; without formula: 0.0754
    Cython; with formula: 0.0120
    Python; reduce with add: 0.3958
    Python; reduce with lambda: 0.4612
    Python; dumb for loop: 0.3413
    Python; formula: 0.0387
    Python; Cython without formula wrapped: 0.0775
    """
    import timeit

    # That formatting though :D
    print("\n\n")
    print(
        f"Cython; without formula: {timeit.timeit('sum_powers_cythonized(17, 13)', setup=IMPORTS_FOR_TIMEIT_SETUP, number=100000):.4f}"
    )
    print(
        f"Cython; with formula: {timeit.timeit('sum_powers_formula_cythonized(17, 13)', setup=IMPORTS_FOR_TIMEIT_SETUP, number=100000):.4f}"
    )
    print(
        f"Python; reduce with add: {timeit.timeit('sum_powers_reduce_add(17, 13)', setup=IMPORTS_FOR_TIMEIT_SETUP, number=100000):.4f}"
    )
    print(
        f"Python; reduce with lambda: {timeit.timeit('sum_powers_reduce_lambda(17, 13)', setup=IMPORTS_FOR_TIMEIT_SETUP, number=100000):.4f}"
    )
    print(
        f"Python; dumb for loop: {timeit.timeit('sum_powers_dumb(17, 13)', setup=IMPORTS_FOR_TIMEIT_SETUP, number=100000):.4f}"
    )
    print(
        f"Python; formula: {timeit.timeit('sum_powers_formula(17, 13)', setup=IMPORTS_FOR_TIMEIT_SETUP, number=100000):.4f}"
    )
    print(
        f"Python; Cython without formula wrapped: {timeit.timeit('sum_powers_wrapped(17, 13)', setup=IMPORTS_FOR_TIMEIT_SETUP, number=100000):.4f}"
    )
    print("\n\n")
