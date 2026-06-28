class Vector:
    def __init__(self, entries:list[float]) -> None:
        self.entries = entries 

    def __repr__(self) -> str:
        return f"Vector({self.entries})"
    
    def __eq__(self,  other: "Vector") -> bool:
        """ Return True if other is a Vector with identical entries.
        
        Two vectors are equal if and only if they have the same dimension
        and the same component values in the same order. Returns NotImplemented
        for non-Vector operands so Python can fall back to other comparison.
        """

        if not isinstance(other, Vector):
            return NotImplemented
    
        return self.entries == other.entries


