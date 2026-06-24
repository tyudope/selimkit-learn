from selimkit.linalg import Vector

def test_vector_creation() -> None:
    v = Vector([1.0, 2.0, 3.0])
    assert v.entries == [1.0, 2.0, 3.0]


def test_vector_repr() -> None:
    v = Vector([1.0,2.0])
    assert repr(v) == "Vector([1.0, 2.0])"