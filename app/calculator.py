"""A tiny calculator.

Each function is deliberately small: in this repo, a feature = a branch = a PR.
"""


def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b 


def subtract(a: float, b: float) -> float:
    """Return a minus b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


# TODO(session): implement divide(a, b) on a feature branch and open a PR.
# Don't forget the division-by-zero case — there is a skipped test in
# tests/test_calculator.py waiting for you. See docs/exercises.md.
def divide(a: float, b: float) -> float:
    """Return a divided by b."""
    print('Dividing...')
    return a / b