import pytest
from selimkit.linalg import Matrix

# Initializaiton 
def test_valid_matrix_creation() -> None:
    valid = Matrix([[1,2],[3,4]])
    assert valid.entries == [[1,2],[3,4]]

def test_empty_matrix_allowed() -> None:
    """A 0x0 matrix (no rows) should be allowed."""
    valid = Matrix([])
    assert valid.entries == []

def test_matrix_with_empty_rows_allowed() -> None:
    """A 1x0 matrix (one row, no column) should be allowed."""
    m = Matrix([[]])
    assert m.entries == [[]]

def test_jagged_matrix_raises() -> None:
    with pytest.raises(ValueError):
        Matrix([[1,2],[1,2,3]])

def test_non_list_input_raises() -> None:
    with pytest.raises(TypeError):
        Matrix('selim')

def test_flat_list_input_raises() -> None:
    with pytest.raises(TypeError):
        Matrix([1,2,3])