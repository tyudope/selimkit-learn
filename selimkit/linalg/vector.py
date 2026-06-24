class Vector:
    def __init__(self, entries:list[float]) -> None:
        self.entries = entries 

    def __repr__(self) -> str:
        return f"Vector({self.entries})"