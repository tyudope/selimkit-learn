from selimkit.linalg import Vector

def test_vector_creation() -> None:
    v = Vector([1.0, 2.0, 3.0])
    assert v.entries == [1.0, 2.0, 3.0]


def test_vector_repr() -> None:
    v = Vector([1.0,2.0])
    assert repr(v) == "Vector([1.0, 2.0])"



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

