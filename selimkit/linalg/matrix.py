class Matrix:


    def __init__(self, rows: list[list[float]]) -> None:
        """Initialize a matrix from a list of rows.
        
        
        Args:
            rows: A list of rows, where each row is a list of numbers.
            All rows must have the same length (rectangular) .
            Empy matrices ([]) and matrices with empty rows ([[]]) are allowed.

        Raises:
            TypeError: If rows is not a list, or contains non-list elements.
            ValueError: If rows have different length (jagged matrix).
        
        """


        if not isinstance(rows, list):
            raise TypeError(f"Expected list of rows, got {type(rows).__name__}")
        

        if rows and not all (isinstance(row, list) for row in rows):
            raise TypeError("All rows must be lists")
        
        if rows:
            expected_length = len(rows[0])
            if not all (len(row) == expected_length for row in rows):
                raise ValueError("All rows must have the same length")
            
        
        self.entries = rows