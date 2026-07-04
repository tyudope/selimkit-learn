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


    def __add__(self, other:"Vector") -> "Vector":
        """Add two vectors and return a new vector with the same dimension.
        
        [1,2] + [2,3] = [3, 5]

        Component-wise addition: To add two vectors a and b you independently,
        add their corresponding elements.
        
        Remark: By default, vector addition is not defined for vectors of different
        dimensions.
        """

        if not isinstance(other, Vector):
            return NotImplemented
        
        if len(self.entries) != len(other.entries):
            raise ValueError("For Vector Addition, Dimensions must match.")

        return Vector([a + b for a, b in zip(self.entries, other.entries)])
    
    def __sub__(self, other:"Vector") -> "Vector":
        """
        Subtract two vectors and return a new vector with the same dimension

        [3,2] - [2,1] = [1,1]

        Component-wise subtraction: To subtract two vectors a and b you independently,
        subtract their corresponding elements.

        Remark: By default, vector subtraction is not defined for vectors of different 
        dimensions.
        
        """

        if not isinstance(other, Vector):
            return NotImplemented
        
        if len(self.entries) != len(other.entries):
            raise ValueError("For Vector subtraction, Dimensions must match.")
        

        return Vector([a - b for a,b in zip(self.entries, other.entries)])
    

    def __mul__(self, scalar) -> "Vector":
        """
        Scalar multiplication of the vector. A fundamental linear algebra
        operatoin where a vector is multiplied by a real number (scalar)

        [6,5,4] x 3 = [18,15,12]

        Component-wise multiplication: To scale vector with scalar x you independently
        multiply elements with the scalar.
        
        """

        if isinstance(scalar,bool) or not isinstance(scalar, (int, float)):
            return NotImplemented
        

        return Vector([entry * scalar for entry in self.entries])
    

    def __rmul__(self, scalar) -> "Vector":
        """Delegate to the __mul__"""
        return self.__mul__(scalar)
    


    def __neg__(self) -> "Vector":
        """A new vectgor with the exact same magnitude (length) but the opposite direction."""
        
        return self * -1


