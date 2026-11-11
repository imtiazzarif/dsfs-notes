"""Small linear algebra helpers used by the notebook.

This implements a tiny subset of the helpers from Joel Grus' "scratch" package
so the notebook import `from scratch.linear_algebra import ...` works.
"""

from math import sqrt
from typing import List

Vector = List[float]


def add(v: Vector, w: Vector) -> Vector:
    """Element-wise addition of two vectors."""
    assert len(v) == len(w), "vectors must be the same length"
    return [vi + wi for vi, wi in zip(v, w)]


def subtract(v: Vector, w: Vector) -> Vector:
    """Element-wise subtraction of two vectors."""
    assert len(v) == len(w), "vectors must be the same length"
    return [vi - wi for vi, wi in zip(v, w)]


def scalar_multiply(c: float, v: Vector) -> Vector:
    """Multiply every element of v by scalar c."""
    return [c * vi for vi in v]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums a list of vectors element-wise."""
    assert vectors, "no vectors provided!"
    num_elements = len(vectors[0])
    assert all(len(v) == num_elements for v in vectors), "different sizes!"
    return [sum(vector[i] for vector in vectors) for i in range(num_elements)]


def vector_mean(vectors: List[Vector]) -> Vector:
    """Computes the element-wise average of a list of vectors."""
    n = len(vectors)
    return scalar_multiply(1 / n, vector_sum(vectors))


def dot(v: Vector, w: Vector) -> float:
    """Dot product of two vectors."""
    assert len(v) == len(w), "vectors must be the same length"
    return sum(vi * wi for vi, wi in zip(v, w))


def sum_of_squares(v: Vector) -> float:
    """Sum of squares of a vector."""
    return dot(v, v)


def magnitude(v: Vector) -> float:
    """Euclidean length (L2 norm) of v."""
    return sqrt(sum_of_squares(v))


def distance(v: Vector, w: Vector) -> float:
    """Euclidean distance between two vectors."""
    return magnitude(subtract(v, w))
