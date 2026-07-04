import pytest
from selimkit.linalg import Vector

# Initialization
def test_vector_creation() -> None:
    v = Vector([1.0, 2.0, 3.0])
    assert v.entries == [1.0, 2.0, 3.0]

# Representation
def test_vector_repr() -> None:
    v = Vector([1.0,2.0])
    assert repr(v) == "Vector([1.0, 2.0])"



# Equality.
def test_eq_identical_vectors() -> None:
    v1 = Vector([1.0, 2.0])
    v2 = Vector([1.0, 2.0])
    assert v1 == v2


def test_eq_different_values() -> None:
    v1 = Vector([1.0, 2.0])
    v2 = Vector([1.1, 2.0])
    assert v1 != v2

def test_eq_different_dimensions() -> None:
    v1 = Vector([1.0, 2.0])
    v2 = Vector([1.0, 2.0, 3.0])
    assert v1 != v2 

def test_eq_non_vector_returns_false() -> None:
    v1 = Vector([1.0, 2.0])
    v2 = [1.0, 2.0]
    assert v1 != v2




# Addition
def test_add_valid_dimensions() -> None:
    v1 = Vector([1.0,2.0,3.0])
    v2 = Vector([4.0,5.0,6.0])

    assert v1 + v2 == Vector([5.0, 7.0, 9.0])


def test_add_mismatched_dimensions_raises() -> None:
    """Vector addition with mismatched dimensions should raise ValueError."""
    v1 = Vector([1.0,2.0])
    v2 = Vector([1.0,2.0,3.0])


    with pytest.raises(ValueError): 
        # is a context manager that expects a ValueError to occurs inside the with block
        # If it does -> Test passes
        # If no error is raised -> Test fails
        # If a different error is raised -> Test Fails
        v1 + v2
    
    

def test_add_non_vector_raises() -> None:
    v1 = Vector([1.0, 2.0])
    
    with pytest.raises(TypeError):
        v1 + 5



# Subtraction
def test_subtract_valid_dimensions() -> None:
    v1 = Vector([3.0, 2.0])
    v2 = Vector([1.0, 1.0])

    assert v1 - v2 == Vector([2.0, 1.0])


def test_subtract_non_valid_dimensions_raises() -> None:
    """Vector subtraction with non-valid dimensions should raise ValueError"""
    v1 = Vector([2.0,1.0])
    v2 = Vector([2.0,1.0,3.0])

    with pytest.raises(ValueError):
        v1 - v2 

def test_subtract_non_vector_raises() -> None:
    v1 = Vector([1.0, 2.0])

    with pytest.raises(TypeError):
        v1 - 5


# Scalar multiplication
def test_mul_valid_scalar() -> None:
    v1 = Vector([1.0,2.0,3.0])

    assert v1 * 2 == Vector([2.0,4.0,6.0])
def test_rmul_valid_scalar() -> None:
    v1 = Vector([1.0, 2.0, 3.0])
    assert 2 * v1 == Vector([2.0,4.0,6.0])

def test_mul_zero_mul() -> None:
    v1 = Vector([1.0,2.0,3.0])
    assert v1 * 0 == Vector([0.0,0.0,0.0])

def test_mul_unvalid_scalar_raises() -> None:
    v1 = Vector([1.0,2.0,3.0])

    with pytest.raises(TypeError):
        v1 * "selim"


# Negation
def test_neg() -> None:
    v1 = Vector([1.0, 2.0])
    v2 = -v1

    assert v2 == Vector([-1.0, -2.0])
    assert -v2 == v1


# Dimension
def test_dimension() -> None:
    assert Vector([1.0, 2.0]).dimension() == 2
    assert Vector([1.0,2.0, 3.0]).dimension() == 3
    assert Vector([42.0]).dimension() == 1