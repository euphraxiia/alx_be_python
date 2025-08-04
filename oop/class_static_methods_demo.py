class Calculator:
    """A class demonstrating the use of class methods and static methods."""
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Static methods don't have access to 'self' or 'cls' and behave like regular functions.
        They are included in a class because they are logically related to the class.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Class methods have access to the class itself via 'cls' parameter.
        They can access class attributes and other class methods.
        
        Args:
            cls: Reference to the class itself
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
